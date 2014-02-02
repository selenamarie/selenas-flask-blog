title: "Migrations with Alembic: a lightspeed tour"
slug: migrations-with-alembic-a-lightspeed-tour
id: 4761
date: 2013-05-17 12:44:46
tags: 
categories: 
- postgresql

I've got a [Beer &amp; Tell](https://wiki.mozilla.org/Webdev/Beer_And_Tell/May2013) to give about [alembic](https://alembic.readthedocs.org/en/latest/). Alembic is a migration tool that works with SQLAlchemy. I'm using it for database migrations with PostgreSQL.

So, here's what I want to say today:

*   Written by SQLAlchemy wiz [Mike Bayer](https://twitter.com/zzzeek)
*   Here's the [tutorial](https://alembic.readthedocs.org/en/latest/tutorial.html). Socorro is now using alembic in production with SQLAlchemy 0.6.x. I'm hoping to get us upgraded to 0.8.x soon.
*   Here's what [running an upgrade in production for Socorro looks like](https://gist.github.com/selenamarie/4dcf5d05bbe8419e4b42/raw/62de2c32f17c0153dc69afa97f145f25a5fab12b/alembic+output+v46.txt). Awesome right?
*   Here's what a [migration looks like](https://github.com/mozilla/socorro/blob/master/alembic/versions/37004fc6e41e_bug_867606_add_data_.py).
*   Here's [a configuration file](https://github.com/mozilla/socorro/blob/master/config/alembic.ini-dist).
*   Generating a migration from the command line might look something like:`alembic revision -m "bug XXXXXX Add a new table" --autogenerate`

The most difficult thing to deal with so far are the many [User Defined Functions that we use in Socorro](https://github.com/mozilla/socorro/tree/master/socorro/external/postgresql/raw_sql/procs). This isn't something that any migration tools I tested deal well with.

Happy to answer questions! And I'll see about making a longer talk about this transition soon.
