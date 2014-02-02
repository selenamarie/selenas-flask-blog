title: "Drupal + PostgreSQL: review some patches, folks!"
slug: drupal-postgresql-review-some-patches-folks
id: 385
date: 2008-06-16 21:47:43
tags: 
- 5.x
- drupal
- patching
- postgres
- postgresql
- srsly
- tough love
categories: 
- drupal
- postgres
- postgresql

<center>[![baseball bat](http://www.chesnok.com/daily/wp-content/uploads/2008/06/2537026948_23fbc1c5a7.jpg)](http://www.flickr.com/photos/majorvols/2537026948/in/photostream "baseball bat")
<font size="-2">am i the girl, the bat or the heart? you decide!</font></center>

I've been working on [a site](http://pugs.postgresql.org/) that uses Drupal for a few months now. And I'm living dangerously with CCK, Views and, as of last week, Organic Groups.

I found this [sharp moderation module (Modr8)](http://drupal.org/project/modr8) last week, and then quickly realized that I wanted to be able to provide this moderation tool any conferences that wanted it! Enter the Organic Groups.

I'm using PostgreSQL for the back-end database, and so I'm used to being a second-class database citizen in Druplandia.  This means that I frequently have to patch modules so that they use SEQUENCE instead of AUTO_INCREMENT, or get rid of the (8) after an INT type.  So, when Organic Groups and the og_modr8 modules caused [this bug](http://drupal.org/node/128846) to rear up, and I suddenly had a full-scale "blogs running backwards" problem on my hands, I wasn't surprised. 

Thank goodness for Brenda Wallace's [patch](http://drupal.org/node/128846#comment-884840), which fixed everything up a short while later.  What got me, however, was that the problem has had a fix (although not Brenda's ultimate patch) for over a year, but it hasn't been added to core. Particularly when the problem causes nodes to be presented out of order, site-wide.  

Apparently there's a shortage of PostgreSQL reviewers in the Drupal community.

Fortunately, if you'd like to help get patches applied to core, there's a page of [Patches To Be Reviewed](http://groups.drupal.org/node/6980), and a few [people are trying to add a postgresql tag](http://groups.drupal.org/node/9103#comment-28376) to bugs.  If you're a Drupaler and use PostgreSQL, please take a few minutes to review a patch.
