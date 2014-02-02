title: "FrOSCon: Mistakes were Made: Education Edition talk slides and notes"
slug: froscon-mistakes-were-made-education-edition-talk-slides-and-notes
id: 4401
date: 2012-08-26 14:01:34
tags: 
categories: 
- conference
- postgresql
- speaking

_I just finished giving my keynote at FrOSCon, and am pasting the notes I spoke from below. This was meant to be read aloud, of course. Where it says [slide] in the text is where the slides advance._

<bold>Update:</bold> [My slides are now available](http://programm.froscon.de/2012/events/1107.html) on the FrOSCon site.

[FrOSCon - Mistakes Were Made: Education Edition](http://www.chesnok.com/daily/wp-content/uploads/2012/08/Froscon-slides-mistakes-were-made.pdf)

[slide]

Thank you so much for inviting me here to FrOSCon. This is my first time visiting Bonn, and my first time enjoying Kölsch.  I enjoyed quite a lot last night at the social event.

Especially, I would like to thank Scotty and Holgar who picked me up at the train station, Inga who talked with me at length on Thursday night. All the volunteers who have done a terrific job making this conference happen.  Thank you all so much for a wonderful experience, and for cooking all the food last night!

And I promised to show off the laser etching on my laptop I had done here by the local hackerspace. I come from the PostgreSQL community, so I got an elephant etched into the laptop. It only costs 10 euro and looks awesome.

[slide]

I've also [made a page of resources](http://piratepad.net/froscon-keynote-selena-reading-list) for this talk. I'll be quoting some facts and figures and this pirate pad has links to all the documents I quoted.

For those of you from countries other than Ireland, Great Britain, United States, German and Turkey - if you know where to get a copy of computer science curriculum standards for your country, please add a link. Right at the top of this pirate pad is a link to another pirate pad where we're collecting links to curriculum standards.

[slide]

And finally, this talk is really a speech, without a lot of bullet points. So, the slides will hopefully be helpful and interesting, but occasionally I will be showing nothing on a slide as I speak. This is a feature, not a bug.

[slide]

For the past few years, I've been giving talks about mistakes, starting with problems I had keeping chickens alive in my backyard. Here's a map of my failures. Scotty is familiar with the video that is online that tells the whole story of how all these chickens died.

Next, I talked about system administration failures - like what happens when a new sysadmin runs UNIX find commands to clean up -- and delete all the zero length files, including devices, on a system. Or how to take down a data center with four network cables and spanning tree turned off. Here's a tip: it really only takes first cable.
<!--more-->
And most recently, I talked about hiring - how difficult it is to find the right people for tech industry jobs, how once you hire them, they might find another job way too quickly, and how the tech industry's demand for skilled developers - and especially for developers with open source skills - is growing faster than we're able to train people.

Computer science enrollment at universities has decreased by about 3% since 2005 in the United States (from 11% of students down to 7% overall).

[slide]

At the same time the projected demand for CS and computer-related jobs will increase more than 50% by 2018, creating about 1.5 million new jobs in the US alone. Researchers say that even in places where enrollment in CS programs is up, companies report that they can't trust that graduates have any of the fundamental skills that are necessary for new jobs.

And these companies aren't just in Silicon Valley - in Oregon (where I'm from), the Netherlands (where I landed before I got to FrOSCon) and from what I've heard these last few days, Germany, are all experiencing shortages in skilled developers.

But I'm not here to talk about those things either.

Today, I'm going to share some observations about computer science education. I believe that our skill shortages start at the earliest stages in our schools, and if the system is left as it is, open source will suffer the most.

[slide]

In a survey of 2700 FOSS developers, 70% had at least a Bachelors degree, and most discovered FOSS sometime between the ages of 18-22\. This age, and this time in college is the perfect time to connect with and attract people into the free software lifestyle. And think about this, how much easier would recruitment be if every student at university was already exposed to computer science ideas when they were in primary and secondary school?

[slide]

You may not know this, but my husband, Scott, is a high school teacher. That's where I got my German last name. He specializes in global studies, journalism and psychology.

Recently, he joined forces with a friend of mine named Michelle Rowley to help teach women how to program with Python. Naturally, I volunteered to mentor in the classes that were offered.

[slide]

This is a picture from one of the classes. Before these workshops, I had never tried to teach anyone how to program.

For the workshops, I mentored groups of 6 or 8 women over two days. We walked around the tables, answering questions and just observing as some students learned about variables, conditionals and functions for the very first time. I  enjoyed getting to know a group of women who were really excited and looking forward to applying the skills they were about to learn.

Mentoring made me feel great, but it was also a little shocking.

[slide]

Our first lessons explained file system navigation, the command-line and how to set up a GUI text editor. Some people quickly became lost and confused. The connection between a graphical filesystem browser and the command-line was very difficult.

Most students had never opened up a terminal and then, beyond that, typed a command into a terminal before. But that's not all that surprising. What did surprise me was that some had never looked at files through the graphical file browser, instead using menus to find recently used files, or saving everyone into just one folder, or just using web-based file management tool like Google Docs. For those women, I found myself at a loss. I sat thinking during a break about how exactly I could explain a filesystem to someone who had never been exposed to the idea before. I thought hard about real world examples that would help me explain.

My hope is that you're all thinking now about metaphors you'd use, pictures you'd draw and what you'd say to a person who didn't understand filesystems.  Or maybe, now that I've said that, you're thinking about it now. Maybe you're thinking about a person in your life who you might teach this exact lesson to. A parent, a brother or sister, a niece, your daughter or son.

I hope you are thinking, because I want to ask each of you to do something after this talk is done. I want you to sit down with an important person in your life who doesn't understand a computer science concept like filesystems and teach them. My guess is, with the right lesson, you can teach this to someone in an hour. And if we don't have the right lesson now, if enough of us try this out, we'll end up with the best lesson in the world for teaching a person what filesystems are, using real-world examples and the feedback from all our loved ones about what worked and what didn't.

There's an important reason why I want you to do this.

[slide]

I want us to demonstrate that sharing lessons works. UNESCO recently made the Paris Declaration. In it they said that they wanted to encourage the open licensing of educational materials produced with public funds. Recently, I contacted an organization to ask if I could transcribe a couple lessons that they'd shared in PDFs into text form to make them easier to use and share them in a git repo. My idea was: share the lessons and let people submit changes and observations as diffs.

The organization that published the lessons told me that they couldn't allow me to use their lessons in this way, because the research was government funded.

I believe that we can demonstrate to teachers and the organizations creating curriculum how useful it can be to share, so that no one gives me that excuse ever again.

I want to show teachers how interesting and engaging it is to let people take a lesson, try it out and report back. These, after all, are the same skills we need to work on open source software  Except we'll apply this skill to teaching a lesson.

So, get ready. I really am going to ask you all to do that.

[slide]

I started understanding what programming was my second year of college. I'd spent almost a year doing tech support at my university, getting the job after some friends taught me how to install linux from floppies and enough UNIX commands to be dangerous. One day, a friend sat me down and tried to teach me PASCAL from a book. The experience left me frustrated, and even angry. I remember thinking that very little of it made sense, and I felt very stupid. I decided at that moment that I never wanted to learn programming.

Later, a different friend from college, Istvan Marko, sat me down in front of a command line prompt and showed me a shell script. He told me about his work automating configurations and showed me how to  set up linux systems way more quickly than I could by entering commands one at a time. The automation blew my mind.

What he modeled for me in shell scripting immediately made my work life better. The tools he showed me applied to what I already knew about computers and installing new linux systems, and I saw immediately how I could use it all.

A whole world opened up as I thought through problem after problem, wrote little scripts to recompile kernels, and copied tricks from other friends like timing commands or redirecting output from STDERR to STDOUT. In the beginning I was just copying and studying because I was a little afraid of making mistakes -- automation was so powerful! But soon I was remixing and writing my own stuff from scratch. I was hooked.

The next year, I switched my degree program from Chemistry to Computer Science.

So, I don't think every person exposed to shell scripting will want to become a developer. But there were two things that happened for me in that lesson: what Istvan managed to get right was teaching me in my "zone of proximal development" or ZPD. It's an education term that basically means -- it was just challenging enough to be interesting, but not so hard that I got completely frustrated. This zone is where people learn things really well.

[slide]

The other important thing that happened was that the skill my friend taught me was something I could immediately apply elsewhere. But first, he worked with me, what we call guided practice, to rewrite a simple shell script with my username as a variable. Then I went off on my own, writing my own scripts to start and stop network interfaces and automatically connect to servers and run commands. This is what we call independent practice. And later, when I started writing Perl, I wrote my Perl exactly like I was writing bash scripts.  I had just generalized my skills to another language! Maybe in the worst way possible!

But what all those things were - the modeling, the guided practice, the independent practice and the generalization - was how I really learned a new skill. I learned how to think about tasks with automation in mind, with parameters and variables in mind. And I really, really learned it well because my friend took the time to make sure that I learned it.

My experience of having a real-world application for a new skill matches up with research about keeping women and minorities, and many men, engaged in computer science. The process of customizing curriculum for the life experience of students is called contextualization.  And of course, each person's context is different. Part of the challenge for educators is designing courses that can be relevant to students from a variety of backgrounds, perhaps very different than the teacher. Like, teaching a bubble sort of student names in the physical world by having kids get up and move around, instead of teaching sorting only with numbers on a screen. Or using election data from local elections that affect students lives to teach about database schema and report design.

Or, when you're thinking about this lesson you're going to teach about filesystems, find a way to tie it to the life of the person you're teaching. Have they ever "lost" a file that you later helped them find with the filesystem "search"? Have they ever lost a hard drive, or part of a directory, or lost something "in the cloud". Have they created files on their computer? Do they know where those files are? Or what "where" means on a computer? Could you maybe draw some kind of structure to help them think about how the files are organized? I'm sure you'll come up with something great to fit your student's experience.

[slide]

Some people believe that the reason why we don't have enough people with the right kinds of developer skills is because university CS programs just aren't teaching the right things.  And, honestly, a lot of programmers never went to college for computer science!

For all of us at FrOSCon, who are often trying to hire people with open source specific skills, it's certainly true that very few universities are training students for that. But I think there's a much bigger problem than the university programs out there.

[slide]

If you look at CS curriculum versus math, science, history or literature, you'll find that there's almost no computer science taught in primary and secondary schools. In the US, over the past 10 years we have lost 35% of the comp sci classes taught in high school, which is 9-12 grades. In addition, we have very few computer science teachers, and inconsistent standards for testing and qualifying CS teachers -- leading to a teacher shortage in the places where CS is actually wanted by a school.

[slide]

I talked with Inga Herber, one of the core organizing volunteers here at FrOSCon, on Thursday night. She's is preparing to teach secondary school computer science here in Germany. Her observations were that here, there's a strong movement in the schools to get more computer science classes, yet there are still not many qualified teachers.

But worse than the lack of classes and teachers, if you look at what is being taught in the few places where something like CS is available, we see classes like basic keyboarding -- which drills to help you type faster -- are given the "computer science" label. Also -- there are classes on how to use Excel and Word, searching the internet, or how to program in obscure or outdated languages, which for students often means just copying and pasting functions out of books. We're actually teaching the "copy pasta" form of programming in our schools!

The most promising classes in high school would seem to be those that teach students how to take apart and put back together computers. Knowing the parts of a computer is certainly useful. But learning computer science by taking apart and putting computers back together is like learning to read by tearing books apart and putting them back together. (thanks to Mike Lee for that analogy) In the same way that we don't think of bookbinding as essential for literacy, taking apart and putting together computers, while fun and educational, will not teach computer science literacy.

[slide]

What we really need to teach students has nothing to do with keyboards, the office suite or motherboards. In the words of the the "Exploring computer science" curriculum, we need to teach "computational thinking practices of algorithm development, problem solving and programming within the context of problems that are relevant to student's lives."

This idea of "computational thinking" comes via Jeanette Wing, who wrote about this idea for the ACM in 2006\. "Computational thinking is a fundamental skill for everyone, not just for computer scientists. To reading, writing, and arithmetic, we should add computational thinking to every child’s analytical ability. Just as the printing press facilitated the spread of the three Rs, what is appropriately incestuous about this vision is that computing and computers facilitate the spread of computational thinking."

[slide]

And she provides a much longer definition later, that includes this, my favorite part:

[it's] A way that humans, not computers, think. Computational thinking is a way humans solve problems; it is not trying to get humans to think like computers. Computers are dull and boring; humans are clever and imaginative. We humans make computers exciting. Equipped with computing devices, we use our cleverness to tackle problems we would not dare take on before the age of computing and build systems with functionality limited only by our imaginations.
Jeanette Wing's description makes me think about a world where computer science would be inspiring to everyone.  And not just inspiring, but creative and fun.

[slide]

It makes me think of the great Ada Lovelace comics I've seen like this one by Sydney Padua, where Charles Babbage and Ada Lovelace, creators of the first computing machine, are crimefighters.  The heroes are quirky, smart and solving devilishly tricky problems.

Another show I love the new Sherlock, a BBC TV show, for how wonderfully geeky he is in his problem solving, and how he often uses silly pranks with technology to show off. The first episode has him sending group texts as a sarcastic counterpoint to a police chief's press conference.

In the same way that Einstein and Feynman are crucial parts of the storytelling around physics, we need to talk more about the heroes of computer science, about what made them human, and interesting and not like computers at all.

And armed with these fascinating stories, we can share them as part of our teaching. Because this is all so fun -- this conference, is full of people with great stories, working on an event that spans seven years. There have been great times, and near disasters, and triumphs. Those can be our examples and starting points for explaining the computer science that we want our friends and family to understand.

[slide]

As I've done my research, its become painfully clear how separated open source developers are from teachers. There's a lot of reasons why this might be. I married a teacher, but I don't think advocating for marriage between teachers and open source people is a scalable solution.

So, other than marriage, how can we invite more teachers into open source?

One barrier to communicating with teachers is being able to speak the language of education. This is not just the terms teachers use for their work. It's also having the experience of and relating to teaching.

Teaching is incredibly difficult. It's both mentally and physically challenging. When I finished mentoring students for one day and teaching a single hour-long lesson, I was ready for a beer and sleep. I can't imagine doing that every day.

[slide]

But teachers - they do this for 8 hours a day, every day. A valuable experience for every developer is to just for a few minutes, to teach something new, in person and without a computer. I don't think you need to get in front of a classroom to experience this.

What you can do is schedule an hour with a friend, a colleague or a family member and try to teach. See if you can get them to really understand, and then demonstrate the new skill back to you. Like with the filesystems - after you explain, see if they can do something specific -- like find a special file (easter egg planting!), or explain back to you what it is that you taught them, or even better: watch as they try to explain filesystems to someone else.

Once you've had the experience of helping someone master a brand new skill, you've started down the path that teachers walk every day. This is a shared experience, a point of empathy you can draw on if you ever have the chance to talk directly to a teacher.

[slide]

For too long, free software advocates have focused on getting open source software into classrooms without understanding exactly what that means to teachers. When something goes wrong with my servers or my laptop, it's my job to figure out what is wrong and to fix it. I have time in my day for mistakes, and for bugs.

Teachers, on the other hand, have a certain number of hours in a year with students. They count them! That time is carefully scripted, because teaching is actually very difficult. Teachers can't improvise excellent teaching when the computers they are using crash, or the software doesn't work the way they expected, or the user interface changes suddenly after an upgrade. All the things that I think of as features, for teachers are another thing that takes away time they would spend creating lessons and teaching students. This is why I think free software is not more widely used in schools.

[slide]

I do not mean to diminish the efforts of the many awesome projects like Skolelinux, a school-specific Linux distribution based on Debian. But if we look at the software that runs grading and attendance, the software that kids use to play games, and the operating systems on teacher computers -- this software is largely still proprietary.

I hope that I can plant a seed of empathy in you all for what teachers are up against. Think about how much time that you spend considering the filesystem lesson you're going to teach, for example. My husband was given one hour per day to plan for 7 hours of teaching. I spent nearly 100 hours preparing for this keynote. The ratio of preparation time to instruction time is terrifyingly small for professional teachers.

[slide]

If open source contributors all experienced what in-person teaching is like to the non-technical people in our lives, learning to use modeling, guided practice, independent practice and generalization in our own lessons about open source technology, we will develop a common vocabulary to talk with teachers. In the same way that in free software we share a vocabulary that starts with freedom, source code and sharing.

And once we can talk with teachers, and we do so on a regular basis, we can ask them what it is that they really need, and how we as open source experts can help them make schools and teaching even better. Because, really, teachers and the free software movement are natural allies in our efforts to share information.

[slide]

We have a tremendous problem ahead of us. There aren't enough people who understand the fundamentals of computer science. And a lot is at stake.

We're in an era where privacy, financial security and our elections are managed by software. If we all get this right, then software we create will also be used to fight corruption, solve important problems and make us all more free.

Before I leave, I want to share a story from 2009\. This isn't a free software story, not yet, but it's about the power of computational thinking when applied to the democratic process.

[slide]

So in 2009, I was invited to come teach a class about PostgreSQL. I travelled to Ondo State, Nigeria, specifically to Akure.

[slide]

Here's a picture of my students. They had degrees in computer science or taken programming classes, and several were professional developers.

[slide]

It was from them that I learned how the Governor of Ondo state, Olusegun Mimiko, won his election. He was running against former Governor Agagu, the People's Democratic Party candidate, which is also the majority party across Nigeria.

[slide]

You may not have heard about this, but back in 2007 when the elections were held, there was country-wide unrest. United Nations observers reported violence, and accusations of voter fraud were raised.

[slide]

So, once the ballots were counted, Mimiko had lost.

[slide]

But, his campaign had been so sure they were going to win because of poll results.

[slide]

So, they filed a lawsuit and got ahold of the ballot boxes for a recount. And it was at this point where they did something different.

[slide]

The way that you vote in Nigeria is with a thumb-print next to the candidate you select on a paper ballot. So, if there was fraud, the Mimiko team reasoned, you would have lots of ballots with the same thumb print. A local group of techies put together a plan. They would electronically scan in all the ballots and then have someone validate fingerprints and find duplicates.

[slide]

They searched the world for a fingerprint expert, and found Adrian Forty in Great Britain. Adrian Forty and his team analyzed all the ballots, and they found a few duplicates.

[slide]

In fact, they found 84,814 duplicate fingerprints. In one case a single fingerprint was used 300 times.

[slide]
After a two year court battle, finally, they won. :) But the work was just beginning. 
[slide]

One of the places my colleagues took me was Idanre Hill, which is on the tentative world heritage site list. This is a picture of a handrail that was cut by the outgoing government. My colleagues said this in Yoruba which means "left like thieves." They won the election, but got no help from the outgoing government to transition to power.

[slide]

Of course, the method for detecting voter fraud was viral. The expertise in counting fingerprints has been shared with neighboring states, and similar fraud was uncovered and stopped in Osun State as well.

[slide]

The new government in Ondo State has been very focused on IT initiatives, and in particular focused on what using cell phones to connect citizens with their government can do. One initiative gave all new mothers cell phones to stay in touch with their doctors.  The cell phone program resulted in reducing the number of mother and child deaths to just 1 last year, a 35% drop in mother and infant mortality. Their goal is a 75% reduction in infant mortality by 2015.

[slide]

This last picture was taken as two friends and I hiked up Idanre Hill.

Which brings me to what I want you all to do.

We need to teach people how to ask the right questions, to be suspicious or satisfied by the answers they get to their questions. We need to teach people how to break apart problems into understandable chunks instead of assuming that they will never understand a complicated process.

And we need to teach them the value of sharing source code. What it means to have software freedom, and how much it matters to us that everyone has the opportunity to learn from and build upon the work of others.

I believe that we can demonstrate again, to the world, how useful it can be to share, how interesting and engaging it is to let people take a lesson, try it out and report back.

Think about filesystems. Think about your friends and family. Who could you spend an hour with, teaching them an important skill that will help them understand our world of computers?

Thank you very much for your time today.

_To encourage you all to do this, I [created a little website](http://teachtoday.chesnok.com/) where you can publicly say that you're going to try to teach a lesson to someone. The authentication system only supports twitter right now - very sorry. But I have some code and was planning on hacking in email login this afternoon. I also have published the code on Github and linked to it from the site. I hope that you'll have a look, and certainly if you find bugs, let me know._
