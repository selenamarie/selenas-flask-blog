title: "psql and file, CSV exports"
id: 159
date: 2007-10-13 16:53:20
tags: 
- postgres
categories: 
- postgres
- postgresql
- sysadmin

Gabrielle and I met to talk about some projects today. She brought up a couple questions that were raised about differences between MySQL and PostgreSQL syntax for data export. 
<!--more-->
She showed me `\pset fieldsep` and `\pset format` for controlling interactive output from `SELECTS` (see [psql documentation](http://www.postgresql.org/docs/current/static/app-psql.html)).  You might say: `\pset fieldsep ,` (although that wouldn't be CSV.. but it's quick and dirty). And `\pset format` offers `unaligned, aligned, html, latex, or troff-ms`. There are several shortcuts available - `\a` for aligned/unaligned. A combination of `\pset fieldsep` and `\a` gets you nearly to CSV.

Then we took a look at the [COPY](http://www.postgresql.org/docs/8.2/static/sql-copy.html) command and our options there. That's when we discovered this: 

> `> 
> COPY { tablename [ ( column [, ...] ) ] | ( <font color="red">query</font> ) }> 
>     TO { 'filename' | STDOUT }> 
> ` 

See that <font color="red">query</font>?  Yeah, super sweet. This feature was new in version 8.2\. ([8.3 beta](http://www.postgresql.org/developer/beta) is out now!)
 Now you can run a command like: 

> `> 
> COPY (SELECT param1, param2, param3 from myview) TO STDOUT WITH CSV; > 
> `

Or you can replace STDOUT with a file path. `\copy` supports the same syntax. This is a reasonable alternative to MySQL's `SELECT INTO OUTFILE`. And the feature has been there for at least a year.
