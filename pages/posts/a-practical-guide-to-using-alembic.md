title: "A practical guide to using Alembic"
slug: a-practical-guide-to-using-alembic
id: 4891
date: 2013-07-02 15:58:07
tags: 
- alembic
- postgres
- postgresql
- sqlalchemy
categories: 
- postgresql
- python

_I spent some time guiding a coworker through using [Alembic](http://alembic.readthedocs.org) for the first time with [Socorro](http://github.com/mozilla/socorro) this morning and what follows are my notes from that meeting._

I've been using Alembic, a [database schema migration](http://en.wikipedia.org/wiki/Schema_migration) tool, for about three months now, and really liking it a lot. I created a blog post that served as a slide deck for an internal team called [A lightspeed tour of Alembic](http://www.chesnok.com/daily/2013/05/17/migrations-with-alembic-a-lightspeed-tour/) as my first stab at user education.

Setting things up initially was pretty simple, but explaining it to a coworker after I'd set everything up for myself proved slightly more difficult. Below are my notes on the differences between [Alembic](http://alembic.readthedocs.org) and some other migration tool.

## Terminology

Alembic calls each migration a _revision_. Revisions know what order to be run in because each revision is given a `down_revision` to identify its parent. If `down_revision` is `None`, that revision is the very first revision according to Alembic. You can put your whole schema in that revision, or you can just start adding changes to this initial revision. Alembic doesn't complain either way.

A best practice would likely be putting your entire model into the first revision. I may go back and "fix" this for us later. I opted to just have the default use case be to create a database fresh with a tool we call `setupdb_app.py`.

If you're looking to migrate to using alembic, you'll also need to use SQLAlchemy. I used sqlautocode for my initial schema [reflection](http://docs.sqlalchemy.org/en/latest/core/schema.html#reflecting-database-objects), and there's a new tool [sqlacodegen](https://bitbucket.org/agronholm/sqlacodegen/src) you may want to check out for generating your SQLAlchemy models for the first time.

## Preparation: edit config and activate a virtualenv

Our environment was set up per the [alembic tutorial for creating an environment](https://alembic.readthedocs.org/en/latest/tutorial.html#creating-an-environment). I ran:

`alembic init alembic`

I also put an `alembic.ini-dist` file into our project's `config/` directory, and modified `alembic/env.py` to include our model.

To get started working with an existing install, you'll need to modify `alembic.ini-dist`, and copy it to `config/alembic.ini` to fit your environment - setting the connection string and the path to the alembic directory are the two most important settings. We have a script which creates databases from our `models.py` called `setupdb_app.py`. This script takes `--database_name` as a command-line argument. My default for our project is to use `breakpad`.

We use a `virtualenv` called `socorro-virtualenv`. The virtualenv is created automatically if you run `make test`. If you're creating a standalone virtualenv, you can do that with `virtualenv socorro-virtualenv`. Activate this with `. socorro-virtualenv/bin/activate`.

# Creating a revision

1.  Create a fresh database to work from. For Socorro, the command is: `PYTHONPATH=. socorro/external/postgresql/setupdb_app.py --database_name=breakpad`
2.  Edit `models.py` with the change to the schema
3.  Run: `PYTHONPATH=. alembic -c config/alembic.ini revision -m 'your message about the migration'`. The output will include the name of the new file.
4.  Edit that file as needed `alembic/versions/*.py`
5.  Run: `PYTHONPATH=. alembic -c config/alembic.ini upgrade +1`

If all goes well, your revision is ready! If something goes wrong, edit and try again. The revision will automatically rollback if there are any errors.

# Production deployment

You'll need to deploy an `alembic.ini` on your production database system and probably a `virtualenv` to support your python modules.

We deploy our virtualenvs with our application, so this step was pretty simple for everything except for alembic itself. The virtualenv put in full, static paths for the python binaries and had some dependencies that I haven't figured out yet for actually running alembic. To get around this, I created a virualenv locally on the system for the _postgres_ user. Having your postgres user run the migrations locally is a must for me because I need to access the filesystem to pull in new versions of user defined functions stashed in the directory my model lives in.

I just deploy a new release of our application code on the database server locally, and then I run alembic against the `versions` directory that's deployed.

# FAQ

And here's an FAQ for the common problems folks ran into:

## OOPS I forgot to create a database before I created a revision!

To "fix" this, try:

1.  Create the database from scratch using your current `models.py`.
2.  Run: `PYTHONPATH=. alembic -c config/alembic.ini downgrade -1`
3.  Run: `PYTHONPATH=. alembic -c config/alembic.ini upgrade +1`

Assuming your downgrade function works, this should allow you reverse the latest revision and then test your migration.

## Error message: "Only a single head supported so far."

See [Working with Branches](https://alembic.readthedocs.org/en/latest/tutorial.html#working-with-branches).

## I'm using schemas, and alembic doesn't recognize them when I try to use `--autogenerate`.

See [include_symbol](http://alembic.readthedocs.org/en/latest/api.html?highlight=include_symbol). And be sure to add this to both the "offline" and "online" versions of the revision code in `env.py`.

## Error message: Target database is not up to date.

This means you've got a file in your `versions` directory that contains one or more migrations that haven't been applied to the current database. You can either apply them with `alembic upgrade head` or have a look in that directory and remove the migration(s) that you don't want.
