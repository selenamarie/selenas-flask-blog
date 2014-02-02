title: "Raw notes from Kevin Grittner's talk on SSI"
slug: raw-notes-from-kevin-grittners-talk-on-ssi
id: 2750
date: 2011-03-24 05:02:48
tags: 
- postgres
- ssi
categories: 
- postgres
- postgresql

This is just a quick dump of my notes from yesterday. Unfortunately, the talk wasn't recorded, but Kevin (and Dan Ports) is [giving a similar talk on this topic](http://www.pgcon.org/2011/schedule/events/333.en.html), more focused on core developers at PgCon. 

<!--more-->

<pre>
== True Serializable Transactions Are Here ==
Kevin Grittner's talk
Serializable Snapshot Isolation

snapshots
* Serializable or repeatable read uses one snapshot for entire transaction
* read committed - new snapshot for each statement, and may see data outside snapshot if it is blocked by a write conflict

declarative constraints 
- can do in triggers with the new serializable code, BUT DON'T DO THAT
- esp exclusion constraints
- always use the most specific constraint you can get away with

== blocking on locks ==

row granularity: update/delete, select for update, select for share
- cause write to disk
- last until commit or rollback

table granularity
- automatic locks as part of most sql statements
- explicit locks can be made in application programming -- get it before you do your other stuff, because if you later get your lock, someone else might have dove in.
- limited by shared memory allocation
- last until commit or rollback
- for repeatable read, or serializable, must be acquired before data access

advisory
- based on numbers with no standard semantics (??)
- may be acquired and released at any time

== Serialization failures have a specific SQLSTATE ==
- sql standard: write conflict - cancels a transaction using sqlstate 40001
- deadlock: cancels a transaction using sqlstate 40P01
- dangerous structure: non-blocking read/write conflicts and a commit which form a possible cycle in the apparent order of execution among two or three concurrent transactions) cancells a transaction using SQLSTATE 40001

Transaction retry -- all should be safe for retry
* immediate retry of the canceled transaction is very unlikely to fail again on conflict with the same set of transaction
* don't want to use SSI if you don't have a framework to automatically retry
* automated means of transaction retry based on SQLSTATE is highly desirable

Kevin's code --> 
* everything in Java Class checks for the serializable state error and retries 

== Simple cases ==
*SQL standard does not specify that the order has to be consistent with the commit order*

Actual transaction serialization
* transaction isolation doesn't matter, apparent order of execution can always be considered to match actual order of exec 

All reads
* apparent order can be anything because nothing changed

One writer and many readers
* if readers are repeatable read or serializable there is no blocking and xactions are completely isolated
* when read only trans overlaps the read/write the read-only trans can always be considered to be executed first since it can't see the work of the writer
* apparent order of readwrite can always be considered to match order of execution

== Read committed ==

== serializable ==
* writes don't block reads, they just rollback to avoid conflicts

ANOMOLIES!
simple write skew
* two concurrent transactions can generate a result which could not have occurred if either committed before the start of the other this is known as write skew. 
* if either had run first, there could not be both kiwi fruit

more than two transactions
* T0 tries to read data matching what t1 writes
* t0 and tn both overlap with t1
* t1 tries to read data matching what Tn writes but can't see Tn's writes because they are concurrent
* Tn commits first
* SSI makes an assumption that Tn depends on T0 in some way which makes it look like Tn executed before T0
** Issue: this could be through multiple transactions and involve different types of dependencies

attempts to do full cycle tracking: too much cost in tracking all those complex possibilities

== multi-row integrity constraints ==
** read up on this.

== TO USE SSI ==
* Identifying conflicting transactions
** intuition: small data, well-versed developers
** reaction: when data is found which violates the rules!
** static analysis: manually or using software, search application code for transactions and build a graph of all dangerous interactions among them

programming to protect against anomalies
* external scheduling
* materialize the conflict 
* promote the conflict
* lock tables

== SSI ==
* published in 2008 -- best paper at ACM SIGMOD, Michael Cahill (2009)
* First production level implementation of it !!

== Tradeoffs ==
* Advantages
** simplified programming
** avoids table level locks
** no extra disk writes (like select for update would generate)
** no blocking beyond current snapshot isolation

* Disadvantages
** database client must be prepared to handle serialization failure from any serializable query at any time
** cause of ser failure may not be obvious
** will sometimes happen on read-only transactions
** rate of serialization failure is higher than other techniques

DB2 stress test.. Daniel (who?) worked on this with Kevin

Where is serializable a good fit? 
* many devs write queries for a single database
* ad hoc queries are run against the database
* some or all queries are generated by a framework or ORM
* multi-row integrity rules are enforced by triggers or app code
* data violating business rules have been found .. and corruption is occuring

== how to maximize performance ==
* declare transactions as READ ONLY when possible
* control the number of active connections, using a connection pool. especially important with SSI
* don't put more into a single transaction than is needed for integrity purposes
* don't leave connections dangling "idle in transaction" longer than necessary
* eliminated explicit locks, select for update and select for share where no longer needed due to protections automatically provided by serializable transactions

Michael James cahill - http://hdl.handle.net/2123/5353
Sudhir Jorwekar, fekete, ramamritham, sudarshan, http://www.cse.iitb.ac.in/~udarsha/Pubs-dir/VLDB07-snapshot.pdf
Tom lane: http://www.postgresql.org/files/developer/concurrency.pdf

== ssi with hot standby ==
* we don't support it with hot standby -- throw an error if people request it on the hot standby 
** maytbe 9.2 we can cover transient anomolies

** Dan at MIT 
** wants to upgrade the predicate locking on btere to usee next key, finer grained than page locking

-- indexes other than btree are locking at index relation level, get finer grained on that

</pre>
