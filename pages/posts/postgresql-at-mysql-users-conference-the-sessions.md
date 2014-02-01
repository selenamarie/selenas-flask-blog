title: "PostgreSQL at MySQL Users Conference: the sessions!"
id: 2544
date: 2011-02-14 16:37:08
tags: 
- conference
- discount
- mysqlconf
- postgres
- postgresql
categories: 
- postgres
- postgresql

[![](http://www.chesnok.com/daily/wp-content/uploads/2010/10/mysqlconfbanner-300x48.png "mysqlconfbanner")](http://www.chesnok.com/daily/wp-content/uploads/2010/10/mysqlconfbanner.png)

You've probably seen a few posts about this - from [the CFP](http://www.chesnok.com/daily/2010/10/06/postgresql-at-mysql-users-conference-2011/), to [Baron's recent pointer](http://www.xaprb.com/blog/2010/12/19/schedule-for-mysql-and-beyond-conference-is-live/) to the release of the schedule. And now Josh Berkus [just posted a Meetup for the event](http://www.meetup.com/postgresql-1/events/16566207/?a=mc1_grp&rv=mc1), so that spurred me on for this post...

So, just to make things even easier for you, I thought I'd summarize the [awesome talks we're having at the O'Reilly MySQL Users Conference](http://en.oreilly.com/mysql2011/public/schedule/topic/PostgreSQL) this year related to PostgreSQL.

*   [Building Data Warehouses with PostgreSQL, Josh Berkus (PostgreSQL Experts, Inc.)](http://en.oreilly.com/mysql2011/public/schedule/detail/17133)
Has your database grown to hundreds of gigabytes in size, with no limit in sight? Are you considering moving to an expensive proprietary database system do deal with your huge database? PostgreSQL is an excellent database for small to medium sized data warehouses in the 0.5 to 5 terabyte range.*   [Bottom-up Database Benchmarking, Greg Smith (2ndQuadrant US)](http://en.oreilly.com/mysql2011/public/schedule/detail/17296)
While databases are increasingly being distributed across multiple nodes, the performance of every node still matters--especially if you're considering virtualized or cloud deployments that have their own specific trade-offs. Memory performance scaling as core count changes, all aspects of disk performance, and using sysbench to benchmark both MySQL and PostgreSQL are all topics covered here.*   [An Introduction to PostGIS - the PostgreSQL spatial extension, Ragi Burhum (Burhum LLC - GIS Consulting)](http://en.oreilly.com/mysql2011/public/schedule/detail/17529)
PostGIS is an extension to the PostgreSQL object-relational database system which allows GIS (Geographic Information Systems) objects to be stored in the database. It includes support for spatial indexes, and functions for analysis and processing of GIS objects.*   [Securing PostgreSQL From External Attack, Bruce Momjian (EnterpriseDB)](http://en.oreilly.com/mysql2011/public/schedule/detail/17544)
This talk explores the ways attackers with no authorized database access can steal Postgres passwords, see database queries and results, and even intercept database sessions and return false data. Postgres supports features to eliminate all of these threats, but administrators must understand the attack vulnerabilities to protect against them.*   [Introduction to PostgreSQL Configuration, Robert Haas (EnterpriseDB)](http://en.oreilly.com/mysql2011/public/schedule/detail/17342)
PostgreSQL is highly customizable, but which settings are most important and what values are most appropriate for a typical installation? This talk will explain the basics of how to configure PostgreSQL for reliability and good performance.*   [Mixed MySQL/PostgreSQL environments, Jeff Davis (Aster Data)](http://en.oreilly.com/mysql2011/public/schedule/detail/17466)
Mixed SQL system environments are a reality for most organizations. MySQL and PostgreSQL are a natural combination -- both are open source, and they complement each other nicely. See how to improve data consolidation, increase confidence in query results, and analyze data across applications.*   [Maintaining Terabytes: 10 Things to Watch Out For When PostgresSQL Bets Big, Selena Deckelmann (PostgreSQL)](http://en.oreilly.com/mysql2011/public/schedule/detail/17195)
Size can creep up on you. Some day you may wake up to a multi-terabyte Postgres system handling over 3000 tps staring you down. Learn the best ways to manage these systems as they grow, and find out what new features in 9.0 have made life easier for administrators and application developers working with big data.*   [Openstreetmap -> (PostGIS|MySQL|SpatiaLite) -> OpenLayers: From Map to Web, Hartmut Holzgraefe (...???...)](http://en.oreilly.com/mysql2011/public/schedule/detail/17383)
OpenStreetMap raw data for any non-trivial area comes as a massive amount of XML data. Processing that XML data directly is possible, importing it into into a spatial database provides for much more interesting processing options though, especially when it comes to producing on demand map data for web applications with acceptable performance.*   [War Stories and Solutions: Operational Fun with PostgreSQL and PostGIS in the Cloud, Andy Parsons (Obikosh.com)](http://en.oreilly.com/mysql2011/public/schedule/detail/17647)
As CTO of Outside.in, and in my new stealth company, I've seen my share of challenging scenarios keeping a very busy PostgreSQL-based startup online and responsive during tremendous growth. EC2 + PostgreSQL + PostGIS + no downtime. Others can probably learn from my battle scars!*   [Replace phpMyAdmin with Something Better, Jakub Vrana (Self-employed)](http://en.oreilly.com/mysql2011/public/schedule/detail/17157)
phpMyAdmin is a well-known PHP application for managing MySQL database. What's wrong with it? It is big, slow and it misses support for many advanced features like stored procedures or triggers. Its free alternative Adminer provides user-friendly interface, requires no setup, is lightning fast and highly customizable. Adminer is available for MySQL, PostgreSQL, SQLite, MS SQL and Oracle.

We're also having a Birds of a Feather session, and staffing a booth on the exhibit floor!

If you're planning to attend, you can use my code & save 25% in addition to early registration savings: **mys11fsd**: [http://oreil.ly/goaqst](http://oreil.ly/goaqst)

Hope to see you there!
