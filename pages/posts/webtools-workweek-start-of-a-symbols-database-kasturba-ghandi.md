title: "WebTools workweek, start of a symbols database, Kasturba Ghandi"
id: 4646
date: 2013-02-09 18:49:44
tags: 
categories: 
- personal

I came across a comment from [Sumana](https://www.mediawiki.org/wiki/User:Sumanah) saying that she'd like to hear more about the day-to-day life of our fellow FLOSS women. So here's a run-down of my past week:

## Mozilla WebTools team workweek

Mozilla teams hold work weeks from time to time - to get the team together, to experiment with new ideas and in our case, to meet up with a couple other teams (Marketplace and AMO, plus a couple extra folks we work a lot online with, but don't see very often). I did my normal nerd-out things like making a spreadsheet of all the names and silly intro comments people made on the first day, and I setup and deployed backup scripts to a new 5TB backup server that's just for crash-stats.mozilla.com's PostgreSQL database. 

There were a few projects on the table to deep-dive into: support for JSON datatypes, creating a symbols database-backed system to [replace our filesystem-based one](http://symbols.mozilla.org), and work a bit on replacing the SQL-file migration system in [Socorro](http://github.com/mozilla/socorro) with a SQLAlchemy one. 

## Symbols database and Range Types

I ended up focusing on the symbols database because Ted, [one of our breakpad experts](https://code.google.com/p/google-breakpad/), was around and very generously walked me through what we needed. I have a rough schema in place, and a plan for setting up a few systems to house what will likely be a 1TB database.

In working on this, I spent some time learning more about how to apply [range types](http://www.postgresql.org/docs/devel/static/rangetypes.html). The queries for finding symbols are mostly "show me the functions that contain the memory address I have". Functions all have start addresses and a size, so running "contains" queries makes a lot of sense. In my initial tests, queries using the range types were about 60% faster than queries using plain integer types.

When we've got a larger data set to work with imported, I will post some detailed numbers about the in-database comparisons, as well as any performance improvements we'll get from querying a database instead of loading the plain-text symbols files

## Getting JSON files to describe builds and releases

A small project I've been working on is getting JSON files produced to describe our builds. Before I go on -- please know that this is pretty obscure. The people who are concerned about this information are mostly people who identify crashes and track down which releases are affected by particular bugs. What we keep are things like what platform (Linux, Mac OS X, Windows), what day a release occurred on, whether the release was a beta or not and a few other things.

The way that we got this information in the past was by deriving it from filenames and directory names in our release FTP server. The code to pull this information out is kind of a pain, and if anyone changes a directory name (for a good reason, or on accident..), this code breaks. 

It would be much better if we had a way of getting this information in a standardized format. I recently talked to B2G about putting this information into a JSON file (they already were publishing release information via the manifest directory on our FTP server in XML, so it wasn't too big of a leap).  I thought it would be nice to spread this practice to our other software releases.

As luck would have it, a person familiar for Firefox builds is in Mountain View and was giving Ted a ride to the airport! So, just as they were about to leave, we chatted about the problem, created a bug and now I'm going to get build and release information from a JSON file. :)

It's a tiny change, and hopefully won't take very long to make, but is going to make getting this information much more pleasant and reliable.

## Reading about Kasturba Gandhi

I decided to read a real paper book on my flights last week, and picked up a copy of "The Forgotten Woman", a biography of Kasturba Gandhi, wife of Mahatma Gandhi. Arun Gandhi visited the University of Oregon in the 90s, and my husband had picked up a signed copy. 

I'm having a hard time summing up the book. There were a number of things that surprised me. I hadn't realized that illiteracy for women was so prevalent at the turn of the 20th century in India. I also wasn't aware of the focus Mahatma Gandhi had on women's role in political transformation, or how much he had attributed the origin of [Satyagraha](http://en.wikipedia.org/wiki/Satyagraha) to Kasturba. Also, this biography attributed Gandhi's vow of celibacy to Kasturba's near death after the birth of her fifth child.  Kasturba also led an important self-reliance movement, urging women in India to learn to spin and weave their own cloth, rather than buying foreign goods. She also led an effort to teach hygiene to Indigo farming families.

I had a look at [the wikipedia page for her](http://en.wikipedia.org/wiki/Kasturba_Gandhi), which had no citations and not very well written. I've started some work on it, but need to think a bit more about how it should be structured. 
