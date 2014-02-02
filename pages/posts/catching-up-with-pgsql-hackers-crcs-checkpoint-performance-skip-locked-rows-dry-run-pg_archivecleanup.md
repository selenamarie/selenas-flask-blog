title: "Catching up with pgsql-hackers: CRCs, checkpoint performance, SKIP LOCKED ROWS, dry-run pg_archivecleanup"
slug: catching-up-with-pgsql-hackers-crcs-checkpoint-performance-skip-locked-rows-dry-run-pg_archivecleanup
id: 3686
date: 2012-02-07 08:25:04
tags: 
- catching up with pgsql-hackers
- postgres
categories: 
- pgsql-hackers
- postgres
- postgresql

I've been sick for a few days, so I settled in with a nice cup of tea and started in on the tremendous backlog I've got on pgsql-hackers. I put patch status at the end of each paragraph. 
<!--more-->
The first thread I read was a patch for [implementing 16-bit CRCs for all buffer pages](http://archives.postgresql.org/message-id/CA+U5nMJzQyxcObkpNAf1SYTX-gO_Mom3O9JXHnGpxRo1kXJ7ww@mail.gmail.com). This is the most recent patch in a multi-year effort around CRCs. There are many small and large problems with implementing this (performance, hint bits and cramped page header space for starters). If you read the whole thread, you'll see some interesting compromises, and the role that pg_upgrade now plays in the stewardship of page format changes.  Patch is still under review.

That lead me over to performance [testing results](http://archives.postgresql.org/pgsql-hackers/2012-01/msg00943.php) from what was titled as a double-write buffer patch from VMWare. The author of these patches doesn't respond to comments in-line like everyone else on -hackers does, so it makes his responses pretty difficult to track relative to everyone else. Still WIP.

And, related a [checkpoint performance tuning treatise from Greg Smith](http://archives.postgresql.org/pgsql-hackers/2012-01/msg00883.php). This started from a patch to add a parameter that allows adding pause time before a checkpoint. He points out that to tune this usefully, you need to know what the number of files a checkpoint typically syncs. (and [has a related patch that publishes this information](http://archives.postgresql.org/message-id/4F13C38D.2080905@2ndQuadrant.com)). Patches are still under review. 

There's another discussion about [SKIP LOCKED ROWS and a patch](http://archives.postgresql.org/message-id/CADLWmXUUjmrPU-+9ss7BCATxM-hr6__9mB6Wv7ry3-r+KXGgBw@mail.gmail.com), apparently a commercial database feature. Early WIP.

In usability land, there was [an addition of a "dry-run" feature to pg_archivecleanup](http://archives.postgresql.org/message-id/4EE4C393.4060302@2ndQuadrant.it). This one's committed!

This all makes me so excited for the 9.2 release this year. Also, great to see a bunch of new folks submitting patches.
