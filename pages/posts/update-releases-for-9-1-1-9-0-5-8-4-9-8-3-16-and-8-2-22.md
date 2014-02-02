title: "Update releases for 9.1.1, 9.0.5, 8.4.9, 8.3.16 and 8.2.22"
slug: update-releases-for-9-1-1-9-0-5-8-4-9-8-3-16-and-8-2-22
id: 3372
date: 2011-09-26 08:30:02
tags: 
- 8.2.22
- 8.3.16
- 8.4.9
- 9.0.5
- 9.1.1
- postgres
- postgresql
- update release
categories: 
- postgres
- postgresql

Today the Global PostgreSQL Development Group released branch updates for all supported versions. You can go ahead and [download them now](http://postgresql.org/download)!

There were quite a few fixes for somewhat obscure crashes, fixes for memory leaks discovered by some valgrind testing, and a couple big fixes for GiST indexes, like this: 

> * [Fix memory leak at end of a GiST index scan](http://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=0a6cc28500b7a8db7a27cbd0d75e18837fb2e367)> 
> 
>     gistendscan() forgot to free so->giststate.> 
> 
>     This oversight led to a massive memory leak --- upwards of 10KB per tuple> 
>     --- during creation-time verification of an exclusion constraint based on a> 
>     GIST index.  In most other scenarios it'd just be a leak of 10KB that would> 
>     be recovered at end of query, so not too significant; though perhaps the> 
>     leak would be noticeable in a situation where a GIST index was being used> 
>     in a nestloop inner indexscan.  In any case, it's a real leak of long> 
>     standing, so patch all supported branches.  Per report from Harald Fuchs. 

There were a few fixes for catalog or catalog index corruption, and avoidance of buffer overflows which could cause a backend crash. There were also a few fixes that will improve the performance of VACUUM over time.

Release notes have all the details. Many of the fixes have already been committed to 9.1 (there are only 11 new commits in 9.1.1). So, you're about to experience a great many bugfixes, users of 8.2->9.0\. 

Another thing to note - 8.2 will be deprecated in 2011! You ought to upgrade anyway, just to get HOT and to get yourself into a position to use pg_upgrade for future upgrades. But now, you've got extra incentive.
