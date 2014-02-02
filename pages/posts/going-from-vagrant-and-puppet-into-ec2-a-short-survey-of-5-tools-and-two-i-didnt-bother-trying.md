title: "Going from Vagrant and Puppet into EC2: A short survey of 5 tools (and two I didn't bother trying)"
slug: going-from-vagrant-and-puppet-into-ec2-a-short-survey-of-5-tools-and-two-i-didnt-bother-trying
id: 3420
date: 2011-10-28 18:21:58
tags: 
- bootstrap
- deployment
- devops
- ec2
- provisioning
- puppet
- tools
- vagrant
categories: 
- sysadmin

I thought this would be easy. 

I started using [Vagrant](http://vagrantup.com/docs/getting-started/index.html), and was productive with it in about a day. Really a couple hours. Most of my time was spent downloading the correct version of VirtualBox, [looking for starter images](http://morethanseven.net/2011/05/08/Vagrant-plugin-for-interacting-with-vagrantboxes.html) and then a small amount of time experimenting with the Vagrantfile scripting language ([for multiple VMs](http://vagrantup.com/docs/multivm.html)).

And we made some Puppet configs.
<!--more-->
Then I wanted to use those same Puppet configs with EC2.

So my ultimate goals were: 

1.  Reuse my existing puppet configs as much as possible
2.  Have a completely automated deploy of a server system (including checkouts of code from a private github repo)
3.  Have a puppetmaster in EC2
4.  Be able to provision systems from EC2 or my laptop
5.  Make the whole process easy for my coworkers

This is mostly a list of what I failed at using, and the thing I succeed with at the end.

_Short aside:_

**Pro tip to people writing documentation**: Most tutorials and sites that make recommendations for tools leave out the part where you run into all kinds of insane problems. **Create a wiki page or a place where you collect the problems.** Please. 

For example: My Cloud Formation to Ubuntu AMI deploy was failing with an error in cfn.rb that said: "Unexpected return."  Um. Ok. *facepalm*

The problem was that a AWS-image specific JSON file wasn't present (and couldn't be created) on the target machine. So instead of noting (raise an exception, anyone?) that the file wasn't present, the module just executed a bare `return`. 

Because I don't know much about Puppet internals, this was a very annoying problem to solve. (like, what gets installed in `/var/lib/puppet/lib` vs. in the `gem install` vs. the cloudpack library I was told to install in `/etc/puppet/modules`?)

Stepping back a bit - a useful note from the Cloud Formation folks would have been: "Hey - this probably won't work if you try to deploy to non-Amazon Linux AMI distros of Linux." It's not obvious that's the case! You're supposed to be able to completely control the classes being installed on the target system, right? Bad assumption, apparently.

_And we're back!_

Let me know in the comments if you've successfully navigated any of the tools I didn't pick. Juju, in particular, I don't think I gave a fair chance (since I didn't try it at all). 

Here's my list: 

1.  [Juju](http://www.slideshare.net/derleiermann/juju-puppetconf)

I just wasn't sure this was a reasonable thing to install/use. No one I knew had ever heard of it. Didn't try it. 

2.  [Mcollective + tools ported to PHP](http://www.devco.net/archives/2010/07/14/bootstrapping_puppet_on_ec2_with_mcollective.php)

I'm interested in Mcollective, but the configs looked overly complex, and I didn't have anyone close by that was actively using it. 

The examples scared me away because of the PHP. I already had three languages at play in the deployment, and I didn't need another language dependency. So, I didn't bother trying it.

3.  [Custom scripts based on the ec2-tools packages](http://www.codelord.net/2010/12/19/using-puppet-to-automatically-configure-new-ec2-instances/)

This approach works, but is fragile and a PITA to keep updated. I tried it as a "getting oriented" exercise, and abandoned it.

4.  [Mccloud](https://github.com/jedi4ever/mccloud)

This looked awesome! I could reuse all my Vagrant configs and not really have to change anything... Except I had to maintain duplicate configs, just sub 'Mccloud'. Eh. 

I may revisit this tool in the future, but it seemed to require pretty much the same things as the tool I ultimately decided to use, and didn't seem as flexible. I also had a weird restriction where it wouldn't allow me to spin up the correct type of image (I wanted m1.small in my testing). Could have been PEBKAC -- I didn't take good enough notes to say for sure.

5.  [cloud-init](https://help.ubuntu.com/community/CloudInit)

This looked very promising! We were already using Ubuntu so seemed like a good fit. 

Pros: easy - pass in a shell script when starting an EC2 instance from the web. Cons: required yet-another-configuration style. But there were command-line tools and it was looking very promising.

In the end, using a supported package would have required me to be running a Linux desktop to start my puppetmaster. I didn't search much harder than `brew install cloud-init` for a Mac-equivalent (that doesn't exist). So, I moved on to the next thing.

6.  [AWS Cloud Formation](http://aws.amazon.com/cloudformation/)

I launched a puppetmaster pre-configured instance! I sort of got puppetmaster running! Then I tried to deploy an Ubuntu AMI from it... This does not work. 

So, I will save you a ton of time: **Avoid trying to mix the pre-specified Cloud Formation images with other systems.**

Someone showed me the chunk of the config you can rip out and probably get it to work. I was frustrated at that point, and moved on. Too much tweaking was required, for what was uncertain gain at that point. 

7.  [PuppetLab's Cloud Provisioner](https://github.com/puppetlabs/puppetlabs-cloud-provisioner)

This is what I am currently using! I'm running `HEAD` pulled directly from github.  Older versions are not recommended. (I tried three versions.)

The configuration is pretty straightforward and [documented](http://docs.puppetlabs.com/guides/cloud_pack_getting_started.html). The one thing (a very important thing) is that you have to amend your `$RUBYLIB` if you don't install the code in your version of ruby's default libdir. There's no gem. [Yet](http://projects.puppetlabs.com/issues/10379). 

I customized the deploy script to my liking - there is an unsupported option called `--install-script` you can pass in that will execute whatever `.erb` (a shell script!) you'd like if you put it in `~/.puppet/scripts`. You can also pass in your puppetmaster hostname with `--server`.

Totally sweet. 

The command-line is ok, but there's also a programmatic interface in Ruby. Dan Bode showed me a short code snippet that worked (hostnames & keys sanitized): 

`
irb(main):012:0> require 'puppet'
irb(main):013:0> require 'puppet/face'
irb(main):014:0> Puppet::Face[:node, :current].install('myserver.compute-1.amazonaws.com', :keyfile => 'mykey.pem', :login => 'ubuntu', :install_script => 'custom-puppetmaster', :server=>'myserver.compute-1.amazonaws.com')
`

I so appreciate this! [Faces](http://puppetlabs.com/faces/) is awesome.

I've got some additional tweaking to do yet, but I'm planning to commit a few amendments to the provisioner scripts included by default and the README. And I filed a couple bugs. 

Overall, I'd bet that [cloud-provisioner](https://github.com/puppetlabs/puppetlabs-cloud-provisioner) (if you use the version currently on github) will work for most people. 
