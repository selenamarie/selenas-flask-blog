title: "GSoC Acceptance, Hstore in Heroku, Inheritance & Sharding, Wikimedia Women's History Month Editathon"
slug: gsoc-acceptance-hstore-in-heroku-inheritance-sharding-wikimedia-womens-history-month
id: 3778
date: 2012-03-16 12:51:10
tags: 
- postgres
categories: 
- postgres
- postgresql

Happy Friday!

[![](http://www.chesnok.com/daily/wp-content/uploads/2012/03/gsoc_postgres_in-300x200.png "gsoc_postgres_in")](http://www.chesnok.com/daily/wp-content/uploads/2012/03/gsoc_postgres_in.png)

[PostgreSQL was accepted into the 2012 Google Summer of Code](http://www.google-melange.com/gsoc/accepted_orgs/google/gsoc2012) program! 180 organizations were accepted, and as they fill out their contact information, they are becoming visible on the GSoC website.
<!--more-->
[Students, please apply](http://wiki.postgresql.org/wiki/GSoC_2012)! Mentors, please let us know you want to mentor! Josh Berkus and Thom Brown are our admins this year, and I'm helping out with communication. 

Heroku Postgres [announced their first supported extension](https://postgres.heroku.com/blog/past/2012/3/14/introducing_keyvalue_data_storage_in_heroku_postgres/): `[hstore](http://www.postgresql.org/docs/9.1/static/hstore.html)`. After the announcement, a few people pinged me with questions, so I'm going to work on a blog post this weekend having a look at `hstore` and `json` support

I wrote a short blog post about [inheritance and sharding](http://www.chesnok.com/daily/2012/03/14/inheritance-and-sharding-with-postgres/). I'm advising people just to not do that, since inheritance doesn't go so well with multi-node architectures. 

This is Women's History Month, and there's an [wiki edit-a-thon at the Wikimedia offices in San Francisco](http://en.wikipedia.org/wiki/Wikipedia:Meetup/San_Francisco_WikiWomen%27s_Edit-a-Thon) from 1-5pm. I'll be there!

Oh, and the [Postgres Open](http://postgresopen.org) site is being worked on. New logo and website refresh now visible. Expect awesomeness next week!
