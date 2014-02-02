title: "Everyday Postgres: INSERT with SELECT"
slug: everyday-postgres-insert-with-select
id: 5090
date: 2013-11-19 08:04:50
tags: 
categories: 
- postgresql

_This is a continuation of a [series of posts about how I use Postgres everyday](http://www.chesnok.com/daily/tag/everyday-postgres/)._

One of the most pleasant aspects of working with Postgres is coming across features that save me lots of typing. Whenever I see repetitive SQL queries, I now tend to assume there is a feature available that will help me out.

One such feature is `INSERT` using a `SELECT`, and beyond that, using the output of a `SELECT` statement in place of `VALUES`.

Take for example:

    INSERT into foo_bar (foo_id, bar_id) VALUES ((select id from foo where name = 'selena'), (select id from bar where type = 'name'));    
    INSERT into foo_bar (foo_id, bar_id) VALUES ((select id from foo where name = 'funny'), (select id from bar where type = 'name'));
    INSERT into foo_bar (foo_id, bar_id) VALUES ((select id from foo where name = 'chip'), (select id from bar where type = 'name'));
    `</pre>

    I think a lot of people know that this is possible. There are a few problems with it - like if the result of the `WHERE` clause isn't unique in both cases, you'd get an error. In this case, `id` in both tables were surrogate keys, with both `name` and `type` being unique.

    What some people don't realize is that you can SELECT, and then directly insert that into a table:

    <pre>`INSERT into foo_bar (foo_id, bar_id) ( 
      SELECT foo.id, bar.id FROM foo CROSS JOIN bar 
        WHERE type = 'name' AND name IN ('selena', 'funny', 'chip') 
    );

If the values you wanted to take from the table `bar` were not all the same, the query would be considerably more complex. Given that I only am interested in a single value from `bar`, and I want it joined with a series of explicitly selected values from `foo`, this version of the query saves me a lot of typing.

The bigger picture, however, was pointed out in the comments by [Marko](http://www.chesnok.com/daily/2013/11/19/everyday-postgres-insert-with-select/#comment-1129753354):

> VALUES is just a special type of SELECT and that INSERT writes the
>   result of an arbitrary SELECT statement into the table. Consider:
> 
> SELECT 1; vs. VALUES (1);
> 
> SELECT * FROM (SELECT 1) sq; vs. SELECT * FROM (VALUES (1)) sq;
> 
> INSERT INTO quix VALUES (1); vs. INSERT INTO quix SELECT 1;
> 
> The reason VALUES is often used with INSERT is that many RDMBSs don't
>   support SELECT without a FROM clause, so using VALUES is more
>   convenient. It's also handy if you have a list of data you want to
>   SELECT, e.g. VALUES (..), (..), (..);

I may have referenced this feature a few times when breaking down functions used for reports in Socorro. It's super convenient and saves quite a bit of typing! You can put any valid SQL query in there, including [CTEs](http://www.chesnok.com/daily/2013/11/12/how-i-write-queries-using-psql-ctes/). The [documentation for INSERT](http://www.postgresql.org/docs/current/static/sql-insert.html) provides a few more examples.
