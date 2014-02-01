title: "synchronized scanning talk"
id: 120
date: 2007-08-17 00:00:17
tags: 
- postgres
categories: 
- postgres
- postgresql

_I normally post a long email about PostgreSQL talks we have here in Portland for PDXPUG meetings.  Below is a draft of what I'll be sending to the list._

The August 16th meeting began with a short discussion of Rules vs. Triggers. I didn't come up with an EXPLAIN operator to talk about, but had recently run into a situation where I could have implemented something as a RULE or as a TRIGGER. Jeff explained that for table partitioning, the recommendation was to use Triggers. This had to do with some odd cases where you had a query whose predicate would be altered by the RULE in such a way as to render the "window" of data's result NULL.  Hrm.  We all talked about that for a while, tried to come up with an example case - which was hard. Then we tried to blame something on MySQL that will remain undiscussed. And then we moved on.

I would like to revisit rules vs. triggers, and come up with the example case!

We had a few new faces - including the leader of the PHP group - Sam! Also, Jerry was looking for someone to help him out with some SQL questions.  We hope he posts some questions to the list.

Jeff's talk was largely about his patch, with a few bits about his development environment, a patch from Simon Riggs that was related but not dependent, and a little database theory thrown in.

The fundamental idea behind Jeff's Synchronized Scan patch is that Sequence Scans can really start at any place between 0 and N, with N being the number of records in a table. It was arbitrary, before his patch to 8.3, that all Sequence Scans were starting at 0\. In the past, DBAs would just need to plan for poor or unpredictable performance when multiple sequence scans occurred.

The patch implements a system where each process keeps track of where a sequence scan is at - in a tiny piece of shared memory. Then, when a new sequence scan starts up on the same table, it is given a hint as to where to start. The effect is that the second sequence scan now asks for data that is in the cache. For any tables that are larger than cache size, and whose queries are I/O-bound, this is a big performance benefit, with no real performance penalties. So awesome!
Jeff also discussed Simon Riggs' patch which implements a very small ring cache to service Sequence Scans. This is also a big performance improvement because it prevents cache pollution by confining sequence scan data to a small space that can't push other cached data around. Jeff mentioned that PostgreSQL already does a pretty good job, but this patch makes the caching even more efficient.

Another topic that came up was the [Linux I/O scheduling algorithms](http://www.redhat.com/magazine/008jun05/features/schedulers/). He had originally tested his patch using Deadline, NOOP, and Anticipatory. When he tried it with CFQ more recently, it didn't work so well. He'd also tested ZFS, which seemed to work well but needed more testing.

Mark spoke up and mentioned that Deadline worked very well in general, non-deterministic cases with PostgreSQL.

There were tons of great questions, and even a few esoteric, theoretical arguments. Very good meeting, everyone!

Afterward, the Lucky Lab was crazy busy! We drank a couple pitchers, talked about the linux kernel, and I think there was a long argument about BSNF.

We did decide that someone was going to have to give a talk on "Hypercubes and Dungeons and Dragons: what you never thought they had in common".
Next month's meeting with be about relational algebra, with James, Vassilis and Rafael tag-teaming.  Rafael has been teaching the intro to databases class this summer at PSU, so he is ready for some real heckling. I can only hope that Randal will be able to make it.
