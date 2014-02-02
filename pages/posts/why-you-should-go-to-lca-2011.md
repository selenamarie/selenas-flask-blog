title: "Why you should go to LCA 2011"
slug: why-you-should-go-to-lca-2011
id: 1419
date: 2010-01-27 08:17:59
tags: 
- conferences
- lca2010
- new zealand
categories: 
- conference
- personal

<center>[![capsicum](http://www.chesnok.com/daily/wp-content/uploads/2010/01/capsicum-300x225.jpg "capsicum")](http://www.chesnok.com/daily/wp-content/uploads/2010/01/capsicum.jpg)</center>

I returned from LCA 2010 on Sunday with an ecstatic grin, and tons of projects to work on for the rest of the year. I was lucky enough to have [End Point](http://endpoint.com/) send me to New Zealand! I knew a few of the organizers, and had high expectations. LCA totally surpassed them all.

Next year, [LCA will be held in Brisbane, Australia](http://followtheflow.org/). You should really go.

I'll break it down for you: 

* Content

The talks were really good. People went out of their way to talk about the technical issues they are facing without sugar coating it, dumbing it down, or resorting to lists of features. 

[Ted Ts'o](http://thunk.org/tytso/blog/)'s talk on [EXT4 development](http://www.lca2010.org.nz/programme/schedule/view_talk/50291?day=wednesday) was amazing in this regard. I came thinking that he'd give a laundry list of features, how it differed from EXT3, when he thought they'd be "production ready". What I got instead was an incredibly detailed accounting of the failures in testing and systems analysis that filesystems developers had encountered over many, many years. The new development effort had its own fair share of bug creation, but they also found long standing bugs in EXT3\. He went so far as to break down effort in terms of new feature creation, bug fixing and two other tasks (i wish I had a copy of the slides already!). Anyway, interesting talk, great advice for those who work with concurrency-sensitive applications (most of us these days) and very interesting case studies in failure. 

Paul Gunn, an engineer at [Weta Digital](http://www.wetafx.co.nz/), gave a detailed talk on his experiences scaling their data centers. Much of the lessons there were fairly well understood by data center engineers (hot/cold aisles, raise the temperature to save some dollars!, don't cram stuff under the floor where air is supposed to flow!, use high ceilings to sink heat). It's always great to see companies sharing their practical experiences with developers. 

Another fun project I learned about was [Sheepdog](http://www.osrg.net/sheepdog/) - an EBS replacement developed by a team from NTT. The whole project looked fantastic - providing snapshot, cloning and thin provisioning, and a reasonable looking GUI. This could be a fundamental building block of free clouds.

I also was inspired by [Cucumber-nagios](http://auxesis.github.com/cucumber-nagios/), a relatively new project from Lindsay Holmwood. He and others have been talking about "[behavior driven infrastructure](http://holmwood.id.au/~lindsay/2009/11/09/behaviour-driven-infrastructure-through-cucumber/)", a great bit of syntactic sugar on systems automation work that started with cfengine in the early '90s. I look forward to playing around with these tools. And I really like that he leveraged nagios' existing interfaces rather than inventing something new. This type of collaboration between projects is a breath of fresh air for sysadmins, who (if they're anything like me) struggle to make awesome new tools talk to the awesome old ones.

I spent some time in an Arduino intro class, soldering and hacking on a temperature probe for a few hours. I ended up with a working temperature monitor and an appreciation for how easy to use the tools are.

* Hallway Track

There was a fantastic common area filled with people hacking on their talks, having conversation or maybe just hanging out to see what would happen next. IRC was full of hilarious chatter, and people connecting to see new babies (my god, so many people have had babies!).

There were also some couches, and a nice courtyard that often filled up with people. The common spaces in a conference seem to determine how well people can connect once they're not just sitting in front of a speaker. 

Another convenient and wonderful aspect of the location was the food. Excellent restaurants at reasonable prices were within a 5 minute walk of the conference venue. This made impromptu coffee breaks and relaxed but productive lunches very easy and enjoyable. I really, really liked this.

* Inspiration

Three keynotes by Biella Coleman, Benjamin Mako Hill and Glyn Moody were inspirational and subversive. All three were rallying cries for a hacker mentality - the drive to tweak, tinker, create and share. All three spoke to the pleasures and joys of software development. 

Biella Coleman brought up the origins of the Free Software Foundation, and even played a video of a very young Richard Stallman talking about his frustration with not being able to modify source code. She also discussed the responsibility leaders in free and open source have to be transparent in their management of their projects (and how we remind ourselves of that in amusing ways).

Benjamin Mako Hill gave a rallying talk about [antifeatures](http://wiki.mako.cc/Antifeatures), and how their existence is a competitive advantage for free and open source software. [Pia Waugh gave a detailed description](http://pipka.org/blog/2010/01/20/linux-conf-au-2010-%e2%80%93-day-3-freedom-games-bruce-campbell/) of the talk, and the categories of antifeatures - protection money, market segmentation, securing monopolies and protecting copyrights. A memorable quote was "I have yet to meet a free software DVD player that respects the unskippable DVD track." Mako reminds me that humor is the best medicine for something that's seriously broken.

Glyn Moody went a slightly different route - talking about how sharing and openness are leaking out into the rest of the world. The Human Genome Project and Project Gutenburg were two of several examples he used, and to briefly cast a glance at what was at stake if public ownership had not been achieved - in particular with the Human Genome Project. He managed to convey a sense of urgency and importance that is often missing. 

What free software actually gets used for and why are critically important stories. We all need to get better at telling compelling stories.

* Friendship

Free software is built on friendships. Trust, willingness to make mistakes in front of each other, and a desire to build on top of others work to make something better are the traits I see among those who collaborate with each other. Building free software can be a painful process - long nights, tedious bugs, no recognition for the work that went into it all. Conferences like LCA are a tremendous affirmation of the work that we all do.

From the scripted get-togethers, to the spontaneous hackfests and anti-scripted gatherings (the un-professional networking session!), all events are attempts to connect to the other people who know what it's like to live inside of free software. And we relax around each other, make jokes and enjoy for a few days the knowledge that we're doing something really cool.

I met so many people for whose time and attention I am incredibly grateful for. And, for those Kiwis who took me out for great food, shopping and long walks along the pier in the sunshine -- thank you so much for taking the time. I miss you all.
