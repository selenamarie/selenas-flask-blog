#! /usr/bin/env pythnon

import sys
import os
import datetime

from flask import Flask, render_template, url_for, request
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from feedgen.feed import FeedGenerator

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
fg = FeedGenerator()
fg.title("Selena Deckelmann's Blog Feed")
fg.link(href='http://chesnok.com/daily', rel='self')
fg.description('A blog about postgres, open source and the web')

freezer = Freezer(app)

def generate_feed(items, tag=None):
    for item in items:
        fe = fg.add_entry()
        #fe.id('http://chesnok.com/daily/'. item.meta.get('slug', ''))
        fe.author({'name':'Selena Deckelmann', 'email':'selena@chesnok.com'})
        fe.title(item.meta.get('title', ''))
        if tag:
            fe.link(href='http://chesnok.com/daily/category/' + tag + '/feed/', rel='self')
        else:
            fe.link(href='http://chesnok.com/daily/feed/', rel='self')
    return fg.rss_str(pretty=True)

@app.route('/daily/feed/')
def feed():
    sorted_pages = sorted(pages, key = lambda tagged_page:tagged_page.meta.get("date", "-1"), reverse=True)
    return generate_feed(sorted_pages[:10])

@app.route('/daily/category/python/feed/')
def feed_python():
    tag = 'python'
    tagged = [p for p in pages if (p.meta.get('categories') and tag in p.meta.get('categories', []))]
    tagged = sorted(tagged, key = lambda tagged_page:tagged_page.meta.get("date", "-1"), reverse=True)

    return generate_feed(tagged[:10], tag)

@app.route('/daily/category/postgresql/feed/')
def feed_postgres():
    tag = 'postgresql'
    tagged = [p for p in pages if (p.meta.get('categories') and tag in p.meta.get('categories', []))]
    tagged = sorted(tagged, key = lambda tagged_page:tagged_page.meta.get("date", "-1"), reverse=True)

    return generate_feed(tagged[:10], tag)

@app.route('/')
def index():
    mypages = sorted(pages,
        key=lambda page:page.meta.get("date",
            datetime.datetime.strptime('1970-01-01', '%Y-%m-%d').date()),
        reverse=True )
    return render_template('index.html', pages=mypages[:10])

@app.route('/daily/posts/<path:path>/')
def posts(path):
    post = pages.get_or_404(os.path.join('posts', path))
    return render_template('post.html', page=post)

@app.route('/daily/tag/<string:tag>/')
def tag(tag):
    tagged = [p for p in pages if (p.meta.get('tags') and tag in p.meta.get('tags', []))
            or (p.meta.get('categories') and tag in p.meta.get('categories', []))]
    tagged = sorted(tagged, key = lambda tagged_page:tagged_page.meta.get("date", "-1"),
        reverse=True )
    return render_template('tag.html', pages=tagged, tag=tag)

@app.route('/daily/<int:year>/<int:month>/<int:day>/<string:slug>/')
def by_slug(year, month, day, slug):
    slugged = [p for p in pages if p.meta.get('slug') and slug == str(p.meta.get('slug', None))]
    if len(slugged) == 1:
        return render_template('post.html', page=slugged[0], slug=slug)
    return render_template('page_not_found.html'), 404

@app.route('/daily/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

@app.route('/daily/', methods=['GET'])
def id():
    page_id = request.args.get('p')
    ided = []
    for p in pages:
        if p.meta.get('id', None) and int(page_id) == p.meta.get('id'):
            return render_template('post.html', page=p, id=page_id)
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)
