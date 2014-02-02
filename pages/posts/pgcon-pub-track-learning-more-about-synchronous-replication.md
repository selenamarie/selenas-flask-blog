title: "PgCon Pub Track: Learning more about Synchronous Replication"
slug: pgcon-pub-track-learning-more-about-synchronous-replication
id: 3007
date: 2011-05-21 11:00:44
tags: 
- pgcon
- postgres
- postgresql
- pubtrack
categories: 
- postgres
- postgresql

[![](http://www.chesnok.com/daily/wp-content/uploads/2011/05/5743376089_815a3b3c80_b-300x225.jpg "5743376089_815a3b3c80_b")](http://www.chesnok.com/daily/wp-content/uploads/2011/05/5743376089_815a3b3c80_b.jpg)

So, we're at the Pub and doing ["create a billion tables" time trials](http://it.toolbox.com/blogs/database-soup/one-billion-tables-or-bust-46270) with Jan Urbanski using Python and Josh Berkus using Perl.

We're also hacking on a test framework the Slony developers have, specifically hacking with [Steve Singer](http://scanningpages.wordpress.com/). What we discovered is that sync rep doesn't wait for a WAL segment to be *replayed* before it returns. In the pg_stat_replication table, we see sent_location, write_location and flush_location synchronized, but not replay_location.

This makes sense from a database perspective, but may be surprising behavior for application developers. There are patches out there (according to what I just heard from Bernd) to make synchronous replication wait for replay on the slave, but it's not certain when that will be committed. It definitely won't be part of version 9.1.

I just [wrote up configuration details from a database administrator's perspective](http://tech.myemma.com/replication-synchronized/), and am planning on doing some additional work to make a highly condensed configuration tutorial for our main docs.  We definitely need to explain this more clearly for users, who might be thinking of it more from an application perspective.
