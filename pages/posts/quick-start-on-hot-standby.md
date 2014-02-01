title: "Quick start on Hot Standby"
id: 1808
date: 2010-07-12 19:48:12
tags: 
- hot standby
- pdxpug
- postgres
- postgresql
- quickstart
- recipe
- replication
categories: 
- postgres
- postgresql

**Updated.**

We could have some better end-user documentation around creating a warm or hot standby system for basic postgresql replication. 

To this end, I created a [Quick Start](http://wiki.postgresql.org/wiki/Hot_Standby#Quick_Start) doc on the wiki, but it could use more help.  Maybe we should create some setup recipes for common situations?

Also - I wrote the following script during a [hot standby bugbash](http://archives.postgresql.org/pdxpug/2010-07/msg00002.php) [PDXPUG](http://pugs.postgresql.org/pdx) had today:

`
#!/bin/sh

BINPATH=/usr/local/pg90/bin
CP=/bin/cp
PGCTL=${BINPATH}/pg_ctl
PSQL=${BINPATH}/psql
INITDB=${BINPATH}/initdb

sudo mkdir -p /var/tmp/archive
sudo chown ${USER} /var/tmp/archive

${INITDB} hotstandby1

echo 'wal_level = hot_standby' >> hotstandby1/postgresql.conf
echo 'archive_mode = on' >> hotstandby1/postgresql.conf
echo "archive_command = 'cp %p /var/tmp/archive/%f'" >> hotstandby1/postgresql.conf
echo "archive_timeout = 60" >> hotstandby1/postgresql.conf
echo "port = 6543" >> hotstandby1/postgresql.conf

${PGCTL} -D hotstandby1 start -l hotstandby1.log
sleep 5

${PSQL} -p 6543 postgres -c "select pg_start_backup('backup')"
${CP} -pR hotstandby1/ hotstandby2
${PSQL} -p 6543 postgres -c "select pg_stop_backup()"
rm hotstandby2/postmaster.pid
rm hotstandby2/pg_xlog/*

echo 'hot_standby = on' >> hotstandby2/postgresql.conf
echo 'port = 6544' >> hotstandby2/postgresql.conf
echo "standby_mode = 'on'" >> hotstandby2/recovery.conf
echo "restore_command = 'cp -i /var/tmp/archive/%f %p'" >> hotstandby2/recovery.conf

${PGCTL} -D hotstandby2 start -l hotstandby2.log
`

* Added port specification in case you've already got postgres running. Added a BINPATH for custom install directories.
