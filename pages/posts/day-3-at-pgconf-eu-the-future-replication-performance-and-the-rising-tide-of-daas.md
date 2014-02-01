title: "Day 3 at PgConf.EU: the future, replication, performance and the closing keynote"
id: 3400
date: 2011-10-21 06:33:36
tags: 
- day summary
- pgconf.eu
- postgres
- postgresql
- talks
categories: 
- postgres
- postgresql

[![](http://www.chesnok.com/daily/wp-content/uploads/2011/10/closing_keynote_audience-300x225.jpg "closing_keynote_audience")](http://twitpic.com/73jjap "Audience in closing keynote at #pgconfeu   on Twitpic")

I was room host for Simon Riggs, Magnus Hagander and Greg Smith today before giving my final talk this afternoon. 

The morning started with Simon Riggs [talking about his wishlist for the future of Postgres](http://www.postgresql.eu/events/schedule/pgconfeu2011/session/199-postgresql-roadmap/) - including some boundary-stretching ideas for bi-directional replication (a way to possibly support multi-master architecture for Postgres). Simon named his talk "Postgres Futures", but also called it his personal "shopping list" of features he'd like to see implemented, or implement himself. [Magnus deep-dove into the replication protocol](http://www.postgresql.eu/events/schedule/pgconfeu2011/session/147-the-postgresql-replication-protocol-tools-and-opportunities/) and how to use pg_basebackup with 9.1\. [Greg's talk on benchmarking](http://www.postgresql.eu/events/schedule/pgconfeu2011/session/157-bottom-up-database-benchmarking/) is always fantastic, and I learn something new every time. He included some graphs for FusionIO testing he'd done in the last couple weeks. 

I also gave my last talk of the conference, "[Managing Terabytes](http://www.slideshare.net/selenamarie/managing-terabytes)" about my experiences managing 8.x version clusters of a terabyte or larger in size for several companies. I reorganized this talk from the last time I'd given it, and I think it came across quite a bit more clearly to the audience. One developer gave me the suggestion that I should have tried to do a series of updates to a catalog tables to try to recover page space. I'm designing a little test case to help someone do this in the future if they run into this problem with older versions of Postgres. HOT (8.4 and later) essentially fixes this issue, by the way.

The keynote was shared by Ed Boyajian and Bruce Momjian. Ed mentioned that Oracle had the best earnings statement ever in the most recent shareholders call. In spite of that, there's a rising tide of Oracle users who are looking for alternatives, given how strongly they're locked into their technology. He said that he was recommending companies use Postgres is a strategic lever to negotiate with Oracle. And as IT departments strapped for cash are trying to figure out how to fund new data initiatives - they're turning to products that are free.

Bruce then quoted the opening keynote by Ram Mohan - "With open source, support is a whole new level." And Bruce's comment was that what Ram did when he started 10 years ago with Afilias was heretical for conventional IT wisdom at the time. 

Bruce also said that he'd always thought Postgres would ultimately only ever be a niche player among databases. But with all the progress we've made as a project, and the new markets being explored, he sees much greater possibilities for the project.

He asked the audience about the speed at which bugs had been fixed - within 24 hours, a few days or a single week. Only one hand was raised for a bug requiring more than 1 week to be fixed, among probably 40-50 hands raised for much faster fixes.

Bruce also noted that developers are often moved to work and stay with Postgres as a project, because they have decided that "this is an important thing for me to do in my life."

PgConf EU was a great conference, and I'd be happy to be invited back, wherever they decide to hold it in 2012.
