title: "TIL: Formatting, search_path and colorcolumn"
slug: til-formatting-search_path-and-colorcolumn
id: 4793
date: 2013-05-10 14:34:24
tags: 
categories: 
- python

The last six months have involved a lot more writing of code than the previous couple of years.

I've been tweeting little things I learn on a daily basis and thought I'd look back on this week.

# format()

A reocurring problem with report writing is getting numbers formatted properly for the occassion. I discovered 'format' in Python this week:

    print "{0:.2f}%".format(float(1)/3 * 100)
    `</pre>

    That prints out a float to 2 decimal places. I looked around and [Dive Into Python](http://www.diveintopython.net/native_data_types/formatting_strings.html) has similar syntax, but without the format() function. So, the equivalent would be:

    <pre>`print "blah %.2f" % (float(1) / 3 * 100)
    `</pre>

    So, why use one over the other? A user on [StackOverflow](http://stackoverflow.com/questions/5082452/python-string-formatting-vs-format) suggested that compatibility with 2.5 might drive a person to use '%' over 'format()', but otherwise, the poster suggested that format() is the cleaner looking and more flexible choice.

    # set search_path = bixie

    I'm working on a new schema for a [project](http://xor.lonnen.com/2013/04/11/error-reporting.html). We're rolling out a prototype quickly, so we're going to house it in our existing production database for now. To keep things easy to clean up, [Laura](http://twitter.com/lxt) suggested that we put things into a [separate schema](http://www.postgresql.org/docs/current/static/sql-createschema.html). For managing our database models, I've switched to using SQLAlchemy, and also alembic for migrations. This made it super easy to specify that I wanted all the Bixie related tables in their own schema:

    <pre>`class BixieCrash(DeclarativeBase):                                              
        __table_args__ = {'schema': 'bixie'}                                        
        __tablename__ = 'crashes'
    `</pre>

    And that was it.

    Then, to avoid having to add 'bixie.' to all the table paths in test queries, I put this command into the tests:

    <pre>` cursor.execute(""" SET search_path TO bixie """)
    `</pre>

    I imagine there are some other ways to handle this. We're not really using the ORM for anything other than schema loading, so I'll probably add that to our connection initialization code for the new app. Then developers can write their queries as without any concerns about being in the correct schema.

    And I'll glow just a little bit about deploying alembic on stage!

    <script src="https://gist.github.com/selenamarie/f9c7a56544b924a4520f.js"></script>

    # set colorcolumn=80

    I've been trying to write prettier Python. Today's micro-effort was figuring out how display a vertical line to tell me when I exceed the 80 character width.  The proper command to add to .vimrc is:

    <pre>`:set colorcolumn=80

Which looks something like:

[![colorcolumn in action](http://www.chesnok.com/daily/wp-content/uploads/2013/05/Screenshot-from-2013-05-10-152620-300x168.png)](http://www.chesnok.com/daily/wp-content/uploads/2013/05/Screenshot-from-2013-05-10-152620.png)
