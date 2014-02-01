title: "Why give credit to reviewers?"
id: 4884
date: 2013-06-26 15:29:22
tags: 
- code review
- postgresql
categories: 
- postgresql

_This is a lightly edited version of an email I sent to pgsql-hackers today._

Josh Berkus asked:

**> How should reviewers get credited in the release notes?**

Without getting into how the community might decide to do this, I thought it might be helpful to share the reasons why I believe recognizing and expressing gratitude to reviewers is a helpful, useful and gratifying exercise for the Postgres community.

I support crediting reviewers in a more formal way than we currently do for a few different reasons.

First, I believe it's worth finding a way to say "Hey, you just did something great for Postgres", publicly, to a bunch of people who could have spent their valuable time and energy in some other way.

Second, reviewers get better at their work by reviewing multiple times - so I'd like to encourage people to review more than once.

Third, reviewers don't always need to be expert developers, or experts at Postgres to get started, but many people who do open source work have no idea this is true. Public recognition helps make it clear that we have people who give useful reviews and are relative novices.

We also have several different kinds of reviews:

*   "does it compile"
*   style/typo/easily seen bug passes
*   in-depth discussion of design choices, use case, interface
*   complex testing cases
*   performance testing
*   pre-commit checks for more subtle bugs or committer preferences.

All of those, except probably the very last, can be done by people who are familiar with Postgres or its configuration, but aren't necessarily Postgres or C experts.

Fourth, we have very few accepted ways to recognize contributions to Postgres. Naming in Release Notes is one way this community has consistently supported as a _public_ way to say "hey, you just did something great for Postgres". The complete list of ways I'm aware of are:

1.  Recognizing major, minor and emeritus contributors
2.  Making someone a committer
3.  Being part of the -core group
4.  Naming authors by name in commit messages (but without consistent metadata, making it difficult to count well)
5.  Naming authors in release notes

That's pretty much it. That's great for the people who have already secured positions through seniority, or because they're amazing C hackers. I don't know if I need to lay out for everyone the value of public recognition - if you want me to I can enumerate them. But the benefits of public recognition are huge -- both in a social and a financial sense.

Currently, the only way I know of to be recognized for work on Postgres that is _not_ seniority or code-related is #1\. If you're a reviewer, there's almost no chance you'll be recognized in our list of contributors without some additional, very significant contribution to our community. (Please let me know if I'm mistaken about this -- I only know what I know!) Adding names to Release Notes (or some variant of Release Notes) seems like a minor concession for work that we as a community need, value and want to encourage.

We are so few in terms of patch contributors - somewhere between 300-400 people contribute code to PostgreSQL each year based on the names I try to pull out of commits. I haven't counted how many reviewers we have who do not also contribute patches separately.

Giving people appreciation for the review work they're doing, for free, is a good thing for everyone. Naming more names helps describe the true scope of our community. Spreading gratitude is good for those who thank and those who receive thanks (like, proven scientifically!). And we increase the number of people who benefit directly from the work that they do here, by giving them something they can point their boss, their company and their colleagues to.

So, when we're debating _how_ recognition might be done, please don't lose sight of _why_ this is important in the first place.
