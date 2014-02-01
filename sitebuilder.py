#! /usr/bin/env pythnon

import sys
import os
import datetime

from flask import Flask, render_template, url_for, request
from flask_flatpages import FlatPages
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)

freezer = Freezer(app)

@app.route('/')
def index():
    mypages = sorted(pages, key = lambda page:page.meta.get("date", datetime.datetime.strptime('1970-01-01', '%Y-%m-%d').date()), reverse = True )
    return render_template('index.html', pages=mypages)

@app.route('/daily/posts/<path:path>/')
def posts(path):
    post = pages.get_or_404(os.path.join('posts', path))
    return render_template('post.html', page=post)

@app.route('/daily/tag/<string:tag>/')
def tag(tag):
    tagged = [p for p in pages if p.meta.get('tags') and tag in p.meta.get('tags', [])]
    tagged = sorted(tagged, key = lambda tagged_page:tagged_page.meta.get("date", "-1"), reverse = True )
    return render_template('tag.html', pages=tagged, tag=tag)

@app.route('/daily/<int:year>/<int:month>/<int:day>/<string:slug>/')
def by_slug(year, month, day, slug):
    slugged = [p for p in pages if p.meta.get('slug') and slug in p.meta.get('slug', [])]
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
