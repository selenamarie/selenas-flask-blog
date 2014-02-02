title: "Security and maintenance release for PostgreSQL: versions 9.1.3, 9.0.7, 8.4.11 and 8.3.18"
slug: security-and-maintenance-release-for-postgresql-versions-9-1-3-9-0-7-8-4-11-and-8-3-18
id: 3740
date: 2012-02-27 08:06:44
tags: 
- 8.3.18
- 8.4.11
- 9.0.7
- 9.1.3
- postgres
- postgresql
- release
categories: 
- postgres
- postgresql

Today, PostgreSQL Global Development Group [released new versions](http://www.postgresql.org/about/news/1377/ "PostgreSQL Security Release Announcement") of all active branches. This includes three security bugfixes, two of which are pretty obscure and one that fixes a possible security issue with restoring un-sanitized output from pg_dump. Details about the security issues are included in the [release announcement](http://www.postgresql.org/about/news/1377/ "PostgreSQL Security Release Announcement"). 
<!--more-->
Some other bug and performance fixes in this minor release include: 

*   Fix btree index corruption from insertions concurrent with vacuuming
*   Avoid crashing when we have problems deleting table files post-commit
*   Fix recently-introduced memory leak in processing of inet/cidr
*   Fix postmaster to attempt restart after a hot-standby crash

[Upgrade](http://www.postgresql.org/download/ "PostgreSQL Download Page") as soon as you can!
