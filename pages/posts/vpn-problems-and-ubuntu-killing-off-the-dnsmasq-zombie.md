title: "VPN Problems and Ubuntu: killing off the dnsmasq zombie"
slug: vpn-problems-and-ubuntu-killing-off-the-dnsmasq-zombie
id: 5027
date: 2013-10-18 10:58:53
tags: 
categories: 
- linux

I've been having problems with VPN, DNS and Ubuntu for a year. But, I'm also pretty lazy when it comes to spending time on configuration. And configuring VPNs is like last on my list of ways I'd like to spend my time.

In short, I'd rather reboot than figure out exactly why my networking just stopped working.

[![REBOOT.](http://www.chesnok.com/daily/wp-content/uploads/2013/10/TurningitOffandOnAgain1.jpg)](http://www.chesnok.com/daily/wp-content/uploads/2013/10/TurningitOffandOnAgain1.jpg)

Fortunately, I had an easy (for me) work-around for most of my VPN needs: use SSH and a jump-host for getting to servers. I found it annoying when I wanted to look at a website on protected network space, or had a service on an unusual port that I wanted to test things against. I would work around with SSH tunnels, or I would fire up my Mac, whose VPN settings worked flawlessly.

That all said, I thought today, a sunny, lovely fall day in Portland, I would fix my VPN.

And so, my buddy @[uberj_](http://twitter.com/uberj_) helped me get things sorted.

The root cause of all my VPN heartache was the `dnsmasq` daemon controlling my DNS. And, related, `network-manager`. There are a few places that document exactly how to disable `dnsmasq`

*   DNS in Ubuntu 12.04 http://www.stgraber.org/2012/02/24/dns-in-ubuntu-12-04/
*   Disabling dnsmasq as your local DNS server in Ubuntu http://mark.orbum.net/2012/05/14/disabling-dnsmasq-as-your-local-dns-server-in-ubuntu/

However, they leave out one important step: killing off the existing dnsmasq process. For the unlucky, restarting `network-manager` does not kill off `dnsmasq`.

So, to find and kill dnsmasq, do the following:

     sudo service network-manager stop
     kill `ps -C dnsmasq -o pid=`
     sudo service network-manager start
    `</pre>

    Then, start your VPN and check out the contents of the `/etc/resolv.conf`. If all went well, you've got nameserver addresses other than `127.0.0.1` in the file.

    [![Yay!](http://www.chesnok.com/daily/wp-content/uploads/2013/10/7512696366_76be236667-300x226.jpg)](http://www.chesnok.com/daily/wp-content/uploads/2013/10/7512696366_76be236667.jpg)

    Sadly, this was not the end of my story.

    After a few minutes, NetworkManager started `dnsmasq` up again!

    [![Zombie dnsmasq](http://www.chesnok.com/daily/wp-content/uploads/2013/10/Animated-Zombie-Reverse.gif)](http://www.chesnok.com/daily/wp-content/uploads/2013/10/Animated-Zombie-Reverse.gif)

    So, like any reasonable sysadmin, I opened up the `/etc/NetworkManager/NetworkManager.conf` file, uncommented the `dns=dnsmasq` line, and replaced it with `dns=/dev/null`. My guess was that you can probably put just about anything other than dnsmasq into that line to permanently disable the plugin.

    I ran `sudo service network-manager restart`, checked `/etc/resolv.conf` and felt pretty smug.

    I tried also uninstalling `dnsmasq-base` package, but unfortunately that takes out a number of other packages I appear to need. So, I left /dev/null in my NetworkManager.conf, and updated this blog post.

    [![But wait...](http://www.chesnok.com/daily/wp-content/uploads/2013/10/h5AC86B91-300x225.jpeg)](http://www.chesnok.com/daily/wp-content/uploads/2013/10/h5AC86B91.jpeg)

    While editing this blog post, `dnsmasq` took over my DNS settings again.

    A clue as to what was happening was in `/var/log/syslog`:

    <pre>`Oct 18 10:20:10 localhost dnsmasq[30535]: started, version 2.59 cache disabled
    Oct 18 10:20:10 localhost dnsmasq[30535]: compile time options: IPv6 GNU-getopt DBus i18n DHCP TFTP conntrack IDN
    Oct 18 10:20:10 localhost dnsmasq[30535]: DBus support enabled: connected to system bus
    Oct 18 10:20:10 localhost dnsmasq[30535]: warning: no upstream servers configured
    `</pre>

    It turns out that `dnsmasq` was still getting revived by `NetworkManager`. Why NetworkManager doesn't seem to care about configuration settings was beyond my willingness to investigate today. So, I did some more searching about truly killing of dnsmasq for good.

    And I found [this thread](http://www.chesnok.com/daily/wp-content/uploads/2013/10/7512696366_76be236667.jpg), and [this sample configuration file](http://www.thekelleys.org.uk/dnsmasq/docs/dnsmasq.conf.example). In the output for the `dnsmasq` process from ps:

    <pre>`nobody   30777 30759  0 10:21 ?        00:00:00 /usr/sbin/dnsmasq --no-resolv --keep-in-foreground --no-hosts --bind-interfaces --pid-file=/var/run/sendsigs.omit.d/network-manager.dnsmasq.pid --listen-address=127.0.0.1 --conf-file=/var/run/nm-dns-dnsmasq.conf --cache-size=0 --proxy-dnssec --enable-dbus --conf-dir=/etc/NetworkManager/dnsmasq.d
    `</pre>

    I dug into the thread, and the suggestion was to set `port=0` in the config. I created a file called `custom` in `/etc/NetworkManager/dnsmasq.d`. And ran `sudo service network-manager restart`.

    And then I got this in my syslog:

    <pre>`Oct 18 10:21:10 localhost dnsmasq[30777]: started, version 2.59 DNS disabled

FINALLY.

[![FINALLY!](http://www.chesnok.com/daily/wp-content/uploads/2013/10/yes-finally-pl-ffffff-252x300.jpeg)](http://www.chesnok.com/daily/wp-content/uploads/2013/10/yes-finally-pl-ffffff.jpeg)
