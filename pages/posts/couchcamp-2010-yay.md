title: "CouchCamp 2010: yay!"
slug: couchcamp-2010-yay
id: 1951
date: 2010-09-11 11:06:34
tags: 
- community
- couchcamp
- couchdb
- postgres
categories: 
- community
- conference
- postgres
- postgresql

[![](http://www.chesnok.com/daily/wp-content/uploads/2010/09/159321531-6f0a866198fb58529db8291a8139105f.4c8bd1b0-scaled-300x199.jpg "159321531-6f0a866198fb58529db8291a8139105f.4c8bd1b0-scaled")](http://twitpic.com/2muta3 "Share photos on twitter with Twitpic")
_Max in a tree! Talking about GeoCouch_

I was at [CouchCamp](http://couch.io/couchcamp) last week out at the Walker Creek Ranch - a bit disconnected (no cel service, and spotty internet), but fully immersed in the CouchDB community. 

I was there to give a talk on [MVCC in PostgreSQL](http://chesnok.com/talks/mvcc_couchcamp.pdf). I forgot to mention it during my talk, but it was a fitting topic given that I first talked with JChris after a talk he gave in Portland, where I basically trolled him about compaction and MVCC in CouchDB. My goal was to show people the benefits of CouchDB's built-in MVCC, to point out some places where core developers can learn from PostgreSQL and avoid some of the traps we've fallen into over the years. I've got more to say about the talk some other day, but I wanted to just reflect on CouchCamp for a moment.

One comment a friend made was, "Wow, these people are just so nice!" And it's true. Every hacker meetup I attend is full of people who are overwhelmingly kind and thoughtful, and CouchCamp was more of the same. 

CouchDB is at a critical point in their development - [1.0 is out the door](http://www.apache.org/dyn/closer.cgi?path=/couchdb/1.0.1/apache-couchdb-1.0.1.tar.gz), and developers are [already building cool apps](https://voxer.com/) on top of it. [CouchApps + Evently](http://oreillynet.com/pub/e/1604) are an interesting and fun way to get started building things on top of a couch. And [replication parties](http://wiki.apache.org/couchdb/Replication) - seriously awesome.  [Ward Cunningham](http://c2.com/~ward/) is rumored to be considering a CouchDB wiki to drive the [patterns repository wiki](http://c2.com/cgi/wiki?WelcomeVisitors) (And [here it is](http://wiki.ppr.couchone.com/)! Thanks, Max!), and CouchCamp was overflowing with ideas and implementations (distributed social, a replacement for email, [UbuntuOne](https://one.ubuntu.com/)).

So what did I learn at CouchCamp? I learned how to hack on a [CouchApp](http://github.com/selenamarie/couchcamp_profiles) (Thanks for the help, [JChris](http://twitter.com/jchris)!). I learned about what [Max Ogden](http://maxogden.com) [is up to](http://www.slideshare.net/maxogden/how-to-build-an-open-geo-wiki), and am so excited for him and the lucky folks that get to work with him. (and he's running a [hack/project night next weekend](http://calagator.org/events/1250459208) you should TOTALLY GO TO!) 

I heard about the success and tribulations of running CouchDB on the desktop, and the launch of UbuntuOne from [Stuart Langridge](http://www.kryogenix.org/days/). During his talk, Stuart brought up the idea of a general replication API - something that I also believe is important to the growth of open source databases and is critical to enabling data freedom. I met a real, live [Pick](http://en.wikipedia.org/wiki/Pick_operating_system) user/admin/developer, and talked about the inability to move to another system but the possibility of interfacing something like CouchDB to it.  I got to chat with [Rebecca Murphey](http://twitter.com/rmurphey) about Javascript, MVCC and quality booze. I saw bunnies, foxes, deer, raccoons, and tons of bright stars late at night. And, I saw [Damien Katz](http://damienkatz.net/) perform a brief interpretive dance.

I also was pointed to [a retrospective on Couch 1.0 development](http://groups.google.com/group/tumbolia/browse_thread/thread/4a5e8ed2cf064b7b) by Ted Leung. I don't know Noah Slater, but wow, what a testimonial. Noah's comments about why he continues to contribute to CouchDB mirror a [recent thread about PostgreSQL contribution](http://archives.postgresql.org/pgsql-hackers/2010-09/msg00289.php) -- we work on these open source projects because of the incredible community that develops around them.

Thanks, Mikael, JChris, Jan and Damien, and all the CouchDB folks for creating a community that so many people want to contribute and become a part of. I certainly want to be a part of it, and look forward to finding ways of contributing more. 

And thanks for bringing us all together in person. From the squirt guns in the welcome bag, to the campfire and sing-alongs, to the very late night Android libc storytelling by [Aaron](http://github.com/apage43)... These are the moments that glue us all together, and make all that work we do to connect up with one another through software completely worth it. 
