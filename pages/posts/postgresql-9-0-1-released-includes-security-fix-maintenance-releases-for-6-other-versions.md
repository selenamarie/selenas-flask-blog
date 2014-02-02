title: "PostgreSQL 9.0.1 released, includes security fix & maintenance releases for 6 other versions"
slug: postgresql-9-0-1-released-includes-security-fix-maintenance-releases-for-6-other-versions
id: 2096
date: 2010-10-05 09:44:40
tags: 
- postgres
- postgresql
- release
- security announcement
categories: 
- postgres
- postgresql

The PostgreSQL Global Development group [released new maintenance versions today](http://www.postgresql.org/about/news.1244):  9.0.1, 8.4.5, 8.3.12, 8.2.18, 8.1.22, 8.0.26 and 7.4.30\. This is the final update for PostgreSQL versions 7.4 and 8.0\. There's a security issue in there involving procedural languages, and a [detailed description of the vulnerability](http://wiki.postgresql.org/wiki/20101005securityrelease) is on our [wiki](http://wiki.postgresql.org/). A key thing to remember is that the issue primarily affects people who use SECURITY DEFINER along with a procedural language function. PL/PgSQL is not affected, but any other procedural language with a "trusted" mode is. This includes PL/Perl, PL/tcl, PL/Python (7.4 or earlier) and others.  The new versions fix issues in PL/Perl and PL/tcl.  A patch for PL/PHP is currently in the works.

Most developers feel that the security issue is relatively obscure. If you aren't using a procedural language with some mechanism for altering privileges (SET ROLE or SECURITY DEFINER, for example), you aren't vulnerable to the security issue and can upgrade Postgres during your next regularly scheduled downtime. If you *are* vulnerable, we recommend investigating the use of the functions that may be vulnerable, and taking steps to prevent their exploitation by upgrading as soon as you can.

[From the FAQ](http://wiki.postgresql.org/wiki/20101005securityrelease): 

> What is the level of risk associated with this exploit?> 
> 
> Low. It requires all of the following:> 
> 
> *   An attacker must have an authenticated connection to the database server.> 
> 
> *   The attacker must be able to execute arbitrary statements over that connection.> 
> 
> *   The attacker must have an strong knowledge of PostgreSQL.> 
> 
> *   Your application must include procedures or functions in an external procedural language.> 
> 
> *   These functions and procedures must be executed by users with greater privileges than the attacker, using SECURITY DEFINER or SET ROLE, and using the same connection as the attacker.

This was also the first release for which I generated release notes! :D

Here was my list of interesting changes for the announcement: 

*   Prevent show_session_authorization() from crashing within autovacuum processes, backpatched to all supported versions;
*   Fix connection leak after duplicate connection name errors, fix handling of connection names longer than 62 bytes and improve contrib/dblink's handling of tables containing dropped columns, backpatched to all supported versions;
*   Defend against functions returning setof record where not all the returned rows are actually of the same rowtype, backpatched to 8.0;
*   Fix possible duplicate scans of UNION ALL member relations, backpatched to 8.2;
*   Reduce PANIC to ERROR on infrequent btree failure cases, backpatched to 8.2;
*   Add hstore(text, text) function to contrib/hstore, to support migration away from the => operator, which was deprecated in 9.0\. Function support backpatched to 8.2;
*   Treat exit code 128 as non-fatal on Win32, backpatched to 8.2;
*   Fix failure to mark cached plans as transient, causing CREATE INDEX CONCURRENTLY to not be used right away, backpatched to 8.3;
*   Fix evaluation of inner side of an outer join is a sub-select with non-strict expressions in its output list, backpatched to 8.4;
*   Allow full SSL certificate verification to succeed in the case where both host and hostaddr are specified, backpatched to 8.4;
*   Improve parallel restore's ability to cope with selective restore (-L option), backpatched to 8.4 with caveats;
*   Fix failure of "ALTER TABLE t ADD COLUMN c serial" when done by non-owner, 9.0 only.
*   Several bugfixes for join removal, 9.0 only.

If you have a look at a new tool that Robert Haas and Tom Lane commited to the repo called [git_changelog](http://git.postgresql.org/gitweb?p=postgresql.git;a=blob;f=src/tools/git_changelog;h=af76f6d0ccbf550a75db84d4348dca68f0fa699b;hb=HEAD), you can use it to find the commit IDs for the various features (you need the whole source tree to do it :)).  

You'll find that there are a lot of commits in these sets. We haven't had a minor release since May 2010, so they kind of added up.

Any other changes in there you think we should have mentioned in the announcement? Let me know in the comments.

Download new versions now:

*   [Main download page](http://postgresql.org/download)
*   [Source code](http://postgresql.org//ftp/source/)
*   [Binary packages](http://postgresql.org//ftp/binary/)
*   [One-click installer, including Mac and Windows packages](http://www.enterprisedb.com/products/pgdownload.do)
