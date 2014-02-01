title: "An experiment in attention"
id: 5022
date: 2013-10-13 12:11:12
tags: 
categories: 
- community
- feminism
- gender

I've had reoccurring thoughts about attention and who I give mine to. In the last week, I've been mentioned in a couple "women in tech" twitter lists. This seems to happen about quarterly and someone will create a list of 50 or so, or maybe 100+ women on a list.

I spent a couple days looking through my 5k followers and assembled a list of the [women and women's groups who are following me](https://twitter.com/selenamarie/lists/womentofollow). I probably missed a few, and I know I followed a few people who don't consider themselves women. Sorry! Just let me know and I'll add/drop as needed.

So, why bother with a list like this?

Before I created this list, I was following about 920 people. Which, in itself is a sort of ridiculous number. How could I possibly pay attention to that many people?

I really don't, right? I just check into twitter, sample the firehose, and then step away for minutes, hours or days.

When I do sample the tweet stream, whose voices do I listen to? There are certainly a few close friends whose feeds I look at directly, and a few other people I'm interested in who I will catch up on a backlog. Otherwise, it's whoever is the most vocal.

What I noticed is: most of the voices I hear from when I sample the feed are men. It wasn't anywhere near balanced. That's on social activity, technical rants, technical praise and blogging.

I'd like to be skewed toward women's voices for a while. Particularly on tech issues. So, I just added about 450 women to my feed who were already following me.

My next step may be replacing my primary feed with this list I've made. I [wrote a tool a while back](https://github.com/selenamarie/keepup) to extract URLs and RSS feeds from my friend's twitter profiles and feeds. The code isn't awesome, just rough and practical. But you could do something similar using it. You need a set of read/write API keys ([create an app](https://dev.twitter.com/apps), then make it read/write), but I did the "hard" work for you:

    ./opml.py --consumer_key [key here] --consumer_secret [secret here] --access_token [token here] --access_token_secret [token secret here]  --to_follow [file of twitter handles]

I left some crud in there that links the script directly to my account for the list. Sorry! If anyone actually wants to use this, I'll clean it up. (just ping me on github)

Anyway, doing this kind of attention hacking for yourself isn't hard. It is drudgery to go through all your followers and guess who is what gender. But it is interesting to spend a few hours contemplating what the people you're giving your attention to have in common, and how you might hack it a bit to hear from different perspectives from time to time.

I'm turning comments off because I don't care to hear from anyone who thinks I'm somehow being sexist by changing who I pay attention to. Cheer up, haters! I'm sure plenty of people are already paying attention to you.
