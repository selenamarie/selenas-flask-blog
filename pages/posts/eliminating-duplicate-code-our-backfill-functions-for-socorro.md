title: "Eliminating duplicate code: our backfill functions for Socorro"
slug: eliminating-duplicate-code-our-backfill-functions-for-socorro
id: 5051
date: 2013-11-05 07:37:31
tags: 
- everyday postgres
categories: 
- postgresql

Last Friday, I spent some time refactoring a user defined function in [Socorro](http://github.com/mozilla/socorro) that was taking a little too long to run each day.

This meant splitting up one function into about 8 separate functions. Our functions are designed to backfill themselves when a failure occurs. However, if we need to remove an incorrect daily report and re-run the functions from scratch, we've typically written a special function for every report called `backfill_REPORTNAME` that handles the cleanup work.

This means we've got a lot of boilerplate code, that it would really be nice to replace. So, I took this opportunity to create a utility function and hopefully never have to write another `backfill_REPORTNAME` function again!

Here it is:

    CREATE OR REPLACE FUNCTION backfill_named_table(tablename text, updateday date) 
        RETURNS boolean
        LANGUAGE plpgsql
    AS $function$
    DECLARE
        update_proc_name TEXT := 'update_' || tablename;
    BEGIN

    -- Check if requested table for backfilling exists
    PERFORM 1 FROM information_schema.tables WHERE table_name=tablename;
    IF NOT FOUND THEN
        RAISE INFO 'table: % not found', tablename;
        RETURN FALSE;
    END IF;

    -- Check that requested function for update exists
    PERFORM 1 FROM pg_proc WHERE proname = update_proc_name;
    IF NOT FOUND THEN
        RAISE INFO 'proc: % not found', update_proc_name;
        RETURN FALSE;
    END IF;

    EXECUTE format('DELETE FROM %I WHERE report_date = %L', tablename, updateday);

    EXECUTE format('SELECT %I(%L, FALSE)', update_proc_name, updateday);

    RETURN TRUE;

    END;
    $function$
    ;

Here's [the file with the code](https://github.com/selenamarie/socorro/blob/5c7d59e531d308d4cebbae51d3458176e2a03e63/socorro/external/postgresql/raw_sql/procs/backfill_named_table.sql).

I've been trying to switch over to using [format()](http://www.postgresql.org/docs/current/static/functions-string.html#FUNCTIONS-STRING-FORMAT) instead of `||` in my queries, because it tends to be much more readable.

You'll see that I've got a check for the existence of the table, and that the user defined function for the update exists. The type checking in the function handles ensuring that `updateday` is a valid date. If you think there's any improvements I could make on this, definitely let me know in the comments.
