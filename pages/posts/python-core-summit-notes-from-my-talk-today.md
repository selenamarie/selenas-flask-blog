title: "Python Core Summit: notes from my talk today"
slug: python-core-summit-notes-from-my-talk-today
id: 5188
date: 2014-04-09 12:03:00
tags:
- core summit
- education
category:
- python

I gave a short talk today about new coders and contributors to developer documentation today. Here are my notes!

Me: Selena Deckelmann Data Architect, Mozilla Major contributor to PostgreSQL, PyLadies organizer in Portland, OR

Focusing on Documentation, Teaching and Outreach

Two main forks of thought around teaching and outreach: 1. Brand new coders: PyLadies, Software Carpentry and University are the main communities represented 2. New contributors to Python & ecosystem

**1\. Brand new coders: PyLadies, Software Carpentry and University are the main communities represented**

(a) *Information architecture of the website*

Where do you go if you are a teacher or want to teach a workshop? Totally unclear on python.org. Really could use a section on the website for this, microsite.

Version 2 vs 3 is very confusing for new developers. Most workshops default to 2, some workshops now require 3. Maybe mark clearly on all workshops which version. Generally this is a very confusing issue when encountering the site for the first time.

Possible solution: Completely separate "brand new coder" tutorial. Jessica McKellar would like to write this.

(b) *Packaging and Installation problems* -- see earlier long conversation in this meeting about this. Many problems linked to having to compile C code while installing with pip

(c) *New coder contribution can come through documenting of issues around install and setup.* We could make this easier -- maybe direct initial reports to stack overflow, and then float solutions to bugs.python.org

**2\. New contributors to Python & ecosystem -- with a focus on things useful for keeping documentation and tutorials up-to-date and relevant**

(a) *GNOME Outreach Program for Women* - [Python is participating][1]!

More people from core should participate as mentors! PSF is funding 2-3 students this cycle, Twisted has participated for a while and had a great experience. This program is great because:

*   Supports code and non-code contribution
*   Developer community seems very cohesive, participants seem to join communities and stick around
*   Strong diversity support
*   Participants don't have to be students
*   Participants are paid for 3 months
*   Participants come from geographically diverse communities
*   To participate, applicants must submit a patch or provide some other pre-defined contribution before their application is even accepted

Jessica McKellar and Lynn Root are mentors for Python itself. See them for more details about this round! Selena is a coordinator and former mentor for Mozilla's participation and also available to answer questions.

(b) *[Write the Docs conference][2]* is a python-inspired community around documentation.

(c) *Openstack - [Anne Gentle & her blog][3].* 3-year participant in OpenStack community and great resource for information about building technical documentation community.

(d) *Better tooling for contribution could be a great vector for getting new contributors*.

*   Wiki is a place for information to go and die (no clear owners, neglected SEO etc) - Maybe separate documentation repos from core code repos for *tutorials* 
*   carefully consider the approval process - put the people who are most dedicated to maintaining the tutorials in charge of maintaining them

(e) *[bugs.python.org][4]*

Type selection is not relevant to 'documentation' errors/fixes. Either remove 'type' from the UI or provide relevant types. I recommend removing 'type' as a required (or implied required) form field when entering a bug.

The larger issue here is around how we design for contribution of docs:

*   What language do we use in our input systems? 
*   What workflow do we expect technical writers to follow to get their contributions included? 
*   What is the approval process?

Also see the "tooling for contribution"

 [1]: https://wiki.python.org/moin/OPW/2014
 [2]: http://conf.writethedocs.org/
 [3]: http://justwriteclick.com/
 [4]: http://bugs.python.org
