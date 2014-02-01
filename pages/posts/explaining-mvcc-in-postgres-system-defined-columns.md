title: "Explaining MVCC in Postgres: system defined columns"
id: 1921
date: 2010-09-01 07:00:18
tags: 
- mvcc
- postgres
- slides
categories: 
- postgres
- postgresql
- presentation
- speaking

[![](http://www.chesnok.com/daily/wp-content/uploads/2010/09/Untitled.png "How MVCC is implemented in PostgreSQL")](http://www.chesnok.com/daily/wp-content/uploads/2010/09/Untitled.png)

I'm playing around with some diagrams for explaining MVCC that I'll be posting here over the next few days. Not sure if I'll end up giving up on slides and just use a whiteboard for the talk. I made an [illustrated shared buffers](http://www.slideshare.net/selenamarie/illustrated-buffer-cache) deck to go along with Greg Smith's excellent talk on shared buffers a while back. This is the beginning of a talk that I hope will emulate that.

[Here are my first few slides](http://www.chesnok.com/daily/wp-content/uploads/2010/09/mvcc_in_postgres.pdf), showing the system-defined columns. The next few slides will describe optimizations PostgreSQL has for managing the side effects of our pessimistic rollback strategy, and reducing IO during vacuuming and index updates.
