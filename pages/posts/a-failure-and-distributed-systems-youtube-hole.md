title: "A Failure and Distributed Systems Youtube Hole"
slug: a-failure-and-distributed-systems-youtube-hole
id: 5246
date: 2015-09-30 22:00:00
tags: 
- distributed_systems
categories: 
- work


I was thinking a lot about a conversation I had with a coworker about failure and an email thread about naming a team and ended up diving deep into a series of blog posts and videos. I mostly wanted to remember the series that I read and saw today, but thought maybe you, dear reader, would be interested too. 

This started out just being videos, but there were quite a few blog posts too.

Here goes: 

* [Each necessary, but only jointly sufficient (2012)](http://www.kitchensoap.com/2012/02/10/each-necessary-but-only-jointly-sufficient/)

This kicked things off for me.. I remember this when it came out and was really happy to have this articulated. My first experience with root cause analysis was not a pretty one. Systems thinking is a skill and not one that is taught enough.

* [Elisabeth Hendrickson Discusses Agile Testing - video (2012)](http://continuousdelivery.com/2012/10/elisabeth-hendrickson-discusses-agile-testing/)

This brought back the testing research I read when I was giving talks about failure, and also shared some things I didn't know about how QA's impact on organizations. Basically, unintended consequences of siloing QA off from dev and a strong recommendation to not have a separate org (and of course it's an argument for agile). In practice, I find that build and test automation requires specialized skills. Maybe orgs can think of these specialists as coaches for the rest of the people in the
org?  The problem I see there is that we've all got a need to create, not just coach and teach. How do you find balance?

* [Debate: What is the Role of an Operations Team in Software Development Today? (2010)](http://www.infoq.com/news/2010/04/debate-role-of-ops)

This is an old argument but relevant to naming operations orgs. I like being reminded of what "the other side" thinks, and being able to read about it before I have to enter into these kinds of discussions. 

* [There is no such thing as a devops team (2012)](http://continuousdelivery.com/2012/10/theres-no-such-thing-as-a-devops-team/)

I was reading this also in trying to think up alternatives to "operations" as a team name. 

* [Risk management theater (2012)](http://continuousdelivery.com/2013/08/risk-management-theatre/)

I loved the chart here. There is a "lean organizations" book out there now that has a section on this. Not sure I want to read the book, but this is a handy reminder about what you sacrifice when you go to command-control models for risk management.

* [Blameless Post-mortems (2012)](http://codeascraft.com/2012/05/22/blameless-postmortems/)

I have not seen these used much in practice, but I do like the idea. I am trying to send out post-mortems about tree-closing incidents involving the team I am managing. I have two more to do this week... 

* [How complex systems fail - video (2012)](https://www.youtube.com/watch?v=2S0k12uZR14)

This was heart-warming and reminded me of an old tool I wrote and [I tweeted briefly about it](https://twitter.com/tef/status/649423492140695552). I love the "trust your operations team" advice, and how we should be designing things so that we can trust more and restrict less.

* [How complex systems fail - pdf (1998)](http://web.mit.edu/2.75/resources/random/How%20Complex%20Systems%20Fail.pdf)

Great PDF summarizing some of the points that were made in the talk. And a reminder: "Post-accident attribution accident to a 'root cause' is fundamentally wrong."

* [Resilience in Complex Systems: Operating At The Edge Of Failures - video (2013)](https://www.youtube.com/watch?v=PGLYEDpNu60)

Great, simple model presented for visualizing the processes at work between human overwork, budget constraints and performance. Key learning is about the space between your margin of error and accidents -- that we are constantly pushing against that boundary.


* [Hopelessness and Confidence in Distributed Systems Design - video (2015)](https://www.youtube.com/watch?v=TlU1opuCXB0&feature=youtu.be&a)

"Build silence into systems" -- yes! Also a bae/Peter Bailis reference. Who btw is [looking for grad students](http://www.bailis.org/join.html)!

The big thing here -- relating back to the start of this binge -- is about designing your data. That is how you survive microservices.

* [Engineering for the long game - video (2015)](https://www.youtube.com/watch?v=p0jGmgIrf_M) 

A keynote from Astrid Atkinson. She talks about designing things so that engineers can manage their own systems. So great. "Keep in mind what is costing time." yup.  "If you talk to a server, timeout." "If you retry, exponentially backoff with jitter." "Systems should perform reasonably under degraded circumstances." "Somewhere between 1 and 5 identical services you're going to have to take a stand." "Strongly endorse boring infrastructure choices."

"It's not just enough to build it, you have to migrate existing workloads."

"Move the biggest customer first."

* [DynamoDB post-mortem (2015)](https://aws.amazon.com/message/5467D2/)

Super detailed, awesome post-mortem on the DynamoDB outage. Camille mentioned it in her Strange Loop talk.








