title: "Fancy SQL Monday: format() instead of quote_*()"
slug: fancy-sql-monday-format-instead-of-quote_
id: 5011
date: 2013-08-26 08:29:35
tags: 
categories: 
- postgresql

In the comments, [Isaac pointed out that using `format()`](http://www.chesnok.com/daily/2013/08/16/catalog-sql-friday-using-do-when-weve-got-tables-as-variables/#comments) dramatically increases the readability of SQL. I liked the look of his query, so I dug a little deeper.

As of version 9.1 (first released in 2010), a new function is listed in Postgres' built-in [string function documentation](http://www.postgresql.org/docs/9.1/static/functions-string.html):

> format(formatstr text [, str "any" [, ...] ]): Format a string. This function is similar to the C function sprintf; but only the following conversion specifications are recognized: %s interpolates the corresponding argument as a string; %I escapes its argument as an SQL identifier; %L escapes its argument as an SQL literal; %% outputs a literal %. A conversion can reference an explicit parameter position by preceding the conversion specifier with n$, where n is the argument position.

We also have [examples linked in the definition for various quoting strategies](http://www.postgresql.org/docs/9.1/static/plpgsql-statements.html#PLPGSQL-QUOTE-LITERAL-EXAMPLE) for dynamic SQL.

This is an example where the Postgres documentation probably should have reversed the order what is mentioned.

It turns out that `format()` makes it much easier to avoid using the `quote_*()` functions. The code looks a lot more like a python `"""` string (you can have arbitrary whitespace in there!), with flexible options for usage. The only feature missing is named parameters.

My application requires Postgres 9.2 at this point (for JSON datatype), so my plan is to refactor a few functions using format() instead of `quote_ident()` in particular.

Are there situations where you'd prefer to use `quote_*()` other than for backward compatibility? It seems as though `format()` is far safer, particularly for the quoting and nullable problems mentioned on the [Quote Literal Example](http://www.postgresql.org/docs/9.1/static/plpgsql-statements.html#PLPGSQL-QUOTE-LITERAL-EXAMPLE) documentation.
