title: "PgCon 2010 - PL/Parrot, Simulated Annealing, Exclusion Constraints, Postgres-XC"
id: 1715
date: 2010-05-26 07:43:19
tags: 
- highlights
- pgcon
- postgres
- postgresql
categories: 
- postgres
- postgresql

[![](http://www.chesnok.com/daily/wp-content/uploads/2010/05/IMG_1302-300x225.jpg "Postgres-XC")](http://www.chesnok.com/daily/wp-content/uploads/2010/05/IMG_1302.jpg)

PgCon this year was full of bold ideas, delivered in the quiet manner typical of the Postgres community. Talks by Jonathan Leto, Jan Urbanski and Jeff Davis all presented new features and ideas that show there is so much room yet in Postgres as a project to contribute, and innovate. I was also delighted to see Postgres-XC (touted as a "Postgres RAC") release code, and give a great presentation on the high-level details.

Jonathan Leto presented work on [PL/Parrot](http://github.com/leto/plparrot), along with David Fetter. Parrot is a dynamic language virtual machine, allowing implementation of multiple dynamic languages which can then share classes ([from the docs](http://docs.parrot.org/parrot/latest/html/docs/intro.pod.html): "In theory, you will be able to write a class in Perl, subclass it in Python and then instantiate and use that subclass in a Tcl program."). The project is to embed Parrot in PostgreSQL, and eventually, implement dynamic languages inside the virtual machine. Advantages to doing this are that it will make implementing new dynamic languages in Postgres much easier, because the language implementers won't have to learn the PL interface. Another useful feature in PL/Parrot is the implementation of a security opcode in Parrot which essentially controls access to open(), a key to implementing a secure procedural language in Postgres. (I'm sure Jonathan will correct me if I didn't describe this properly :D)

Jan Urbanski gave a talk on join ordering via [Simulated Annealing](http://en.wikipedia.org/wiki/Simulated_annealing), called [Replacing GEQO](http://www.pgcon.org/2010/schedule/events/211.en.html). The approach was pretty interesting, involved math that required me to scratch my head a bit, and the initial performance improvements for many-join queries made it seem appealing. The [original -hackers posting](http://archives.postgresql.org/message-id/4B31712B.4040205@wulczer.org) from Jan, includes a few hairy queries from Andres Freund which confound the GEQO referenced later in the thread. Jan's [posted the code](http://git.wulczer.org/?p=saio.git), and I'm looking forward to seeing how it develops this year.

Jeff Davis presented [exclusion constraints](http://www.pgcon.org/2010/schedule/events/201.en.html), which are part of 9.0\. He is continuing his work on temporal data types with a clever and very useful generalization of UNIQUE. UNIQUE constrains equality, while exclusion constraints allow other operators (in the most cited example, Jeff demonstrates "overlaps" in the PERIOD datatype).

[Postgres-XC](http://wiki.postgresql.org/wiki/Postgres-XC) was officially presented and [released](http://sourceforge.net/projects/postgres-xc/). For efforts in Postgres clustering, releasing the code is a huge step forward toward mainstreaming work in the community on clustering. This release solidifies community work that started last year, with NTT and the support of the Japanese PostgreSQL User Group in [having a clustering summit](http://www.chesnok.com/daily/2009/11/19/cluster-developer-meeting-recap/) back in November 2009.

I was disappointed to miss a few talks (like [hypothetical indexes](http://www.pgcon.org/2010/schedule/events/233.en.html), [pg_statsinfo](http://www.pgcon.org/2010/schedule/events/216.en.html), CB's [pgMQ](http://www.pgcon.org/2010/schedule/events/251.en.html)) but looking forward to hearing the recordings as they are published!
