title: "A mostly working Lenovo x230 running Ubuntu and Gnome3: Two weeks later"
id: 4501
date: 2012-11-13 19:18:47
tags: 
categories: 
- personal

I've been planning to switch to a Linux laptop for a while, either for work or as my own laptop aged out. So, [joining Mozilla](http://www.chesnok.com/daily/2012/09/22/wrapping-up-postgres-open-new-job-shift-away-from-twitter/) was the perfect opportunity to switch over.  And, I'm happy to report that I'm fully converted, enduring a few bugs that need some help, and seriously considering Gentoo to handle all the weird driver issues I've got.

Overall, I'm liking the new setup. It's easier to install all the developer stuff I need like new versions of Python or PostgreSQL. Having real package management instead of adhoc messy MESS of installers is an incredible relief.

I'm using Firefox for my primary browser instead of Chrome, which has made me realize how broken lots of websites I look at regularly are for most people. Also, I am exploring more plugins as a result.

My favorite feature in the Gnome window manager (and lots of window managers support this) is the ability to automatically snap windows to 1/2 or full size with the 'window' and arrow keys. It saves an incredible amount of time vs using a mouse to resize.

Unfortunately, I lost the epic rundown of all the problems I encountered on installation, as I encountered them. I can sum up with: the experience of desktop linux has significantly degraded in the seven or so years since I last tried to have a linux laptop as my primary workstation. Talking with friends about this has caused several to remark that Apple got it right with tightly controlling vendors and having full control over the hardware used with it's operating system. Without a real commitment from a vendor toward supporting drivers, the situation seems unlikely to improve. I think the strongest hope for this is [ZaReason](http://zareason.com/shop/home.php?cat=), but they weren't an option for my corporate laptop.

Here's a few tidbits that might be helpful to a future x230 owner, wanting to run Ubuntu:

I'm running 12.04, Precise Pangolin.

Installed from an Ubuntu netinstall image created with: [http://unetbootin.sourceforge.net/](http://unetbootin.sourceforge.net/).

Here are a bunch of `ppa`s I used, from my `/etc/apt/sources.d` directory: 
<pre>
deb http://ppa.launchpad.net/andreas-diesner/lightdm-fix-temporary/ubuntu precise main
deb-src http://ppa.launchpad.net/andreas-diesner/lightdm-fix-temporary/ubuntu precise main
deb http://ppa.launchpad.net/andreas-diesner/lightdm-fix-temporary/ubuntu precise main
deb-src http://ppa.launchpad.net/andreas-diesner/lightdm-fix-temporary/ubuntu precise main
deb http://linux.dropbox.com/ubuntu precise main
deb http://linux.dropbox.com/ubuntu precise main
deb http://ppa.launchpad.net/fkrull/deadsnakes/ubuntu precise main
deb-src http://ppa.launchpad.net/fkrull/deadsnakes/ubuntu precise main
deb http://ppa.launchpad.net/fkrull/deadsnakes/ubuntu precise main
deb-src http://ppa.launchpad.net/fkrull/deadsnakes/ubuntu precise main
### THIS FILE IS AUTOMATICALLY CONFIGURED ###
# You may comment out this entry, but any other modifications may be lost.
deb http://dl.google.com/linux/musicmanager/deb/ stable main
### THIS FILE IS AUTOMATICALLY CONFIGURED ###
# You may comment out this entry, but any other modifications may be lost.
deb http://dl.google.com/linux/musicmanager/deb/ stable main
deb http://ppa.launchpad.net/hannes-janetzek/enlightenment-svn/ubuntu precise main
deb-src http://ppa.launchpad.net/hannes-janetzek/enlightenment-svn/ubuntu precise main
deb http://ppa.launchpad.net/hannes-janetzek/enlightenment-svn/ubuntu precise main
deb-src http://ppa.launchpad.net/hannes-janetzek/enlightenment-svn/ubuntu precise main
deb http://ppa.launchpad.net/pitti/postgresql/ubuntu precise main
deb-src http://ppa.launchpad.net/pitti/postgresql/ubuntu precise main
deb http://ppa.launchpad.net/pitti/postgresql/ubuntu precise main
deb-src http://ppa.launchpad.net/pitti/postgresql/ubuntu precise main
deb http://ppa.launchpad.net/upubuntu-com/chat/ubuntu precise main
deb-src http://ppa.launchpad.net/upubuntu-com/chat/ubuntu precise main
deb http://ppa.launchpad.net/upubuntu-com/chat/ubuntu precise main
deb-src http://ppa.launchpad.net/upubuntu-com/chat/ubuntu precise main
</pre>

There's a painful lightdm problem fixed by a package the first source in the above list. 

I also compiled a new kernel for myself to try to fix a bad video flickering problem I'm having with my external monitor. Jury's out on that - the flickering hasn't entirely gone away, and it doesn't happen to my coworker who's got a x220 and is running Gentoo, but a different kernel. 

Also, my video camera doesn't work, and I actually need it. Skype seems to work ok for voice, but not video. Vidyo, however, doesn't work at all.

Wish list for the future: 

*   Camera working
*   A Skitch replacement
*   Vidyo working
*   A package for my .bash_profile, .ssh and .gpg directories that I can install in any new system
*   A better driver for the touchpad that doesn't let my mouse jump around while I'm typing (Yes, I have already enabled the feature, and it doesn't work so great. Friends suggested it might be a hardware limitation.)
*   Change configuration to have the mouse behave like the latest OS X (reverse scrolling)

Here's a few other sites that helped me out:

*   [Ubuntu on the Lenovo Thinkpad x230](http://syntaxionist.rogerhub.com/ubuntu-on-the-lenovo-thinkpad-x230.html)
*   [Slow boot problem bug and fix](https://bugs.launchpad.net/lightdm/+bug/866035) - this took me FOREVER to find

And, I don't recommend trying out Enlightenment as your only window manager on your first try. You'll need something else anyway to get your wireless configured, and if you do something stupid like trying to install 'econnman' and you blindly say 'yes' to uninstalling some packages you don't know anything about, you'll end up accidentally removing your wireless devices. So, start with Gnome, read up and switch to E later. 
