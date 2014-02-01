title: "Variable substitution with psql"
id: 1901
date: 2010-08-30 08:00:50
tags: 
- commandline
- postgres
- psql
- variables
categories: 
- postgres
- postgresql

**Updated:** Thanks @johto for s/:bar/:foo/. :)

A coworker asked about variable substitution with psql using `\set`, and so I looked into it a bit further.

You definitely can do things like this:
`
16:55 sdeckelmann@[local]:5432|postgres=> \set test 'select * from :foo limit 10;'
16:56 sdeckelmann@[local]:5432|postgres=> \set foo 'test'
16:56 sdeckelmann@[local]:5432|postgres=> :test
myint
     1
     2
     3
     4
     5
     6
     7
     8
     9
    10
(10 rows)
`

But, what about something like this:

`
=> \set test 'select * from :var limit 10;'
=> :test mytable
`

Unfortunately, this isn't supported. 

The best you could do is something pathological like:

`=> \set s 'select * from '
=> \set pr ' limit 10;'
=> :s mytable :pr
=> :s test :pr
myint 
     1
     2
     3
     4
     5
     6
     7
     8
     9
    10
(10 rows)
`
</font>
