#! /usr/bin/env pythnon

import sys
import os

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
    return render_template('index.html', pages=pages)


@app.route('/daily/?p=<int:id>')
def id(id):
    ided = [p for p in pages if tag in p.meta.get('id', [])]
    if len(ided) == 1:
        return render_template('post.html', pages=ided[0], id=id)

@app.route('/daily/posts/<path:path>/')
def posts(path):
    post = pages.get_or_404(os.path.join('posts', path))
    print post.meta
    return render_template('post.html', page=post)

@app.route('/daily/tag/<string:tag>/')
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', pages=tagged, tag=tag)

@app.route('/daily/<int:year>/<int:month>/<int:day>/<string:slug>/')
def by_slug(year, month, day, slug):
    slugged = [p for p in pages if slug in p.meta.get('slug', [])]
    print len(slugged)
    return render_template('post.html', page=slugged[0], slug=slug)

@app.route('/daily/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)
