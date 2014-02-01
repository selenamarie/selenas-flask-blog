title: "Everyday Postgres: Tuning a brand-new server (the 10-minute edition)"
id: 5082
date: 2013-11-13 12:03:45
tags: 
- everyday postgres
- performance
categories: 
- postgresql

Server tuning is a topic that consumes many books, blog posts and wiki pages.

Below is some practical advice for getting low-hanging fruit out of the way if you're new to tuning Postgres and just want something that will likely work well-enough on low volume systems. I'd say looking at this list and making changes on a new system should take 10 minutes or less.

## Run pgtune

Greg Smith open sourced a utility for making a first pass at tuning Postgres for a local system with [pgtune](https://github.com/gregs1104/pgtune). This tool is easy to run - just copy it to a target system and then point it at your existing Postgres config. It puts its changes into a new file at the very bottom.

## Use XFS

Filesystem choice matters. Greg Smith goes into some detail on why ext3 is a terrible performance choice for a database filesystem in his talk [Righting Your Writes](http://www.2ndquadrant.com/media/pdfs/talks/RightingWrites.pdf). At this point, XFS is the filesystem that should be your default choice. If you want to explore ext4 or zfs (if that's an option for you), that may be worth looking at. It is "safe" however to choose XFS. Depending on your disk situation, recreating your filesystem might take a bit longer than 10 minutes, but hopefully this will save you time and bad performance in the future!

## Increase your readahead buffer

On Linux, the readahead buffer ([brief explanation](http://makarevitch.org/rant/bufchint.html)) is set way to small for most database systems. Increase this to about 1 MB with `blockdev -setra 2048 [device]`.

## For further performance analysis

I wrote this [performance checklist](http://www.chesnok.com/daily/2011/09/22/my-postgres-performance-checklist/) a while back for assessing a system's health. I'd say a review of all the things on that list would take probably half a day. Following up and making the changes could take a day or more. These kinds of analysis are worth exploring periodically to ensure you haven't missed important changes in your environment or your application over time.
