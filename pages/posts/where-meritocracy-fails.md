title: "Where meritocracy fails"
id: 2774
date: 2011-03-30 18:28:49
tags: 
- meritocracy
- postgres
categories: 
- postgres
- postgresql

Robert wrote about [patches and rejection](http://rhaas.blogspot.com/2011/03/welcoming-community.html) today, and quoted me from some tweets I made [about meritocracy](https://twitter.com/#%21/selenamarie/status/50586220211867648). I think Robert made some good points in his post, and I'm going to make some suggestions about patch review. 

But first, I want to address my [irritation about meritocracy](https://twitter.com/#!/selenamarie/status/50586869171367936)...

The first thing that I'll say is that I'm not sure exactly what people mean when they mention meritocracy. A [definition](http://en.wikipedia.org/wiki/Meritocracy) of it is "Meritocracy...is a system of government or other administration (such as business administration) wherein appointments are made and responsibilities assigned to individuals based upon their "merits", namely intelligence, credentials, and education, determined through evaluations or examinations."

My assuption was that Ed was saying, "Postgres is awesome because our community is meritocratic." I don't believe that's our strongest value, or quality as a community. And, it's not something that I think embodies what is awesome about Postgres.

**Our strongest quality is our ability to create great code.** 

We consistently produce readable, reliable and robust code amongst geographically diverse people who have very strong, divergent opinions about a great many things. We find common ground in the production of database software between people who are rhetorically violent even in agreement.

The code quality arises from a **commitment by Postgres hackers to discuss in public decisions that many developers prefer to make in private**. We are committed to a kind of radical transparency about our code that, at least in our shared Postgres myth, is embodied in Tom Lane's example. He overwhelmingly gifts to us his time and passion, in the form of methodical reviews of code. And that's not to say that our reviews are perfect in tone or fact, but just that we consistently do them.

When I think about our review process as it has evolved through Commitfest, it seems so undeniably humane and personal. I know at the same time that **it's still frightening**... Just last week a developer talked to me about how much he feared someone tearing into *him* and his code, picking apart decisions he'd made and the bits he knew needed more work. Anyone who shares a creative work knows how this feels - whether it's a painting, poetry, music or code.

But I don't think that commitfest or the direct reviews fellow hackers still provide to each other, produced a meritocracy. And I don't think that we should pursue meritocratic organization much more than we already have. 

What we have is something that largely works, and produces a product we feel good about endorsing and improving. There are elements of "promotion through merit". We pay closer attention now to giving commit access to people who it seems really ought to have it. And we recognize individual efforts where it is appropriate in our commit logs - something many projects fail to do.

At the same time, the operation of the project is dominated by people who fit into a very specific profile. And that's something like: 

*   the top 1% of the world in terms of salary, 

*   are male,

*   had parents that were mostly successful (aren't in jail for violent offenses for example), and 

*   either don't have kids, or have a partner or paid helper that does most of the childcare during the work day.

I count myself among you, with the exception that I'm not male, and I don't have kids. But I guarantee you that if I did have kids, either my partner would provide the bulk of childcare during the work day, or we would pay someone to do it for us. 

I bring this up because **in a truly meritocratic organization, privilege wouldn't matter**. Anyone could join us. But the truth is, not everyone can join the Postgres project. And that's why bringing up the myth, and applying it to an organization I contribute to annoys me.

I try to think regularly about my own privilege, and the place of open source software like Postgres in the world. I consider how to contribute to an organization that is not only is excellent in terms of what it produces, but is also something to be proud of because of the way that people treat and care for each other.

So, **I don't think more, or purer meritocracy helps us have better relationships or treat people well**.

We are still small enough at our core (somewhere around 300 people at any point in time), that we can operate like the best businesses do. We rely on good relationships between small groups who tend to appoint leaders to communicate between teams. Our teams seem to often be pairs, or small businesses, which fits our project's need for deep understanding of each feature.

But apart from the practicality of avoiding further pursuit of meritocracy, I don't believe that it helps us with talents that we need as a project now.  What matters is not that someone is the best at something, but that they have the time to put some effort in, which will then motivate others. That someone out there has a few minutes to write a review, file a bug report or fix a typo on our websites.

What we have to do is **create structures that invite people to give what they can, when they can give it**. This is what we enable with our extensive comments and thorough documentation. We probably could use someone with Tom Lane's singular attention and time to our web site, but I think we could make better use of 10 people who could devote a fraction of that time, consistently and with good humor.

So, ending the pursuit of a mythical meritocracy doesn't mean that we start accepting code which doesn't meet high standards, or that all of the sudden we're going to include more code from people in the bottom 1% of the world in terms of salary. It means that we take a look at different aspects of our project and see what is within our means to open up and make accessible to people who aren't exactly like us.
