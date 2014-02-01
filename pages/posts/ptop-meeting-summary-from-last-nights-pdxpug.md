title: "ptop - meeting summary from last nights pdxpug"
id: 175
date: 2007-11-16 10:04:04
tags: 
- postgres
categories: 
- pdxpug
- postgres
- postgresql
- sysadmin
- user groups

Last night's meeting was about [ptop](http://pgfoundry.org/projects/ptop) and Mark Wong's efforts to make an interactive, command-line tool for monitoring the current status of a PostgreSQL database.

For our meeting, Mark set up a test operating system on a USB drive, and bravely demo'd his new software.

Mark got the idea for ptop a few months ago, and went looking for the source code to top to get started. After a few days of hacking, he had a some useful features he wanted to share. So, he's set up a project and started gathering developers:

[http://pgfoundry.org/projects/ptop](http://pgfoundry.org/projects/ptop)

The features currently supported include displaying:

*   Current queries
*   Query plans
*   Locks
*   User table statistics
*   User index statistics

<!--more-->

One feature I particularly liked was showing deltas of statistics over time. So you set your ptop sampling interval to some value (i.e. 5 seconds) and then you can see, for example, user table statics
changing over time. This is something I wrote some perl scripts for, but would love to have as a standard utility.  Particularly if I could log/graph it.

Currently, ptop is only compiling on Linux. I really want it on Mac OS X.

We came up with a short list of desired features for the next revision of ptop:

*   Change command line options to match psql (-U for user, -p for port, etc)
*   Add command to show table (basically \dt [tablename]) for non-query processes
*   Enable arrow keys to move around in the content to select, instead
of cut/paste process ID
*   Log the stats deltas over time (i would be very interested in this)
*   Change lock query to use an OUTER JOIN to show "waiting" locks that
aren't granted

And just a general question that came up:

*   Is it possible to peek at a currently executing SELECT statement's plan?
       - We all agreed that this would be awesome.

Thanks for a great meeting.

* * *

Thank you Mark & Gabrielle for sending out meeting announcements this month.

NEXT MEETING: DIFFERENT DATE AND TIME!

[December Coders Bash](http://pdxgroups.pbwiki.org/2007%20December%20Coders%20Social)
Tuesday, December 11, 2007
CubeSpace, 622 SE Grand Ave., Portland OR 97214

Sam from the PHP Users group started organizing a group event in
December, inviting folks from all the different users groups to come
and socialize.

ALSO a HACKATHON:
Gabrielle, Mark and I thought it would be awesome to have a ptop HackAThon the weekend after Thanksgiving. Some possible features we'd work on are below. Anyone interested? Get in touch.  I was thinking the early afternoon on Saturday, or early evening on Sunday.
