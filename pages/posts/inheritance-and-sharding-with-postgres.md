title: "Inheritance and sharding with Postgres"
slug: inheritance-and-sharding-with-postgres
id: 3757
date: 2012-03-14 08:34:03
tags: 
- devops
- inheritance
- postgres
- postgresql
- sharding
categories: 
- postgres
- postgresql

A friend told me about their [sharding](http://en.wikipedia.org/wiki/Shard_(database_architecture)) scheme last night, and it made me very curious about how others are handling this problem. This question about database design turns into a devops issue, so it's something really the entire development group and devops and DBAs need to be aware of and concerned about. And it's not a problem exclusive to Postgres.
<!--more-->
They're using [Postgres' table inheritance](http://www.postgresql.org/docs/current/static/ddl-inherit.html) to constrain the properties of the sharded tables. And I'm deliberately using 'sharding' because this ends up being a functional grouping, rather than, say, [partitioning by date](http://www.postgresql.org/docs/9.1/static/ddl-partitioning.html). Groups of customers live on each shard, and can be moved around.

In theory, this is awesome. Everything inherited is in lockstep, you never have to worry about one shard's tables being different from any other shard. 

But that's dubious, because you can change or add columns to child tables. The only columns that are constrained are the ones defined by the parent.

And... the problems I've seen with this setup are when you need to make a schema change on a column that's in a parent table. Typically, devs (and sometimes DBAs) give up, and just add columns to each shard's table individually. Because they can't get the downtime they need to modify the tables across all shards.

In this case, we're talking about 1024 tables for each sharded table, and an [ACCESS EXCLUSIVE lock](http://www.postgresql.org/docs/current/static/explicit-locking.html) needs to be acquired on them all before the change can be applied. 

There are some simple things one can do to get around this, but acquiring that lock is a significant undertaking on a busy system. In one case, the table being modified is an audit table. (why this is problematic, exercise for reader, etc) 

And I still have scars from working on a system that had 100k+ inherited tables.

So, my thought was: **just don't use inheritance for sharded designs**. For schema changes, not using inheritance gets you: 

*   Only one ACCESS EXCLUSIVE lock required at a time
*   The ability to apply a change per-shard, instead of globally
*   Preparation for the day when you move a shard to a separate system entirely

If you're using 9.0 or later, you can use [CREATE TABLE ... LIKE](http://www.postgresql.org/docs/9.1/static/sql-createtable.html) instead of using INHERITS, if you're deploying shards with SQL commands. 

Giving up inheritance is a pain because: 

*   Now you have to ensure that your tables remain in sync across shards without inheritance's help (but again, dubious help!)
*   You can no longer write queries against the parent table that will pull data from all child tables (but I'd say - that's for your data warehouse, not your prod OLTP database)
*   You're no longer using inheritance, which is a pretty cool feature

I'd really like to know what others are doing.  Tell me in the comments.

**Some links you might be interested in**

And relevant, but doesn't mention  but about 5 months old: [Instagram's sharding technique](http://instagram-engineering.tumblr.com/post/10853187575/sharding-ids-at-instagram) 

[Sharding for startups](http://www.startuplessonslearned.com/2009/01/sharding-for-startups.html)

[Scalability Strategies Primer: Database Sharding](http://blog.maxindelicato.com/2008/12/scalability-strategies-primer-database-sharding.html)
