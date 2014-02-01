title: "PostgreSQL 9.0: contributions!"
id: 1997
date: 2010-09-21 07:29:23
tags: 
- code
- committers
- community
- contributions
- postgres
categories: 
- postgres
- postgresql

New releases are opportunities for reflection! 

As PostgreSQL grows, I would like to know how many people are contributing at any time. This is difficult to measure, given how many people contribute in ways not visible to the internet - advocating for PostgreSQL at work, sharing information about PostgreSQL offline in any way, or developing code related to PostgreSQL that isn't shared directly back.

PostgreSQL developers have a habit of mentioning the people involved in the development of features in the commit logs.  This includes people who discuss topics on the mailing list, who report bugs, provide test cases or send in patches. I spent a bit of time digging through the commit logs and pulling out unique names that are mentioned.  This is a lossy process, as the log files are long, names are not always easy to spot, and I only spent 6 hours going through it.

I've made it through the 9.0 (16163 lines of logs) and 8.4 logs (21257 lines of logs) so far. 

Here's some basic information about them: 

*   <font size="+2">8.4 logs mention about **230** unique people (11 committers)</font>
*   <font size="+2">9.0 logs mention about **275** unique people (16 committers)</font>
*   8.4 development contained 2293 commits with commits per author broken down below (click for a bigger version): 
[![](http://www.chesnok.com/daily/wp-content/uploads/2010/09/8.4commits-300x225.png "8.4commits")](http://www.chesnok.com/daily/wp-content/uploads/2010/09/8.4commits.png)

*   9.0 development contained 1703 commits, and the commits per author broken down below (click for a bigger version): 

[![](http://www.chesnok.com/daily/wp-content/uploads/2010/09/9.0-commits-300x207.png "9.0 commits")](http://www.chesnok.com/daily/wp-content/uploads/2010/09/9.0-commits.png)

I'm working on graphs about number of lines inserted or deleted by each author, but need more time to work out the information presentation. Some interesting trends emerge about what the role of each committer is - particularly that there are a couple people who seem to be "gardeners" of the code - removing a lot of lines, sometimes more than they are adding. With a project as old as ours (first commit in 1996!), this maintenance work is critical.

I also did some grepping for key words in the commit messages: 

<table border=1>
<tr><th>word</th><th>times mentioned
 in 8.3</th><th>times mentioned
 in 8.4</th><th>times mentioned
 in 9.0</th></tr>
<tr><td>review</td><td>24</td><td>14</td><td>49</td></tr>
<tr><td>cute</td><td>29</td><td>26</td><td>25</td></tr>
<tr><td>tom lane</td><td>904</td><td>901</td><td>635</td></tr>
<tr><td>gripe</td><td>37</td><td>48</td><td>26</td></tr>
<tr><td>hot standby</td><td>0</td><td>5</td><td>48</td></tr>
<tr><td>replication</td><td>18</td><td>4</td><td>52</td></tr>
</table>

You're welcome to explore our git repo at [git.postgresql.org](http://git.postgresql.org/gitweb?p=postgresql.git). Thanks to all the folks who worked on the git migration over the past few months, and finally made [our transition from CVS to git complete](http://blog.hagander.net/archives/175-PostgreSQL-now-on-git!.html) last night!
