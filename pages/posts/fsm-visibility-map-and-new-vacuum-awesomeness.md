title: "FSM, visibility map and new VACUUM awesomeness"
slug: fsm-visibility-map-and-new-vacuum-awesomeness
id: 677
date: 2009-02-10 18:26:43
tags: 
- 8.4
- configuration
- fosdem
- fosdem09
- free space map
- heikki linnakangas
- improvements
- internals
- performance
- postgres
- postgresql
- vacuum
- visibility map
categories: 
- conference
- open source
- postgres
- postgresql

<center>![](http://www.chesnok.com/daily/wp-content/uploads/2009/02/heikki.png "heikki")
<font size='-1'>Heikki Linnakangas, listening as Simon Riggs sketches on the chalkboard.</font></center>

**Update:** Heikki's slides are [here](http://wiki.postgresql.org/wiki/Image:FSM_and_Visibility_Map.pdf)!

Heikki Linnakangas gave a presentation this past Sunday at [FOSDEM](http://www.fosdem.org/) about the improved free space map (FSM), which tracks unused space inside the database, and new visibility map, a bitmap which will indicate which data pages can be skipped during a partial VACUUM.  This performance enhancement will affect all users of the upcoming 8.4 software release. You can see what the new FSM implementation looked like [back in October](http://www.depesz.com/index.php/2008/10/04/waiting-for-84-new-fsm-free-space-map/) from [depesz's blog](http://www.depesz.com/).

Despite Heikki's modest claim during the talk that the performance tests were inconclusive, the consensus among [Postgres contributors](http://blog.hagander.net/archives/129-Visibility-map-arrives.html) is that this feature will result a substantial improvement in the performance of VACUUM for tables that are large, but have few UPDATEs.

The new free space map and Visibility map (in 8.4) and autovacuum (enabled by default starting in version 8.2) are huge administrative usability improvements to version 8 of Postgres. Prior to version 8.1, VACUUM had to be scheduled outside of database system. [Autovacuum](http://www.postgresql.org/docs/8.2/static/routine-vacuuming.html#AUTOVACUUM) has been part of the core Postgres distribution for over two years, and is tunable via several [global configuration parameters](http://www.postgresql.org/docs/8.3/static/runtime-config-autovacuum.html). 

The visibility map enables partial VACUUMs -- meaning that VACUUM no longer has to examine every tuple to update the FSM. The new FSM implementation eliminates two configuration parameters, effectively automating a formerly manual configuration process.

The new FSM is stored on disk in seperate files inside of $PGDATA/base/, and is cached in shared_buffers.  The result is that the max_fsm_* configuration parameters are no longer in 8.4 -- Postgres is able to track and adjust this data structure without user intervention.  

A few critical features of the new FSM are: 

* Now a binary tree structure
* Constructed using 1 byte per heap page
* The top level shows the maximum amount of contiguous space available
* The data structure is auto-repairing and can be reconstructed from the bottom

Previously, every time that VACUUM was run, the free space map had to be reconstructed from scratch. Now, individual nodes in the map may be updated (aka "retail" updates). 

Visibility map is a bitmap of heap pages which tracks which tuples on pages are visible to transactions, and therefore not available for VACUUMing.

Previously, when VACUUM ran, it *had* to look at every tuple in a table, because there was no information about which pages may not have been updated since the last VACUUM. With the visibility map, VACUUM will now be able to perform partial scans of table data, skipping pages which are marked as fully visible.  Partial scans means fewer I/O operations for VACUUM, and happier database administrators.
