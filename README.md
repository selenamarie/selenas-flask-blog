This is some simple blog software to replace my wordpress site.

Inspired by: https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/

Features:
- Markdown support for text of blog posts
- Support for metadata: date, tags, categories, slug, title
- HTML title customized by 'title' of page in metadata
- Provides support for typical Wordpress URLs (/?p=<page_id>, date-based URLs)
- Attempts to freeze pages into text files [this is broken unless you comment out some of the routes]
- Different template for 'pages' (no date) and 'posts' (date, tags, categories)
- Procfile for Heroku specifies gunicorn

My List of TODOs
- [ ] Blog more
- [ ] Do things
- [ ] Do them well
