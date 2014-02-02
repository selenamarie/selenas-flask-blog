title: "Catalog SQL Friday: using DO when we've got tables as variables"
slug: catalog-sql-friday-using-do-when-weve-got-tables-as-variables
id: 4963
date: 2013-08-16 11:46:46
tags: 
categories: 
- postgresql

Just a quick note about modifying constraints:

There's no such thing as `ALTER CONSTRAINT`. So, if you want to safely change a `CHECK` constraint, like on a partition, you need to `DROP` and `ADD` it in a single transaction.

Below is a snippet for finding partitions, their CHECK constraints based on a `WHERE` clause. Then we `DROP` the existing constraint and add back the correct constraint. It doesn't take much sleuthing to figure out what the problem was. :)

     DO $$
      DECLARE myrecord record;
      DECLARE theweek text;
      BEGIN
        FOR myrecord IN SELECT relname, conname from pg_constraint
          JOIN pg_class ON pg_constraint.conrelid = pg_class.oid
          WHERE consrc ~ 'without' and split_part(relname, '_201', 1)
          IN (select table_name from report_partition_info
          WHERE partition_column = 'date_processed') LIMIT 1
        LOOP
           EXECUTE 'ALTER TABLE ' || quote_ident(myrecord.relname)
           || ' DROP CONSTRAINT IF EXISTS '
           || quote_ident(myrecord.conname) || ';';&lt;/p&gt;

       theweek = substring(myrecord.relname from '........$');

       EXECUTE 'ALTER TABLE ' || quote_ident(myrecord.relname)
       || ' ADD CONSTRAINT ' || quote_ident(myrecord.conname)
       || ' CHECK ((date_processed &gt;= timestamptz('
       || quote_literal(to_char(date(theweek), 'YYYY-MM-DD')) || '))'
       || ' AND (date_processed &lt; timestamptz('
       || quote_literal(to_char(date(theweek) + 7, 'YYYY-MM-DD'))
       || ')));';

       RAISE NOTICE 'DONE: %', myrecord.relname;
    END LOOP;

    END$$; 

Here's the [gist version for easier reading](https://gist.github.com/selenamarie/fc4588ff594576f86982).

The couple things I learned in this process was a nice feature in `substring()` allowing me to return the date portion of my partition names easily, and `split_part()` which allowed me to return the parent table name and compare it to my list of partitionable tables for the specific partition column. I recently added support for partitioning on a different column for certain tables, so I have to differentiate for this fix. The [string function docs](http://www.postgresql.org/docs/9.2/static/functions-string.html) are pretty great.

I didn't do any optimization of this -- just got it working and am now testing it in our stage environment. The final script is going to perform the changes on a month's worth of partitions at a time to help reduce the chance of deadlocking.

If you have thoughts on how I could have done this more efficiently, let me know in the comments!
