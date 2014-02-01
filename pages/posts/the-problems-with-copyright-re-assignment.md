title: "The problems with copyright re-assignment"
id: 2034
date: 2010-10-08 07:00:11
tags: 
- copyright
- foss
- licensing
- postgres
categories: 
- postgres
- postgresql

While I was in NYC ([eating awesome food](http://www.flickr.com/photos/selenamarie/5029666861/), riding my bike across the brooklyn bridge in the rain!), I spent time catching up with free software advocates. One issue that we talked about was [copyright assignment](http://producingoss.com/en/copyright-assignment.html). [H Online recently published](http://www.h-online.com/open/features/Copyright-assignment-Once-bitten-twice-shy-1049631.html) an article about this. Their description of the Linux kernel's policy pretty much matches PostgreSQL's policy: 

> Ownership of free software is a difficult area, and one that is resolved simply by the Linux kernel project. The code belongs to everyone and no-one, and the copyright for each individual piece of code belongs to the original coder, so that any future reassignment of the licence or the code for the Linux kernel requires the agreement of every other contributor.

I haven't contributed code to projects other than PostgreSQL in a long time, but an important aspect of contribution that I used to not think very much about is copyright assignment. Now that I have spent a little time thinking about it, my preference is to contribute to projects which do not require copyright re-assignment.

Copyright came up in a conversation about dual-licensing, because it is the copyright assignment which provides the opportunity for a codebase to be re-licensed. But more important to me than the possibility of re-licensing, is the chilling effect copyright re-assignment agreements have on communities. The intent can be to be to hedge a company's bets against contributor interference, and ultimately be able to assert complete control over a codebase. If we agree that the collaborative production of software is a social good, this type of hedging can only be seen as anti-social, and ultimately, destructive to a software community. In practice, I've seen projects which require contributor agreements effectively shun all non-corporate contributions, or actively engage in "[ornamental sourcing](http://twitter.com/#!/thesethings/status/26609256654)".

For a business owner who invests in free and open source software, this is an unsustainable position. The advantage of accessing source code is not just the code, but the **people** who know the code. And while I'm sure there are some exceptions, I doubt most people consider themselves experts in a codebase without having contributed significant patches to it. 

Given all that, [copyright assignment to the Free Software Foundation](http://ebb.org/bkuhn/blog/2010/02/01/copyright-not-all-equal.html) or [to Canonical](http://itmanagement.earthweb.com/osrc/article.php/3904526/Ubuntu-Canonical-Wallow-in-Muddy-Waters-with-Contributors-Agreements.htm) has been a contentious issue. But maybe if you have an organization which is committed in its charter to maintaining software freedom, then the copyright assignment serves a social good and gives an organization like the FSF the legal authority to pursue legal action if the terms of a license are violated.
