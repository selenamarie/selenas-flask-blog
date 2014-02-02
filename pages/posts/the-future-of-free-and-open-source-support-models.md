title: "The future of free and open source support models"
slug: the-future-of-free-and-open-source-support-models
id: 872
date: 2009-04-25 06:07:59
tags: 
- assurance
- contracts
- foss
- postgres
- postgresql
- support models
categories: 
- community
- conference
- open source
- postgres
- postgresql

I attended the [MySQL Conference](www.mysqlconf.com) all last week, and am feeling very excited about the future of open source databases.  I had many interesting discussions and met a ton of Drizzle hackers I was lucky enough to spend Friday with, digging through code.

I was talking with [Paul Vallée](http://www.pythian.com/about/paul_vallee.php) of the Pythian Group Thursday about Postgres and the future of enterprise support. And he showed me this great graph from indeed.com.  It's acceleration here, not the raw numbers - but still, a neat graph :)

<div style="width:540px">
[
![postgres, mysql, oracle Job Trends graph](http://www.indeed.com/trendgraph/jobgraph.png?q=postgres%2C+mysql%2C+oracle&relative=1)
](http://www.indeed.com/jobtrends?q=postgres%2C+mysql%2C+oracle&relative=1&relative=1 "postgres, mysql, oracle Job Trends")
<table width="100%" cellpadding="6" cellspacing="0" border="0" style="font-size:80%"><tr>
<td>[postgres, mysql, oracle Job Trends](http://www.indeed.com/jobtrends?q=postgres%2C+mysql%2C+oracle&relative=1&relative=1)</td>
<td align="right">[postgres jobs](http://www.indeed.com/q-postgres-jobs.html) - [mysql jobs](http://www.indeed.com/q-mysql-jobs.html) - [oracle jobs](http://www.indeed.com/q-oracle-jobs.html)</td>
</tr></table>
</div>

We discussed the issues that enterprise customers with certain types of regulatory obligations encounter -- such as contractual obligations for PCI-compliant credit card storage or outsourced management of sensitive data. The standard response developers might give for this is "read the spec, and make sure you implement it properly". But the truth is, for larger companies, that may not be enough.

So, assuming for a moment that the Postgres community would even want to address this problem as a group -- could it be possible for the Postgres community to provide the legal and financial assurances that an incredibly huge corporation (ahem - Sun/Oracle) can?

The short answer for Postgres right now is "no".

Originally, I had thought just in term of liability, but Paul clarified:

> The liability is just one component of what gives the guarantee meaning because there is a consequence to failed delivery. An SLA can also do this. As can a simple lucrative contract that can be lost, or canceled early if delivery does no take place. The key here is to ensure that the technology adopter can legitimately be confident that they are provably being responsible by adopting the platform. "I trusted" doesn't cut it for many.

My view was that this type of agreement helps to determine who exactly is to blame (and who can be sued) in the event of a software failure. But, Paul said, "It's more about assurance (with evidence) that obligations realistically will be met."  

I sometimes think that this system of liability and assurances is just ultimately broken. But it is a reality. So, would it be possible for us to come up with a new legal framework for community-driven software?

Paul brought up the idea of a cooperative, and that maybe such a legal entity could provide protection for individuals involved in supporting Postgres, and also shoulder some or all of the liability that a corporation using Postgres would want.  I'm not sure that core developers of Postgres would join such a thing, or whether they would be allowed to given existing agreements they have with their own companies. But it is an interesting idea.

Creating a blueprint for this type of organization - hackers cooperatives - could be a way for truly community software to be developed across companies and among individuals in a sustainable, and "trustable" way. Maybe? 

Continuing this train of thought - maybe these are non-governmental organizations, whose main purpose is to create and maintain infrastructure software for the good of the world.

Funding for mid-sized free and open source projects seems to be a consistent problem. Perhaps NGOs are a fair model for us.

I am curious about what effort may have already been made in this direction.  My next step will be to contact Bradley Kuhn and see if there's something out there that might address this.
