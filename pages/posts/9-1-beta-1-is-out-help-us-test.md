title: "9.1 beta 1 is out! Help us test."
slug: 9-1-beta-1-is-out-help-us-test
id: 2948
date: 2011-05-02 08:27:23
tags: 
- 9.1
- beta1
- postgres
- postgresql
categories: 
- postgres
- postgresql

Postgres [released version 9.1 beta 1](http://www.postgresql.org/about/news.1313) today!  This is a preview of 9.1, predicted to be available in the next 2-3 months, not a bugfix release for earlier versions of Postgres.

> PostgreSQL 9.1 contains a huge volume of new features, possibly more any single release of PostgreSQL before. These features also include several innovations which PostgreSQL is the first database system to have. The most anticipated features in this version include:> 
> 
> *   Synchronous Replication
> *   Per-column collations for multilingual databases
> *   Unlogged Fast Tables
> *   K-Nearest-Neighbor Indexing
> *   Serializable Snapshot Isolation
> *   Writeable Common Table Expressions
> *   SE-Linux Integration
> *   Extensions
> *   SQL/MED attached tables> 
> 
> The PostgreSQL project now depends on you to test 9.1beta1 in order have a rapid and bug-free 9.1 release. If you are able to help with testing version 9.1, please see the [Beta Testing HOWTO](http://wiki.postgresql.org/wiki/HowToBetaTest)

[Binary downloads](http://www.postgresql.org/download/) are available, as is the [source](http://www.postgresql.org/ftp/source/).

If you'd like to grab a copy of the latest from git, here is a quick set of instructions to compile 9.1beta1 from the git repo: 

<pre>

git checkout REL9_1_BETA1
./configure --prefix=/opt/pg9.1beta1
make
sudo make install
</pre>

And then to create a database: 

<pre>
/opt/pg9.1beta1/bin/initdb -D mytestdb
/opt/pg9.1beta1/bin/pg_ctl -D mytestdb start
</pre>

For a preview of features coming this fall, [check out Depesz's blog](http://www.google.com/search?hl=en&q=waiting+for+9.1+site%3Awww.depesz.com).
