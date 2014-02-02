title: "JOINing against VIEWs can be harmful"
slug: joining-against-views-can-be-harmful
id: 5046
date: 2013-11-04 14:13:59
tags: 
- ctes
- postgres
- query optimization
categories: 
- postgresql

I had a recent code review problem that was very curious at first glance, but came down to the use of complex VIEW in an even more complicated and frequently used reporting query.

I'll just paste [a edited version of the review below](https://github.com/mozilla/socorro/pull/1613#discussion_r7203097).

tl;dr: Don't use `product_info` (a view, not a table) in this query, move WHERE clauses for product_name and version_string into the `infos` CTE, strictly limit the number of columns in tables being joined

This query is unfortunately doomed because it is using `product_info` -- a view which already contains data from product_versions. There are four other tables which we don't care about for the query that are included in the view.

As a result, you get a self-join many times over. A hint at the horrors of what Postgres decides to do with this is here:

    Unique  (cost=10248.32..10248.35 rows=1 width=294)
       CTE infos
         -&gt;  Hash Right Join  (cost=301.82..1683.83 rows=40195 width=96)
               Hash Cond: (pvb.product_version_id = pv.product_version_id)
               -&gt;  Seq Scan on product_version_builds pvb  (cost=0.00..768.71 rows=42271 width=16)
               -&gt;  Hash  (cost=282.46..282.46 rows=1549 width=84)
                     -&gt;  Hash Right Join  (cost=218.53..282.46 rows=1549 width=84)
                           Hash Cond: (pv.product_version_id = pi.product_version_id)
                           -&gt;  Seq Scan on product_versions pv  (cost=0.00..40.29 rows=1629 width=35)
                           -&gt;  Hash  (cost=199.17..199.17 rows=1549 width=53)
                                 -&gt;  Subquery Scan on pi  (cost=179.81..199.17 rows=1549 width=53)
                                       -&gt;  Sort  (cost=179.81..183.68 rows=1549 width=62)
                                             Sort Key: product_versions.product_name, product_versions.version_string
                                             -&gt;  Hash Join  (cost=5.70..97.73 rows=1549 width=62)
                                                   Hash Cond: ((product_versions.product_name = product_release_channels.product_name) AND (product_versions.build_type = product_release_channels.release_channel))
                                                   -&gt;  Seq Scan on product_versions  (cost=0.00..40.29 rows=1629 width=52)
                                                   -&gt;  Hash  (cost=5.03..5.03 rows=45 width=42)
                                                         -&gt;  Hash Join  (cost=2.34..5.03 rows=45 width=42)
                                                               Hash Cond: (product_release_channels.release_channel = release_channels.release_channel)
                                                               -&gt;  Hash Join  (cost=1.23..3.29 rows=45 width=34)
                                                                     Hash Cond: (product_release_channels.product_name = products.product_name)
                                                                     -&gt;  Seq Scan on product_release_channels  (cost=0.00..1.45 rows=45 width=22)
                                                                     -&gt;  Hash  (cost=1.10..1.10 rows=10 width=12)
                                                                           -&gt;  Seq Scan on products  (cost=0.00..1.10 rows=10 width=12)
                                                               -&gt;  Hash  (cost=1.05..1.05 rows=5 width=8)
                                                                     -&gt;  Seq Scan on release_channels  (cost=0.00..1.05 rows=5 width=8)
    `</pre>

    Whenever you see so many nested joins, subquery sorts and sequence scans mushed together in a staircase, that's a signal that we should investigate whether the query we're running is really what we thought it was.

    While @peterbe dug through code with me, he mentioned that `product_info` was a view! Now all the self-JOINs made sense and I started refactoring.

    The `product_info` view was being deconstructed into it's component parts, which already included product_versions (resulting in a self-join) and including a bunch of junk that for the purposes of this query, we don't really care about. So, as the first step, I just made a copy of the SELECT query from the view (you can get that by running `\d+ product_info` in `psql` or you can dig it out of the `socorro/external/postgresql/procs/views` section of our code.

    Here's my proposal for what should go into `infos`:

    <pre>`         SELECT 
                    product_versions.product_version_id
                    , product_versions.version_string
                    , 'new'::text AS which_table
                    , product_versions.product_name
                    , product_versions.release_version
                    , product_versions.build_type
                    , product_version_builds.build_id
                    , product_versions.is_rapid_beta
                    , product_versions.rapid_beta_id
                    , product_versions.version_sort
            FROM product_versions
                    LEFT JOIN product_version_builds USING (product_version_id)
            WHERE  %(product name and versions)s
    `</pre>

    We really need to move the product name and version filtering to this portion of the query because otherwise we end up doing a horrible self join on a 42,000 row table! :watch:

    Here's what the self-join looks like in the EXPLAIN:

    <pre>`   -&gt;  Sort  (cost=8564.48..8564.49 rows=1 width=294)
             Sort Key: i1.version_sort, i1.product_version_id, i1.product_name, i1.version_string, i1.which_table, i1.release_version, i1.build_type, i1.build_id, i1.is_rapid_beta, i2.is_rapid_beta, ((((i2.product_nam
    e)::text || ':'::text) || (i2.version_string)::text))
             -&gt;  Merge Join  (cost=7755.52..8564.47 rows=1 width=294)
                   Merge Cond: ((i1.product_name = i2.product_name) AND (i1.release_version = i2.release_version) AND (i1.build_type = i2.build_type))
                   Join Filter: (((i1.product_name = 'Firefox'::citext) AND (i1.version_string = '26.0a2'::citext) AND (i1.version_string = i2.version_string)) OR ((i1.rapid_beta_id = i2.product_version_id) AND (i2.pr
    oduct_name = 'Firefox'::citext) AND (i2.version_string = '26.0a2'::citext) AND (i2.is_rapid_beta IS TRUE)))
                   -&gt;  Sort  (cost=3877.76..3978.25 rows=40195 width=233)
                         Sort Key: i1.product_name, i1.release_version, i1.build_type
                         -&gt;  CTE Scan on infos i1  (cost=0.00..803.90 rows=40195 width=233)
                   -&gt;  Sort  (cost=3877.76..3978.25 rows=40195 width=133)
                         Sort Key: i2.product_name, i2.release_version, i2.build_type
                         -&gt;  CTE Scan on infos i2  (cost=0.00..803.90 rows=40195 width=133)
    `</pre>

    ![sad_kitten](https://f.cloud.github.com/assets/54803/1403698/ba78397a-3cf7-11e3-81d4-9d76ada8f290.jpg)

    This is pretty sad. The _Sort_ at the top of Mt. Sadness. There are a series of sorts further down that are just HUGE because we're tossing 45k records that must be joined to each other, and the width of the query is 294 -- _294 columns_ in addition to our 45k rows.

    The obvious (but sadly not always effective) thing to try is to see if we can filter our rows out earlier. Because we're using `infos`, conveniently, that looks possible without too much trouble.

    That just leaves sorting out the rapid beta self-join, which based on my tests should be pretty easy to continue to do in the body of the main SELECT, at line 125.

    With the changes I proposed, the estimated duration of this query is ~200 ms in stage and the query plan looks like:

    <pre>`                                                                                QUERY PLAN                                                                                 
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     HashAggregate  (cost=37.07..37.08 rows=1 width=294) (actual time=221.131..221.149 rows=31 loops=1)
       CTE infos
         -&gt;  Nested Loop Left Join  (cost=0.00..35.18 rows=26 width=64) (actual time=0.136..0.459 rows=150 loops=1)
               -&gt;  Index Scan using product_version_version_key on product_versions  (cost=0.00..7.27 rows=1 width=52) (actual time=0.111..0.112 rows=1 loops=1)
                     Index Cond: ((product_name = 'Firefox'::citext) AND (version_string = '26.0a2'::citext))
               -&gt;  Index Only Scan using product_version_builds_key on product_version_builds  (cost=0.00..27.58 rows=33 width=16) (actual time=0.019..0.268 rows=150 loops=1)
                     Index Cond: (product_version_id = product_versions.product_version_id)
                     Heap Fetches: 150
       -&gt;  Hash Join  (cost=0.84..1.86 rows=1 width=294) (actual time=0.943..47.334 rows=22500 loops=1)
             Hash Cond: (i1.product_version_id = i2.product_version_id)
             Join Filter: ((i1.version_string = i2.version_string) OR ((i1.rapid_beta_id = i2.product_version_id) AND (i2.is_rapid_beta IS TRUE)))
             -&gt;  CTE Scan on infos i1  (cost=0.00..0.52 rows=26 width=233) (actual time=0.141..0.236 rows=150 loops=1)
             -&gt;  Hash  (cost=0.52..0.52 rows=26 width=69) (actual time=0.778..0.778 rows=150 loops=1)
                   Buckets: 1024  Batches: 1  Memory Usage: 8kB
                   -&gt;  CTE Scan on infos i2  (cost=0.00..0.52 rows=26 width=69) (actual time=0.002..0.664 rows=150 loops=1)
     Total runtime: 221.321 ms
    (16 rows)
    
