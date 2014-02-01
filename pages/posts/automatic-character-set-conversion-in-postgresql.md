title: "automatic character set conversion in postgresql"
id: 174
date: 2007-11-14 16:36:04
tags: 
- postgres
categories: 
- postgres
- postgresql

Today, I encountered a few goofy characters in the data I am migrating from one ERP system to another. For example, "Â¢" isn't represented the same way in UTF-8 as LATIN1 character sets. In UTF-8, the hex representation for "Â¢" is `c2 a2`, but in LATIN1 it is  `a2`. 

I started looking for an easy Perl way to translate everything into UTF-8 on the client side, when I discovered that PostgreSQL offers [automatic client-to-server character set conversions](http://www.postgresql.org/docs/8.2/static/multibyte.html#AEN24142).  All I have to do is specify what my client character set is. 

Here's how you can do it with an SQL command: 

> `SET CLIENT_ENCODING TO 'LATIN1';> 
> `

Substitute your character set for "LATIN1". 

Lucky for me, my database is set to `UTF8`, and in that case, all supported encodings on my clients will be automatically converted to UTF-8 -- as long as I specify which encoding I'm using.

The support for UTF-8 (formerly called UNICODE in the docs) in PostgreSQL has been around since version 7.1 (early 2000), and in version 8.1 the conversion support for UTF-8 was expanded to all known character sets.
