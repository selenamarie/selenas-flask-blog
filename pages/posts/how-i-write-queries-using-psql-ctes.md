title: "Everyday Postgres: How I write queries using psql: Common Table Expressions"
slug: how-i-write-queries-using-psql-ctes
id: 5068
date: 2013-11-12 08:46:34
tags: 
- ctes
- everyday postgres
categories: 
- postgresql

This this series of posts about using Postgres every day. The last post was about [`\` commands in psql](http://www.chesnok.com/daily/2013/11/06/top-10-psql-commands-i-use/).

I'm now going to share in a series of posts my workflow for writing queries, and some of the things about working with Postgres that I take for granted in writing queries.

## Shortcuts I can't live without

Three important shortcuts you should learn are:

*   `\e`: Pulls the last query you executed into a buffer in your favorite editor*   `\df+ [function]`: This displays `[function]` information, and the `+` dumps the function itself to STDOUT
*   `\ef [function]`: This pulls `[function]` into a buffer in your favorite editor. This is the most convenient way to grab a copy of an individual function for me.
*   `\ef`: This opens your favorite editor and puts a template for a function (in any supported procedural language) in a buffer

I'll talk about writing functions in a future post.

## Thinking in CTEs

In searching through my recent `psql` history, I found quite a few `WITH` queries. These are [Common Table Expressions](http://www.postgresql.org/docs/current/static/queries-with.html), a useful feature supported by many databases that allows you to embed subqueries in your SQL in a very readable format. CTEs have a lot more interesting features and properties, like `RECURSIVE`.

However, I tend to just use CTEs as a more convenient form of a **subquery**. This allows me to break apart long queries into smaller, testable chunks. I usually will write a subquery so that it's in my command history, generate some fake data for testing, and go back to that query in my history to test edge cases.

I iterate on the smaller tables until I have a set of understandable "paragraphs" of SQL. This makes it easier for me to explain the logic of the query with others, and makes testing each piece easier in the event that something breaks. Usually, when a CTE breaks, I've made an assumption about incoming data that's incorrect.

The composability of SQL is often terrible. CTEs help break apart the complexity visually. There's some warnings about CTEs not performing well under certain circumstances. My approach is to design with CTEs and optimize for performance only if needed.

## Other advantages of CTEs

In case you're not yet convinced CTEs are worth learning, I made a bullet list of advantages from some useful comments about how others are using CTEs:

*   Alternative to throwaway VIEWs and temporary tables when querying replicas ([comment from bma](http://www.chesnok.com/daily/2013/11/12/how-i-write-queries-using-psql-ctes/comment-page-1/#comment-1121281986))
*   [Variable declaration](http://www.chesnok.com/daily/2013/11/12/how-i-write-queries-using-psql-ctes/comment-page-1/#comment-1120950143) - to emulate DECLARE in SQL Server, for example
*   Easier to understand queries and faster development time (ME)

## An example of the kinds of queries I write

Something you'd see a lot in my command history are queries that look like this:

    WITH crashes AS (                                                               
        SELECT uptime_string AS category                                                      
            , sum(report_count) AS report_count                                     
        FROM signature_summary_uptime                                               
            JOIN signatures USING (signature_id)                                       
        WHERE                                                                           
            signatures.signature = 'Fake Signature #1'                                             
            AND report_date &gt;= '2013-08-05T00:00:00+00:00'::timestamptz             
            AND report_date &lt; '2013-08-12T00:00:00+00:00'::timestamptz              
            AND product_name IN ('Firefox')  AND version_string IN ('1')            
        GROUP BY category                                                           
    ),                                                                              
    totals AS (                                                                     
        SELECT                                                                      
            category                                                                
            , report_count                                                          
            , sum(report_count) OVER () as total_count                              
        FROM crashes                                                                
    )                                                                               
    SELECT category                                                                 
        , report_count                                                              
        , round((report_count * 100::numeric)/total_count,3)::TEXT                  
    as percentage                                                                   
    FROM totals                                                                     
    ORDER BY report_count DESC                                                      
    ;

You'll see that I have one or more `WITH` clauses, and then a query that performs a final summary query using the data from the CTEs.

This query probably was asked for something like this:

> Please provide counts of crashes with the same uptime, for Firefox version 1, and the signature 'Fake Signature #1' for the last week, including a percentage of all of the sampled crashes.

While I'm sure there are better ways to write the query above, I wanted to show how I have made a pattern for myself to speed up query writing. I'm not always interested in the best possible query. Hopefully, the Postgres planner makes up for many of my sins as a developer!

What I am interested in is finding answers to problems quickly for my coworkers.

In answering the question I was asked, I first dig out an appropriate summary table (we have quite a few in Socorro). I found the `signature_summary_uptime` table, and fortunately it has `product_name` and `version_string` available in the table. I only need to join `signatures` to fulfill the request. (Yay for denormalized data that supports the kinds of queries we often run!)

Next, I see that I'm being asked for a **total percentage**, so I need to calculate a sum across all the rows that I retrieve. That can be very slow, so I create a second CTE that uses data from the first CTE (rather than doing two full table scans to calculate the total). I use a [window function](http://www.postgresql.org/docs/9.3/static/functions-window.html) instead of `SUM()` here because I've [done experiments to see which tends to be faster](http://www.chesnok.com/daily/2013/08/05/why-use-over-instead-of-a-cross-join/).

And, finally once I have all the data together, I run my final query using my two CTE tables.

## How CTEs and breaking down this process have helped me

So, I've had about a year to practice. A query like this today takes me 10-15 minutes to assemble and test. They are typically slightly more complex -- with more dependencies, and maybe 2-3 more tables involved in JOINs. But they follow the same basic pattern.

Most queries on my data sets conform to recognizable patterns.

After a few months, we recognized that moving JSON for crash data into Postgres also would be a win, and was easy to process using very similar queries.

That's all helped make finding answers about [Firefox crashes](http://crash-stats.mozilla.com) easier and faster!
