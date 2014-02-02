title: "More about JavaScript and PostgreSQL"
slug: more-about-javascript-and-postgresql
id: 4849
date: 2013-05-31 10:51:29
tags: 
- jsconf
- json
- plv8
- schema liberation
categories: 
- postgresql

People asked a lot of questions about what you can do with the datatype and PLV8! My slides are available from the talk [at this dropbox link](https://www.dropbox.com/s/vc2oheabr5s1x11/schema%20liberation%20with%20json%20and%20plv8.pdf). [Speakerdeck seems to be busted](https://speakerdeck.com/selenamarie/schema-liberation-with-json-and-plv8-and-postgres) for the moment. And [here's my gist with the 'liberate()' function](https://gist.github.com/selenamarie/5646494).

Here are some links to resources I've found for using PLV8 and the JSON datatype:

*   [Postgres core documentation for JSON](http://www.postgresql.org/docs/9.3/static/functions-json.html)
*   [Embracing the web with JSON and plv8](http://plv8-pgconfeu.herokuapp.com/#1)
*   [node-postgres](https://github.com/brianc/node-postgres) is the most popular module, older: [Node.js adapter for Postgres](https://github.com/aurynn/postgres-js) -- with Aurynn's patches this is awesome.
*   [LISTEN/NOTIFY example](https://github.com/OrlandoPg/listen-notify)
*   [Building a MongoDB clone in Postgres](http://legitimatesounding.com/blog/building_a_mongodb_clone_in_postgres_part_1.html) -- Jerry is also working on a set of functions that convert PostGIS types to GeoJSON!
*   [What's new in Postgres 9.3](http://wiki.postgresql.org/wiki/What)
*   [JSON and joins](http://stackoverflow.com/questions/13227142/postgresql-9-2-row-to-json-with-nested-joins) -- it's not beautiful, but it is possible. Someone also asked me about "subdocuments" in the style of MongoDB, with foreign keys. I don't have a good answer, but am looking into it.
*   [Live updates to Meteor to Postgres](http://www.lshift.net/blog/2013/02/25/live-updates-to-meteor-from-postgres)
*   [Heroku supporting 9.3beta](https://postgres.heroku.com/blog/past/2013/5/15/postgres_93_beta_access/)

And folks who took notes from my talk:

*   [James Longster's notes](http://jlongster.com/My-JSConf-Diary#plv8)
*   [Dave Stevens' notes](http://dstvns.com/selena-deckelmann-plv8/)
