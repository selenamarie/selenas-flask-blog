title: "\"This story seems too negative. Can you fix that?\""
id: 3698
date: 2012-02-16 08:39:46
tags: 
- keith baggerly
- mistakes were made
- open data
- reproducible research
categories: 
- science

I keep watching [this video about cancer research](http://videolectures.net/cancerbioinformatics2010_baggerly_irrh/). The speaker is Keith Baggerly, a statistician who (with a team) [analyzed data from a series of scientific papers for reproducibility](http://bioinformatics.mdanderson.org/Supplements/ReproRsch-All/). 

Specifically, they were looking at findings from research that determines whether or not a cell line is resistant to a drug - like a cancer fighting drug. 
<!--more-->
The problems he highlights in published research are off-by-one errors, mis-labeling and sloppy editing. I keep watching it because it's a familiar tale about trusting experts, and the importance of being able to run data experiments ourselves to confirm or deny the conclusions drawn. And, it's refreshing to be dropped into a funny, jargon-laden talk on par with the stuff I see at open source tech conferences, but a completely different audience and context. 

The terms he uses are at times bewildering, but the message of the talk is a familiar one. We all make mistakes - and sometimes, the systems we have in place don't know how to respond and recover from serious mistakes. Systems like the scientific journals, universities and medical communities. And he notes that they see simple mistakes all the time that could be addressed if the will was present in these systems to make changes. 

One of the more hilarious bits from the talk is around 21:00, when Keith and his team submit their findings to a few biology journals. They get the comment back, "This story seems too negative. Can you fix that?"  LOL

Then he goes into more serious consequences of bad science. Bad data analysis was used as a foundation for clinical (human) trials of drugs. Meaning, [Anil Potti](http://en.wikipedia.org/wiki/Anil_Potti) and a team at Duke were testing cancer drugs on *people* based on complete bogus research results. 

I don't want to get too hysterical about what might happen if the wrong drugs are tested on the wrong people. But it's hard not to go there, when we're talking about multi-year clinical trials, millions of dollars in research and the mistakes that were made.

Ultimately, Keith Baggerly's team had to file a FOIA request to get the data they needed to attempt to verify test results - only possible because the research was publicly funded. Had the research been only privately funded, they would not have been able to get access to the data. (There was a [60 minutes profile of this story last Sunday](http://groups.google.com/group/reproducible-research/browse_thread/thread/dfa8392b7899fb05).)

I love this guy. He's [been giving talks](https://twitter.com/#!/ivanoransky/status/65392539020165120) [about this](http://retractionwatch.wordpress.com/2011/05/04/the-importance-of-being-reproducible-keith-baggerly-tells-the-anil-potti-story/) for a couple years now.

I'm not sure why Keith doesn't have a Wikipedia page. He's termed the work he's doing "forensic bioinformatics." Not only is he funny, smart and working tirelessly to on a truly thankless task (at least in terms of the immediate response editors and colleagues will have to the work - who likes a guy running around actually TESTING conclusions in published papers!), but he's doing something only possible because of _data that's publicly available_, and he's using open source tools to do the analysis. 

There's an important lesson here. He could not do this work if the data from published papers was secret. He could not do this work if the tools to analyze the data were too expensive, or the algorithms used were secret and not available to scientists. 

And, it's true that some scientists are frauds, but sometimes they just make off-by-one errors. Trust, but verify - right? We need people like Keith to help find and correct errors in medical research. No one expects all research to be perfect. But I do expect that people should be able to verify conclusions.

Keith Baggerly now publishes all his papers with [Sweave](http://www.statistik.lmu.de/~leisch/Sweave/), which is a combination of R and LaTeX. Meaning, his papers are executable, and anyone with R and LaTeX can run the analysis. 

They've got a [great mailing list](http://groups.google.com/group/reproducible-research) talking more about reproducible research.

My coworker Luke is [talking today about what he's doing with open data](http://www.slideshare.net/lukec/sustainable-innovation-with-open-data). The tools he's writing are about reminders to take the garbage out, encouraging marital happiness, and reducing waste. His work is only possible because the data is publicly available.

There are big and small reasons we need transparency. Reasons why we need to share scientific knowledge, share government data, write tests for our own code, and trust but verify. It's to automate the routine and dull tasks, make our communities happier and healthier and, sometimes, it's to save lives.
