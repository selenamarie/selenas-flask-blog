title: "Using JSON data type in production with Socorro"
id: 4888
date: 2013-08-06 06:19:38
tags: 
categories: 
- postgresql

Back in June, we started using the JSON datatype in production for Mozilla's [Socorro](http://github.com/mozilla/socorro). Our implementation analyzes crashes from Firefox and other Mozilla products, configured with a HBase backend and Postgres version 9.2 processing and serving reports to middleware and a Django front-end.

The guts of the application that stores raw data into Postgres is implemented in a [crashstorage class](https://github.com/mozilla/socorro/blob/master/socorro/external/postgresql/crashstorage.py#L106), and an example of how we use this field in report generation is in a [stored procedure for rolling up our "Top Crashers By Signature" reports](https://github.com/mozilla/socorro/blob/master/socorro/external/postgresql/raw_sql/procs/update_tcbs.sql#L40).

The idea is to get the metadata we store for each crash into Postgres in its raw JSON form available to SQL queries. We are currently still storing core crash report data in a normalized table (extracted from the original JSON). We are considering re-writing everything to just use a JSON column at the core. There may be some significant negative performance impacts, so more testing is needed before we move forward.

Previously, we only stored metadata in HBase. While it is convenient to have a year's worth of data in HBase for running arbitrary queries against, once we settle on reports, it is far faster and more convenient to be able to use Postgres with JSON functions and SQL to rollup aggregates. I'm sure this isn't true for everyone. We're working with large, but manageable data sets - around 30 GB per week of JSON, and only 2-3 weeks of data at a time.

The advantage to having the JSON in Postgres is that we **no longer are adding columns to our base tables**. It's not terribly difficult to add columns, but it requires some special work to make the database schema migrations as low-lock as possible on tables with weekly partitions. Cutting out the DBA as an intermediary before developers can deploy new features and reports is a huge win for automation and sustainability of the application.

My preference is that developers never _require_ a DBA to be present when deploying an app -- even when there are schema changes. There are lots of features in Postgres that significantly reduce the need for DBA involvement -- streaming replication, `pg_basebackup`, zero downtime column `ADD`, `DROP` and `ALTER`, transactional DDL and `CREATE INDEX CONCURRENTLY` to name a few. We're not quite there for Socorro, but my plan is to get there.

The ideal role of the Postgres DBA is more to write database code, monitor and improve performance. That kind of role feels a lot more like a partner to developers, rather than a separate, mysterious entity. In much the same way that DevOps and configuration management enable great cooperation between IT and developers, many of Postgres' maintenance features enable greater cooperation and less friction between DBAs and developers deploying new features.

There are still a few configuration and initialization issues to work through before Postgres can be seen as completely past it's reputation as a difficult to deploy database. Some of that can be solved with more widely used configuration recipes for tools like Puppet and Chef. My colleagues in IT have been working on a Puppet module that they plan to release that automatically sets up a master database and as many replicas as you'd like to configure.

My hope is that people more widely share their automation stories and code!

In anycase, the JSON datatype is solving an important problem for our team, and significantly reducing the demand for schema changes. I'd love to hear more reports from users trying out JSON the field.
