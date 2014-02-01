title: "Training lessons learned: Code dojo, whiteboards, interactivity "
id: 1684
date: 2010-10-07 07:00:03
tags: 
- code
- conferences
- nigeria
- postgres
- training
categories: 
- conference
- postgres
- postgresql

Training can be an incredibly boring, frustrating exercise. Often, I have friends who don't bother to attend sessions or tutorials during conferences. Instead, they cherry-pick friends and colleagues that they can work on code, gossip or brainstorm with in the hall while others sit passively in lectures. When I think about it now, knowing this about my friends is what motivated me to start [Open Source Bridge](http://opensourcebridge.org).

The [PostgreSQL training I gave to Ondo State](http://blog.endpoint.com/2009/07/nigeria-postgresql-training-day-1.html) was specifically targeted at developers. I used material [End Point](http://endpoint.com) had from previous trainings, and added few new things designed to meet the needs of fledgling database developers. The high points I wanted to hit were: schema design basics, user defined function development and highlight developer-friendly features of Postgres that they should be aware of.

One big obstacle for me was that they would all be using Windows as their primary operating system. I develop exclusively on UNIX-based platforms, and so I had to spend a little time getting re-acquainted with Windows tools. pgAdmin III was essential, and I was happy that a new version was released along with version 8.4 of Postgres.

Also, while the concepts are the same, the built-in monitoring tools for Windows are quite a bit different, and I used freely available material from my Postgres colleagues who support Windows for a couple hour tutorial on interactive troubleshooting.

When trying to explain concepts - like replication, or basic database terms - it really helps to have a whiteboard. I was working with a group of people with diverse IT backgrounds, and often, I asked individuals to try to explain in their own words various terms (like "transaction"). This helped engage the students in a way that simply stating definitions can't. Observing their fellow students struggling with terminology helped them generate their own questions, and I saw the great results the next day - when students were able to define terms immediately, that took five minutes the day before to work through.

Finally, one important request from the client was that some time be spent mentoring developers on standards, best practices for development and coding style. To accomplish this task with fourteen students in such a limited period of time, I decided to conduct a series of coding sessions where students and I took turns at the keyboard programming as a group. We call this [coding dojo](http://wiki.agilefinland.com/?CodingDojo), a concept built on the [Coding Katas](http://codekata.pragprog.com/2007/01/code_kata_backg.html#more) from Dave Thomas.

Overall, I prefer interactive training, where students are not only encouraged, but forced to interact with each other and the instructor.

When I sent out the [CFP for MySQL Conf](http://en.oreilly.com/mysql2011/public/cfp/126) yesterday, lots of people asked me for suggestions on talk topics. In general, I recommend that speakers focus on a particular take-away for the audience, and mention specifically what a person sitting in is going to learn *and* apply immediately. Not every talk can be interactive, or give people chunks of code. But *every* talk should have a clear goal, and leave the audience educated. The best leave them inspired!
