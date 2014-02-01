title: "Online aggregation paper from 1997 and PSU's database reading group"
id: 1889
date: 2010-08-28 15:03:36
tags: 
- aggregates
- online
- parallelization
- postgres
- research
categories: 
- portland
- postgres
- postgresql

A couple weeks ago, Mark Wong and I took a field trip over to the Database Reading Group at Portland State University. It's a group of students and professors that meet weekly throughout the school year to go over research papers. The papers are picked by the participants, and vary in topic from obscure to very practical.

This week's paper reading was led by Professor Len Shapiro, and titled "[Online Aggregation](http://research.microsoft.com/en-us/um/people/helenw/papers/online.ps.gz)". The paper is considered a foundational paper about SQL aggregates (like COUNT() or AVERAGE), and was published in 1997 by researchers from UC Berkeley and IBM. It's also precursor to research into query parallelization and streaming databases. It was also awarded the SIGMOD "Test of Time" award in 2007, and is cited by over 170 other papers in the ACM archive.

The basic idea behind the paper centered around how to improve user experience in reporting results of aggregate queries - asking questions about how to solve three key problems when solving aggregates: blocking, fairness and control (from a user's perspective). Roughly: Blocking is what happens when some part of the system waits and doesn't return results to the user as a result of the waiting. Fairness concerns whether certain types of operations prevent certain groups of data from being processed (the example given had to do with GROUP BY and groups being processed one at a time). Control concerns whether or not a user can exert control over the speed of computation applied to a group (example given being a lever that "speeds up" processing of a set).

One insight from the paper is how online aggregates should be treated differently than traditional query processing - which might favor expensive plans involving sorts so that the output is ordered. When you're dealing with online aggregates, you prefer unordered, or ideally random order, because your intermediate results will be more representative of the ultimate result. I guess that's probably obvious once you think about it, but the paper provided some concrete examples.

Another interesting thought experiment involving the planner is how you pick plans that favor non-blocking, fairness and user control. Each of those properties is not narrowly defined, and changes based on individual user expectation. Professor Kristen Tufte mentioned that she'd be interested in how the ideas presented in this paper would be applied today, and Professor David Meier brought up that we might most be interested in applications involving managing Hadoop.

Prof Meier also brought up an interesting paper involving [alternating nested loop joins](http://db.cs.berkeley.edu/papers/S2K-94-45.pdf) during a discussion about optimizing JOIN algorithms for online aggregates. Another cool thing about the paper is that it involved modifications to Postgres!  Granted, it was Postgres95, which doesn't resemble the modern PostgreSQL 9.0 very much. But it was nice to revisit research that used Postgres that's still relevant today.
