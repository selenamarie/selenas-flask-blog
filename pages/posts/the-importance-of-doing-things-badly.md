title: "The importance of doing things badly"
id: 3286
date: 2011-08-01 07:27:28
tags: 
- community management
- doing things badly
- oscon
- oscon2011
- postgres
- postgresql
categories: 
- postgres
- postgresql

_Update: added "code review" to the things that we're doing well below._

There were a couple themes for me from OSCON last week. One is transitions and change. I've got a whole slew of thoughts on this, particularly from my experience leaving the management team of Open Source Bridge. 

But the other is the importance of doing things badly. In particular, the importance of doing things badly in open source.

Tim Anglade, at about 41:10, says that he thinks the reason why open source companies make money is because open source is kind of shitty ([from an interview he did with Cliff Moon last fall](http://nosqltapes.com/video/cliff-moon-on-nosql)). So, on one hand there's a Money Making Opportunity. Probably not the one that we'd all prefer, but it is what it is.

When he said that, I immediately thought about the other things that we do badly (other than documentation) and the discussions I'd been having with people last week.

Basically, we had a problem in the Postgres community of experienced developers solving every small bug at nearly the moment it was reported. It's sort of like a cat sitting at the entrance of the only mousehole.

The effect on the code is amazing - we have clearly documented, concise and consistent code. But the effect on the community is that we don't have mid-level developers, and it is very difficult for inexperienced developers to build up a portfolio of small projects, based on bugs. 

I don't have a ready solution for this problem. And I do not mean this as a criticism of the thousands of hours our core teams have devoted to fixing bugs. We all benefit from the dedication. I am just pointing out that our system had a clear tradeoff - fewer contributors. 

What we could do a bit worse (to address the point of this blog post) is lengthen our response time to solving bugs, and let some less experienced developers respond to the bugs queue. This probably involves creating a bug tracker and holding the tension a bit longer on fixes.

Our committers have made efforts toward spreading the load around more - with [commitfest](http://commitfest.postgresql.org) - meaning a greater support of code review, with [Tom's recent presentations about the planner](http://www.pgcon.org/2011/schedule/speakers/202.en.html), with our [wiki-fied Todo list](http://wiki.postgresql.org/wiki/Todo). And there are many more examples of our committers putting real effort into mentoring, tutoring and finding ways of bringing more people in. 

The thing that's missing from all of those efforts, however, is **urgency**. That's what bug-fixing is great for. That's why we have people who remain in operations work even if they hate being woken up at 3am. Urgent work is worthwhile work (mostly).

I'm sure there are other particular areas where we could do things worse, and thus invite more people to contribute. I'll be thinking about this more in regard to our project event planning, as I think there's a bit of a disconnect there, and a huge opportunity to involve more people.

I'm reminded again of David Eaves' talks about how [community management is the core competency](http://www.slideshare.net/david_a_eaves/community-management-presentation/) of open source, not technology. I struggle with that thought every day, but it rings truer the more I try to work on the significant problems facing any particular open source project. 
