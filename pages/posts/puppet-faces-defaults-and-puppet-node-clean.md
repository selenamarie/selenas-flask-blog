title: "Puppet Faces: defaults and 'puppet node clean'"
slug: puppet-faces-defaults-and-puppet-node-clean
id: 3468
date: 2011-11-02 17:55:41
tags: 
- puppet
- puppet faces
categories: 
- sysadmin

Puppet Faces are an extendable API for tricking out your Puppet instances. ("Faces" is just short for "Interfaces".) Just a couple days ago I wrote about [my survey of puppet + ec2 provisioning tools](http://www.chesnok.com/daily/2011/10/28/going-from-vagrant-and-puppet-into-ec2-a-short-survey-of-5-tools-and-two-i-didnt-bother-trying/).

The problem I'm trying to solve, which I don't feel like I've solved well, is how to give a type to a new system at bootstrap time, without using DNS. The type variable maps to a node manifest group, and determines the personality of a host - is it a database, webserver or development instance?
<!--more-->
What I'd like to do is pass a type to puppet at install time and have the puppetmaster and the agent remember that mapping between host and type. 

I did it with a really simple Facter plugin, install scripts named by type (passed in to `puppet node install`), and a file created by the install script in `/etc/puppet`.

Then, I wanted to be able to see which hosts were configured with which install type. Facter was aware of the type, so this seemed like it should be pretty easy...

I wrote a quick and dirty Face that pulls information out of `$varlib/nodes/*.yaml` on the puppet master. I imagine there are better ways to do this, but in the absence of documentation or someone to tell me not to do this, I forged ahead!

There were two things that I spent quite a bit of time chewing on before figuring it out: 

1.  If you want to make an `:action` in your Face the default, you just add `default` in the body of your `:action` block. I had to dig through a few cloudpack files before I found it!
2.  If you are creating and terminating hosts frequently, you may end up with a bunch of certs and other annoying metadata laying around. To clean it up, the Puppet Node Face has a command you can run: 
`
# puppet node clean [hostname]
`

You'll probably need to be the user that's running puppet for this to work -- it affects things that the puppetmaster owns in `$varlib`. 

If you're doing this with code, it's: 
`
Puppet::Face[:node, :current].clean('hostname')
`

I put [a little patch](https://github.com/selenamarie/puppetlabs-cloud-provisioner/commit/44e7300e1097d8a9290f864154ad591689feadc7) into a recent version of cloudprovisioner that invokes clean during a terminate. It's quick and dirty, and only for AWS. 

The resources I've found useful are: 

*   [Kelsey's talk at PuppetConf about Faces](http://www.youtube.com/watch?v=C9k9lF4cskg)
*   [Kelsey Hightower's Git repo for Puppet Dashboard Face](https://github.com/khightower/puppet-dashboard-face/)
*   [Kartar's Github face](http://www.kartar.net/2011/05/puppet-github-face/)

And to a lesser extent, these blog posts were helpful for filling in a few gaps: 

*   [What the heck are Faces?](http://puppetlabs.com/blog/puppet-faces-what-the-heck-are-faces/)
<li>[Creating a simple "backup" Face](http://puppetlabs.com/blog/about-faces-until-we-go-in-the-right-direction/)
