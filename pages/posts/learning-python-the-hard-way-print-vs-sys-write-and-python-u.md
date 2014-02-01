title: "Learning python the hard way: print vs sys.write, and python -u"
id: 2724
date: 2011-03-20 14:54:51
tags: 
- print
- python
- python -u
- sys.write
categories: 
- python

I knew before that print in Python had some weird properties. Like: 

> `> 
> 
> >>> for i in [1, 2, 3, 4]:> 
> ...     print "blah"> 
> ... > 
> blah> 
> blah> 
> blah> 
> blah> 
> >>> for i in [1, 2, 3, 4]:> 
> ...     print "blah",> 
> ... > 
> blah blah blah blah> 
> `

One thing you'll notice is that there's a space between each of the blahs. If you don't want those spaces, you need to use sys.write. [Here's an example of using sys.write](http://code.activestate.com/recipes/576986-progress-bar-for-console-programs-as-iterator/) along with a progress bar indicator.  Which is exactly what I wanted this for. 

Finally, you can indicate to [python on the command-line that you want unbuffered stdin and stdout](http://docs.python.org/using/cmdline.html#cmdoption-unittest-discover-u) with `python -u`.
