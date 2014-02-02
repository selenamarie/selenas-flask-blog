title: "PgCon Day 1 - Cluster summit and catching up with folks"
slug: pgcon-day-1-cluster-summit-and-catching-up-with-folks
id: 3004
date: 2011-05-18 04:28:29
tags: 
- pgcon2011
- postgres
- postgresql
categories: 
- postgres
- postgresql

Yesterday, I spent my morning at the [Clustering summit](http://wiki.postgresql.org/wiki/PgCon2011CanadaClusterSummit), catching up on what the cluster hackers have been up to for the last year. I was lucky enough to sit next to Jan Wieck and Kevin Grittner. You may remember Kevin from [his work on serializable snapshot isolation](http://wiki.postgresql.org/wiki/SSI).

There were some pretty awesome side conversations about where folks think work needs to be done next, and [conflict resolution for multi- (or many-) master setups](https://twitter.com/#!/selenamarie/status/70509515493220353). 

I gave a quick update on [Bucardo 5, which had an alpha release last week](https://mail.endcrypt.com/pipermail/bucardo-general/2011-May/001000.html), supports many-master and has has experimental support for non-Postgres targets. The first two targets are text and MongoDB.

The Postgres project has given the generic name "binary replication" to all the features like WAL shipping, streaming replication and synchronous replication.  Simon Riggs also gave his update on these features at the [Clustering Summit](http://wiki.postgresql.org/wiki/PgCon2011CanadaClusterSummit) today.  He observed that the 9.1 release is the culmination of 7 years of work on replication subsystems. Simon pointed out that synchronous replication is the best, and most obvious, use case for the binary replication at the core of Postgres. And also pointed out that he was quite pleased with the ultimate design.

For the afternoon, I spent some time with folks on the infrastructure team, giving [Magnus](http://blog.hagander.net) well-deserved congratulations for his induction into -core, and meeting up with folks from all over at the Royal Oak and Keg, a reasonable steakhouse in town.

Looking forward to the developers meeting today!
