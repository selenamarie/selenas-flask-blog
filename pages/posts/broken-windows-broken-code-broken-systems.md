title: "Broken windows, broken code, broken systems"
id: 2601
date: 2011-03-02 08:49:09
tags: 
- broken windows
- devops
- postgres
- sysadmin
categories: 
- devops
- postgres
- postgresql

A few days ago, I asked: 

[![](http://www.chesnok.com/daily/wp-content/uploads/2011/03/Twitter-_-@Selena-Deckelmann_-Is-there-a-_broken-window_-...-300x116.png "Twitter _ @Selena Deckelmann_ Is there a _broken window_ ...")](http://www.chesnok.com/daily/wp-content/uploads/2011/03/Twitter-_-@Selena-Deckelmann_-Is-there-a-_broken-window_-....png)

I spend a lot of time thinking about the little details in systems - like the number of ephemeral ports consumed, number of open file descriptors and per-process memory utilization over time. Small changes across 50 machines can add up to a large overall change in performance. 

And then, today, I saw [this article](http://infoworld.com/print/152375): 

> One of the more telling comments I received was the idea that since the advent of virtualization, there's no point in trying to fix anything anymore. If a weird error pops up, just redeploy the original template and toss the old VM on the scrap heap. Similar ideas revolved around re-imaging laptops and desktops rather than fixing the problem. OK. Full stop. A laptop or desktop is most certainly not a server, and servers should not be treated that way. But even that's not the full reality of the situation.> 
> 
> I'm starting to think that current server virtualization technologies are contributing to the decline of real server administration skills.

There definitely has been a shift - "real server administration skills" are now more about packaging, software selection and managing dramatic shifts in utilization. It's less important know to know exactly how to manage M4 with sendmail, and more important that you know you should probably use postfix instead. I don't spend much time convincing clients that they need connection pooling; I debug the connection pooler that was chosen.

The available software for web development and operations is quite broad - the version of Linux you select, whether you are vendor supported or not, and the volume of open source tools to support applications. 

Inevitably, the industry has shifted to configuration management, rather than configuration. And, honestly, the shift started about 15 years ago with [cfengine](http://cfengine.com/pages/history).

Now we call this [DevOps](http://www.kitchensoap.com/2009/12/12/devops-cooperation-doesnt-just-happen-with-deployment/), the idea that systems management should be programmable. Burgess called this "Computer Immunology". DevOps is a much better marketing term, but I think the core ideas remain the same: Make programmatic interfaces to manage systems and automate.

But, back to the broken window thing! I did some searching for development and broken windows and found that in 2007, a developer [talked about Broken Window Theory](http://www.simonfl.com/2007/11/broken-windows-theory-for-software.html): 

> People are reluctant to break something that works, but not so much when it doesn't. If the build is already broken, then people won't spend much time making sure their change doesn't break it (well, break it further). But if the build is pristine green, then they will be very careful about it.

In 2005, Jeff Atwood [mentioned](http://www.codinghorror.com/blog/2005/06/the-broken-window-theory.html) the [original source](http://www.codinghorror.com/blog/files/Atlantic%20Monthly%20-%20Broken%20Windows.htm), and said "Maybe we should be sweating the small stuff." 

That stuck with me because I admit that I focus on the little details first. I try to fix and automate where I can, but for political or practical reasons, I often am unable to make the comprehensive system changes I'd like to see.

So, given that most of us live in the real world where some things are just left undone, where do we draw the line? What do we consider a bit of acceptable street litter, and what do we consider a broken window? When is it ok to just reboot the system, and when do you really need to figure out exactly what went wrong?

This decision making process is often the difference between a productive work day, and one filled with frustration.

The strategies that we use to make this choice are probably the most important aspects of system administration and devops today. There, of course, is never a single right answer for every business. But I'm sure there are some themes. 

For example:

*   My boss wrote about [PEP8 and standards in formatting code](http://tech.myemma.com/python-pep8-git-hooks/), and automating this with a githook.
*   PostgreSQL code [goes through a reformatting pass](http://git.postgresql.org/gitweb?p=postgresql.git&a=search&h=HEAD&st=commit&s=pgindent) before we release.
*   Etsy [tracks their PHP warnings](http://codeascraft.etsy.com/2010/12/08/track-every-release/) for every release

James posted "[Rules for Infrastructure](http://www.kartar.net/2010/03/james-whites-rules-for-infrastructure/)" just the other day, which is a repost of the [original gist](https://gist.github.com/161265). What I like about this is that they are phrased philosophically: here are the lines in the sand, and the definitions that we're all going to agree to. 

Where do you draw the line? And how do you communicate to your colleagues where the line is?
