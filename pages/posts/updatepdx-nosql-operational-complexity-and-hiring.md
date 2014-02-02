title: "UpdatePDX: NOSQL, operational complexity and hiring"
slug: updatepdx-nosql-operational-complexity-and-hiring
id: 2855
date: 2011-04-05 06:02:22
tags: 
- move to portland
- nosql
- updatepdx
- user group
categories: 
- portland

[![](http://farm6.static.flickr.com/5176/5591625595_a8e66db0a4_m_d.jpg "Bradford Stephens")](http://farm6.static.flickr.com/5176/5591625595_a8e66db0a4_m_d.jpg)

Last night, [Tim Anglade](http://twitter.com/timanglade), [Bradford Stephens](http://twitter.com/lusciouspear), [Sarah Novotny](http://twitter.com/sarahnovotny) and [Alex Payne](http://twitter.com/al3x) put together a three-part discussion to talk complexity, caching and collaboration, and in some cases, skewer popular notions of problem-solving around NOSQL.

Big thanks to [Michael Schurter](http://twitter.com/schmichael) and [Rick Turoczy](http://siliconflorist.com) for organizing and providing us space at PIE.

Tim was the thinker and designer behind the event. Many thanks to him for putting so much energy and time into it, and helping many leave inspired.

**"Catchy phrases are red herrings." -@timanglade**

The night began with stories of failure: Bradford touched on [the horror of 300-line SQL](https://twitter.com/#!/selenamarie/status/55076068524163072) and the value of applying computer science to solve problems; Sarah [recalled not having restorable data](https://twitter.com/#!/selenamarie/status/55078165651009536) in an emergency because someone had tested a new backup strategy - for six weeks; Alex talked about [the hard problems in computer science (ok, caching)](https://twitter.com/#!/selenamarie/status/55080706774278144) and the [value of culture](https://twitter.com/#!/selenamarie/status/55081006478278656) and mentoring.

What I loved about this part of the evening, is that each person had a story. Technical presentations sometimes lack guideposts, but these stories all had villains, heros and a lesson.

**"Usually they should just hire a MySQL consultant." -@timanglade**

And then Tim followed with a wickedly funny sendup of "the NOSQL movement". The thing that struck a nerve and made the audience laugh uproariously was: "[Only use NOSQL if you reach a certain point of despair.](https://twitter.com/#!/selenamarie/status/55085830930300928)"

[![](http://farm6.static.flickr.com/5302/5592217452_cebe68dd83_m_d.jpg "Sarah Novotny")](http://farm6.static.flickr.com/5302/5592217452_cebe68dd83_m_d.jpg)

His other points included: Never forget the operational complexity; Some things will always be better achieved with an RDBMS; Distribution Model vs. Data Model vs. Disk Data Structure (invoking the [Moon Methodology](http://groups.google.com/group/nosql-discussion/msg/1d818d500c712153)); Hardware will always help, but it will never save you; Given enough time, most NOSQL projects gravitate towards a MapReduce-like model for computations (and querying); Trust no one. That goes double if they talk about CAP.

**And then we talked.**

The audience had plenty of questions, starting with how do we address collaboration in the context of scalability?  

The answers from the panel, disappointingly, seemed to came down to separation of databases and people. While it's true that it is easier to give out more databases than trying to communicate, it shows how far we have to go as an industry. Another point made was that it's not typically possible to repurpose a DBA to maintain something like a Hadoop cluster. 

In my notes, I wrote: "when problems are of a certain size, and affects the DNA of a company." And when that happens, the typical separation of responsibilities between developer, DBA and operations break down. 

[![](http://farm6.static.flickr.com/5023/5592217704_290ec2f07c_m_d.jpg "Alex Payne")](http://farm6.static.flickr.com/5023/5592217704_290ec2f07c_m_d.jpg)

Alex made my night by mentioning that sometimes solving a problem just takes getting a fresh set of eyes on it. He talked about replacing a particular bit of technology by applying some features of Postgres, with the help of a new hire.

I asked the final question - how does a company hire for the types of skills needed to solve these types of problems? Most agreed that finding someone with a passion for learning was critical. There was a dissenting voice - I think Bradford's. My notes trailed off at that point, unfortunately. My guess is that he spoke up for logic and patience, and that some of the problems companies face have been largely solved, if you spend the time to study the science. 

**Epilogue**

We wrapped up the night out at Little Big Burger and the Teardrop. Several people commented on how lovely Portland was - even in the rain. But damn, they wish they could hire the types of people they needed here. 

So, people who are interested in big data: consider that a call to action. 

Visit us for [OSCON Data](http://www.oscon.com/oscon2011/public/cfp/156) this summer. Then, move to Portland.
