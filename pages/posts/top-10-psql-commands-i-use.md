title: "Everyday Postgres: Top 10 psql \"\\\" commands I use"
slug: top-10-psql-commands-i-use
id: 5058
date: 2013-11-06 15:39:02
tags: 
- everyday postgres
categories: 
- postgresql

I have been thinking about the kinds of questions people have about Postgres if they're mostly users of MySQL. One thing that comes up a lot is how to use the [psql](http://www.pgcon.org/2009/schedule/attachments/116_Power_psql.ppt) command-line.

I'm going to do a series of posts based on what I actually do every day with Postgres. This isn't going to be an exhaustive look at all the features, but just the kinds of things I find useful.

Here's a look at the kinds of commands I regularly use on a production system:

    selena@wuzetian:~ #1642 15:13: awk '{print $1}' /tmp/cmds   | uniq -c | sort -n -r
         47 \e
         22 \d
         13 \x
         12 \df+
         10 \q
          9 \df
          6 \ef
          6 \d+
          5 \o
          5 \h
    `</pre>

    Here's the kinds of commands I use on my local system:

    <pre>`selena@wuzetian:~ #1645 15:15: awk '{print $1}' /tmp/local_cmds  | uniq -c | sort -n -r
         89 \d
         43 \e
         28 \df+
         14 \x
         14 \d+
         13 \df
         11 \c
         10 \h
          4 \a
          3 \ef+

There's not a whole lot of difference between the two. I pretty clearly use the database locally to look at schema definitions over and over again!

Here's what each of these commands do:

*   `\d+`: Examine a table, by default in 9.2 prints the table name, followed by the columns, their types, keys, indexes and constraints. The plus will cause all child tables that inherit from a parent to be listed.
*   `\e`: Opens an editor defined by your EDITOR environment variable, and put the most recent command entered in `psql` into the buffer. You can define a non-command line editor here!
*   `\df+`: Prints information about a User Defined Function, including the function's whole definition (that's what the `+` does), best when combined with `\x` and probably `\a` as well
*   `\q`: Quits `psql`. You can also quit with `^D`
*   `\ef [function]`: Opens up your editor, and puts the function into the buffer. Without a function, it provides a convenient template for creating a new function.
*   `\o [filename]`: Open a local file for writing the output of whatever commands you run next. Stop writing to the file with another `\o`
*   `\h`: Help for SQL commands
*   `\c [databasename]`: Connect to [databasename] on local database cluster
*   `\a`: Print output "unaligned", or without adding whitespace to make columns align. Good when trying to print machine-readable output to the terminal.
*   `\x`: Print output "expanded". This causes output to be printed out like: "Column: Value", rather than the normal tabular/spreadsheet style. Useful in lots of contexts, especially when you've got some columns that have a very large text field.

And here's a few useful commands that didn't make the top 10 lists:

*   `\?`: Help for `\` commands*   `\timing`: Turn timing of all commands on, reports in ms.
*   `\s`: print out your `psql` history to STDOUT.
*   `\i [filename]`: execute the contents of [filename]
*   `\! [command]`: execute a command in the local shell

Finally, when you start up psql, you have a few options. My favorite combination when generating machine-readable output is to add `-AX -qt` (axe cutie! hat tip to [Greg Sabino Mullane](http://www.gtsm.com/) for that mneumonic). Another very useful psql extension is `-e`, which causes the SQL commands used to produce output to _also_ be printed out. This will help you learn about `information_schema` items and all the internal tables used to provide system information.

The shortcuts really worth spending a bit of time exploring are `\e*` and `\d*`. Both provide quite a bit of useful functionality, with relatively easy to remember letter combinations.
