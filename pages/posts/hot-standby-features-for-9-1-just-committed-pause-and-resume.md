title: "Hot Standby features for 9.1, just committed: Pause and Resume"
slug: hot-standby-features-for-9-1-just-committed-pause-and-resume
id: 2533
date: 2011-02-10 09:21:33
tags: 
- 9.1
- commits
- features
- hot standby
- postgres
- postgresql
- simon riggs
categories: 
- postgres
- postgresql

On February 8th, [Simon Riggs committed a couple new functions](http://git.postgresql.org/gitweb?p=postgresql.git;a=commitdiff;h=8c6e3adbf792c2bba448e88cbf2c8e03fb802e73) that will allow Hot Standby to be paused and resumed. You can already *read* from the Hot Standby without pausing, but you could never pause the application of changes in the past. You might want to do this if you have a very high-write-volume server, and some very expensive queries that you want to run on a slave.

> Basic Recovery Control functions for use in Hot Standby. Pause, Resume,> 
> Status check functions only. Also, new recovery.conf parameter to> 
> pause_at_recovery_target, default on.

The basic idea is that if you have a read-only standby system, you can give it the command: `pg_xlog_replay_pause()` and the standby will stop applying changes. Then you can use the database in read-only mode without new changes being applied. When you're done you can issue the command: `pg_xlog_replay_resume()` and proceed with applying logs.

There are some related features that I can't wait to test out around [named restore points for replay](http://git.postgresql.org/gitweb?p=postgresql.git;a=commitdiff;h=c016ce728139be95bb0dc7c4e5640507334c2339). But the ability to pause replay and run queries is just awesome. 

This is a feature that Simon talked about [back in 2009 at FOSDEM](http://www.chesnok.com/daily/2009/02/07/simon-riggs-just-rocked-my-world/), and I am very excited to see it implemented.
