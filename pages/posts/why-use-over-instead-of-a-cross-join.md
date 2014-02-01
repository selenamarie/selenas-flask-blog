title: "Fancy SQL Monday: Why use OVER() instead of a CROSS JOIN?"
id: 4964
date: 2013-08-05 15:44:33
tags: 
categories: 
- postgresql

**EDIT:** I had to add this, because it was cracking me up:

[caption width="540" align="alignnone"]![](http://i.imgur.com/Jc3RPkP.png) FOR LIKE EVERY REASON EVER[/caption]

I'm reimplementing some expensive database queries, moving them from our middleware into materialized view tables. We make pretty extensive use of [Common Table Expressions](http://www.postgresql.org/docs/9.3/static/queries-with.html) (CTEs). And we generate many reporting queries that calculate averages and percentages of a total. One way this could be done is with a `CROSS JOIN`, which is a [cartesian product](http://en.wikipedia.org/wiki/Cartesian_product) of two tables, adding the total and then the percentage calculation to our original table that produces counts of events. For information about `JOIN` types supported by PostgreSQL, see [SELECT...FROM documentation](http://www.postgresql.org/docs/9.3/static/sql-select.html#SQL-FROM).

Or we could use `OVER()`, one of several [Window Functions](http://www.postgresql.org/docs/9.3/static/tutorial-window.html) supported by Postgres. From the Postgres documentation, Window Functions are:

> A window function performs a calculation across a set of table rows that are somehow related to the current row. This is comparable to the type of calculation that can be done with an aggregate function. But unlike regular aggregate functions, use of a window function does not cause rows to become grouped into a single output row — the rows retain their separate identities. Behind the scenes, the window function is able to access more than just the current row of the query result.

A few other folks have written about Window Functions: [Postgres Guide to Window Functions](http://postgresguide.com/tips/window.html), [Window Functions: Postgres's best kept secret](http://www.openlogic.com/wazi/bid/188074/Window-Functions-PostgreSQL-s-Best-Kept-Secret), [SQL Window Functions](http://hashrocket.com/blog/posts/sql-window-functions) (examples in Ruby). "All built-in and user-defined aggregate functions -- such as count, max, bit_or, or xmlagg" -- are available for computation as a window function, [quoting Open Logic](http://www.openlogic.com/wazi/bid/188074/Window-Functions-PostgreSQL-s-Best-Kept-Secret), who phrased it well.

If you read about [OVER()](http://www.postgresql.org/docs/9.3/static/sql-expressions.html#SYNTAX-WINDOW-FUNCTIONS), you'll see that all the examples specify a `PARTITION` clause. But you don't have to specify a `PARTITION` to take advantage of the feature.

We had a query containing two CTEs and a final `SELECT` that produced the matview data. Here's an example of that query:

    WITH crashes as (
      SELECT
        product_name as category
        , version_string
        , SUM(report_count) as report_count
      FROM signature_summary_products
      JOIN signatures USING (signature_id)
      WHERE signatures.signature = 'libflashplayer.so@0x1f2a14'
      AND report_date &gt;= now()::date - '15 day'::interval
      AND report_date &lt; now()::date 
      GROUP BY product_name, version_string
    ),
    totals as (
      SELECT
        category
        , version_string
        , report_count
        , SUM(report_count) OVER () as total_count
      FROM crashes
    )
    SELECT category
      , version_string
      , report_count
      , round((report_count * 100::numeric)/total_count,3)::TEXT
      as percentage
    FROM totals
    ORDER BY report_count DESC;
    `</pre>

    The part under consideration is:

    <pre>`    , SUM(report_count) OVER () as total_count
    `</pre>

    So, you see that `OVER()` has no `PARTITION` defined, meaning that the SUM will be calculated over the entire result.

    Here is that same query, implemented using `SUM()` and a `CROSS JOIN`:

    <pre>`WITH crashes as (
      SELECT
        product_name as category
        , version_string
         , SUM(report_count) as report_count
      FROM signature_summary_products
      JOIN signatures USING (signature_id)
      WHERE signatures.signature = 'libflashplayer.so@0x1f2a14'
        AND report_date &gt;= now()::date - '15 day'::interval
        AND report_date &lt; now()::date 
      GROUP BY product_name, version_string
    ),
    totals as (
      SELECT
        SUM(report_count) AS total_count
      FROM crashes
    )
    SELECT category
      , version_string
      , report_count
      , round((report_count * 100::numeric)/total_count,3)::TEXT
    as percentage
    FROM crashes CROSS JOIN totals
    ORDER BY report_count DESC;
    `</pre>

    What's the difference to Postgres between that and a `SUM()` plus a `CROSS JOIN`?

    Here's the [EXPLAIN](http://www.postgresql.org/docs/9.3/static/using-explain.html) output from this query, pared down to the relevant section:

    <pre>`   CTE totals
         -&gt;  WindowAgg  (cost=0.00..0.03 rows=1 width=72) (actual time=0.112..0.114 rows=3 loops=1)
               -&gt;  CTE Scan on crashes  (cost=0.00..0.02 rows=1 width=72) (actual time=0.097..0.100 rows=3 loops=1)
       -&gt;  CTE Scan on totals  (cost=0.00..0.04 rows=1 width=104) (actual time=0.121..0.129 rows=3 loops=1)
    `</pre>

    The important bit to have a look at is **WindowAgg** right after **CTE totals**.

    Now compare to the EXPLAIN output from a `SUM()` plus a `CROSS JOIN` query:

    <pre>`   CTE totals
         -&gt;  Aggregate  (cost=0.02..0.03 rows=1 width=8) (actual time=0.015..0.015 rows=1 loops=1)
               -&gt;  CTE Scan on crashes  (cost=0.00..0.02 rows=1 width=8) (actual time=0.001..0.004 rows=3 loops=1)
       -&gt;  Nested Loop  (cost=0.00..0.07 rows=1 width=104) (actual time=0.191..0.205 rows=3 loops=1)
             -&gt;  CTE Scan on crashes  (cost=0.00..0.02 rows=1 width=72) (actual time=0.162..0.164 rows=3 loops=1)
             -&gt;  CTE Scan on totals  (cost=0.00..0.02 rows=1 width=32) (actual time=0.006..0.006 rows=1 loops=3)

You can see here that we now have an **Aggregate** (for the `SUM()`) plus a **Nested Loop** (for the `CROSS JOIN`). This example query only has three results returned, but our more typical queries involve 10k or more rows returned.

Avoiding the Aggregate and Nested Loop will save us lots of memory and processing time on every run of a very expensive query.
