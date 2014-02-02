title: "Using logger with pg_standby"
slug: using-logger-with-pg_standby
id: 1887
date: 2010-08-29 08:00:26
tags: 
- hotstandby
- logger
- pgstandby
- pg_standby
- postgres
- postgresql
- syslog
categories: 
- postgres
- postgresql

Piping logs to syslog is pretty useful for automating log rotation and forwarding lots of different logs to a central log server. 

To that end, the command-line utility 'logger' is nice for piping output from utilities like pg_standby without having to add syslogging code to the utility itself. Another thing is that logger comes by default with modern packages of syslog.

Here's an easy way to implement this: 

` 
restore_command = 'pg_standby -d -s 2 -t /pgdata/trigger /shared/wal_archive/ %f %p %r 2>&1 | logger -p local3.info -t pgstandby'
`
