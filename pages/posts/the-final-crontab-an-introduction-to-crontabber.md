title: "The Final Crontab: an introduction to crontabber"
slug: the-final-crontab-an-introduction-to-crontabber
id: 5214
date: 2014-05-06 13:50:00
tags:
- socorro
- mozilla
- crontabber
categories:
- presentation

I gave a talk at [Monitorama][1] today about [crontabber][2]. ([slides][3])

<script async class="speakerdeck-embed" data-id="80588800b77601312dc72252d3db84f0" data-ratio="1.29456384323641" src="//speakerdeck.com/assets/embed.js"></script> 
My coworker tells me that I left out the part of "why you should care" about crontabber from my first few slides. So here's a list:

*   Retries jobs on failure automatically
*   Dependency-aware, and won't execute child jobs that depend on parents that have failed
*   Nagios integration including support for WARNINGs and CRITICALs, and configurable escalation from WARNING to CRITICAL (e.g. 3 WARNINGS == CRITICAL). 

Those three are probably the top features sysadmins who are not happy with how cron is managing jobs wish they had.

Crontabber needs at least Python 2.6, Postgres 9.2, is FOSS and being used in production. We've used a version of the code since February 2013, and currently have the python module version you can install with `pip install crontabber` is currently running in our stage environment.

Let us know what you think!

 [1]: http://monitorama.com
 [2]: http://github.com/mozilla/crontabber
 [3]: https://speakerdeck.com/selenamarie/the-final-crontab
