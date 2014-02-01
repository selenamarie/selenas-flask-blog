title: "High availability and Postgres"
id: 3318
date: 2011-08-17 15:52:08
tags: 
- dba
- devops
- ha
- high availability
- operations
- postgres
- postgresql
- sysadmin
categories: 
- postgres
- postgresql

A friend contacted me today, asking me "What are the best practices for failover with Postgres?"  And he mentioned pgpool-II.

He was interested in 9.0, since 9.1 hasn't been released yet. (but, it's looking like we're [gearing up for a September release](https://twitter.com/net_snow/status/103949707700731905)!)
<!--more-->
My off-the-cuff response was: 

> There isn't a single solution, although [pgpool-II](http://pgpool.projects.postgresql.org/) is a common one.> 
> 
> pgpool-II is what I've used in AWS. I've also seen people use heartbeat (I guess [pacemaker](http://linux-ha.org/wiki/Pacemaker) now?). I think either works fine. The frustrating bit is that we don't have the ability to refresh the failed system easily. > 
> 
> There's also repmgr: [https://github.com/greg2ndQuadrant/repmgr](https://github.com/greg2ndQuadrant/repmgr)> 
> 
> It's new, but might be worth exploring.

I started an [High Availability](http://wiki.postgresql.org/wiki/High_Availability) page on the PostgreSQL wiki.  We really need a canonical source of information for this. Devs are struggling to figure it out [from our docs](http://www.postgresql.org/docs/current/static/high-availability.html).

What are you doing for HA and Postgres?
