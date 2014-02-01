title: "Q&A about Hot Standby "
id: 1813
date: 2010-07-12 20:17:16
tags: 
- 9.0
- hot standby
- postgres
- postgresql
- q&amp;a
- quickstart
categories: 
- postgres
- postgresql

**Updated!**: See below.

Here are some questions that came up from trying to use the current [PostgreSQL hot standby](http://www.postgresql.org/docs/9.0/static/hot-standby.html) documentation: 

**Q: If you set `hot_standby = off` after having it on, what happens? 
**
A: This change requires a database restart on the hot standby (or replica) server. The database goes into "warm standby" mode, and you can no longer issue queries against it. You can change this right back by setting the parameter to 'on' and restarting again.

**Q: Can you use hot standby with only a single schema or database?
**
A: No. Hot Standby is all-or-nothing for a particular PostgreSQL [database cluster](http://www.postgresql.org/docs/9.0/static/creating-cluster.html). A cluster is made up of all the databases that live in a particular $PGDATA instance, and Hot Standby is currently not capable of distinguishing between changes occurring on different particular databases or schemas.

**Q: Is the process for setting up hot standby any different for empty databases vs. populated databases?
**
A: No. The setup process is the same - you must create a [base backup](http://www.postgresql.org/docs/9.0/static/continuous-archiving.html#BACKUP-BASE-BACKUP).

**Q: How do I bring my hot standby out of standby mode? 
**
A: If you're using something like the following in your recovery.conf file: 
`
restore_command = 'cp xxxx' 
standby_mode = 'on'
`

Change: `standby_mode = 'off'` and restart your hot standby postgresql instance.

**Q: Where did my `recovery.conf` file go? (after your database came out of warm/hot standby)
**
A: PostgreSQL automatically changes the name of the file to `recovery.done` when recovery completes. This helps prevent accidents.

**Q: What happens if my `archive_timeout = 60` (which creates a 16mb file every minute) and I flood the database with so much activity that my standby falls behind?
**
A: This is possible, and you may be interested in trying [Streaming Replication](http://www.postgresql.org/docs/9.0/static/warm-standby.html#STREAMING-REPLICATION). However, for the majority of users, a delay in restoring data is acceptable (and possibly desirable). Eventually the standby server will catch up.  You can monitor how delayed the server is using functions like   `txid_current_snapshot()`.

**Q: Are schema changes (like CREATE TABLE or ALTER TABLE) replicated to the standby?
**
A: Yes! All changes to the database cluster are copied to the standby. This includes any DDL operations, new rows, the effects of autovacuum -- any change to the data store on the master is copied to the standby.
