title: "Simon Riggs just rocked my world."
id: 655
date: 2009-02-07 09:49:20
tags: 
- fosdem
- fosdem09
- hot standby
- postgres
- postgresql
- replication
- talk
categories: 
- community
- conference
- open source
- postgres
- postgresql
- presentation

<center>![](http://www.chesnok.com/daily/wp-content/uploads/2009/02/simon-300x199.jpg "simon")</center>

I'm in Brussels for the FOSDEM conference, hanging out at the [PostgreSQL](http://postgresql.org) booth, meeting my [European colleagues](http://postgresql.eu), and running into [friends](http://twitter.com/AE3nn).

PostgreSQL has a [developer's room](https://www.bsdwiki.de/FOSDEM_2009#Developers_room) and [Simon Riggs](http://www.linkedin.com/in/simonat2ndquadrantdotcom) just wrapped up a talk about Replication.  I sincerely hope that the video of the talk turned out well, because it was the most inspiring and technically interesting talk I have seen in a very long time. Unfortunately, I don't have a copy of the slides at the moment, but word is that they will be posted on the [BSD wiki](https://www.bsdwiki.de/FOSDEM_2009) soon.

Simon focused on new features in 8.4 that affect file-based replication, also mentioning streaming, synchronous replication -- which will not be included in 8.4, but is being actively worked on. He explained his rationale for objecting to the inclusion of the synchronous replication patches, mostly, I think, based on the complexity of the WAL archiving required as it was implemented. 

Then, Simon launched into an in-depth tour of the issues and solutions brought about during his team's work on Hot Standby. Hot Standby allows read-only queries to be made against a file-based replication enabled Postgres server, known as Point-in-time recovery and WAL Shipping in the Postgres documentation. 

Simon started work on PITR-related patches about five years ago, and continues that work with others today. 

One fascinating aspect of the hot standby patches is that they ultimately caused performance improvements in sub-transactions across the board - and will likely cause up to 5% improvement in that code path. There were other performance improvements, but I'll wait for the slides to mention those. At several times during the talk, Simon pointed out features that Postgres has that no other database has -- such as multiple options for dealing with conflicts in hot standby (freezing, conflict resolution and timeout).

At the end of the talk, Simon spent a few minutes talking about how Postgres is capable of being the best database, not just the best open source database.  And how all the people in the room were capable of contributing as he had.  He claimed that prioritization and aiming to work on the biggest, most interesting problem you can are all you need.  And he claimed that all that made him different was that he was a little more persistent about solving problems. 

Rock on, Simon.
