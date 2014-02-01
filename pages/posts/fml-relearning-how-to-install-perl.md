title: "#fml: Relearning how to install perl"
id: 3295
date: 2011-08-15 14:23:14
tags: 
- building
- pain
- perl
categories: 
- perl

I am working on a little project that requires a bit of perl and some database modules. I'm running Leopard, which ships with Perl 5.8.8\.  That kinda sucks.

So, I tried to work with a binary installer. Which was, for a number of reasons, a failure. 

Given my recent experience with virtualenv and Python, I started looking into what's the state of the art in this area for Perl.

The suggestion from the Perl home page is "perlbrew".  I took it for a spin.

> ` tar zxvf App-perlbrew-0.28.tar.gz> 
> ...> 
> 
> selena@lulu:Downloads #553 14:12 :( cd App-perlbrew-0.28> 
> selena@lulu:App-perlbrew-0.28 #554 14:12 :) perl Makefile.PL > 
> 
> Checking if your kit is complete...> 
> Looks good> 
> Warning: prerequisite Devel::PatchPerl 0.26 not found.> 
> Warning: prerequisite File::Path::Tiny 0 not found.> 
> Warning: prerequisite IO::All 0 not found.> 
> Warning: prerequisite Path::Class 0 not found.> 
> Warning: prerequisite Test::Output 0 not found.> 
> Warning: prerequisite Test::Spec 0 not found.> 
> Writing Makefile for App::perlbrew> 
>  `

Hmmm... So I tried to use cpanm to get it going: 

> `> 
> selena@lulu:App-perlbrew-0.28 #557 14:13 :( sudo cpanm App::perlbrew> 
> ...> 
> Building and testing App-perlbrew-0.28 for App::perlbrew ... FAIL> 
> ! Installing App::perlbrew failed. See /Users/selena/.cpanm/build.log for details.> 
> `

:(

So I asked a friend.  Who pointed me at [his build script](https://github.com/theory/my-cap/blob/master/bin/perl.sh). And, at least for this project, that's what I'm going to use.

Is perlbrew what most folks use for this type of thing? Is there some other virtualenv equivalent out there? 
