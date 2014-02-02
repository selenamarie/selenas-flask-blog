title: "an example for upcoming very brief normalization talk (part 1)"
slug: an-example-for-upcoming-very-brief-normalization-talk-part-1
id: 138
date: 2007-09-18 19:55:25
tags: 
categories: 
- mysql

I maintain a small database that prints out UPC labels and tracks serial numbers. It does an OK job at this, but the code is starting to get a little crusty.

I got a wild hair today and decided that I'd had enough with a really annoying update process. Here's the table I was working with: 

<!--more-->
<pre>
CREATE TABLE operational_part_number (
    id INT AUTO_INCREMENT NOT NULL,
    operational_part_number VARCHAR(20) NOT NULL,
    style_id INT10) NOT NULL,
    drilling_set_id INT(10) NOT NULL,
    color_id INT(10) NOT NULL,
    is_front TINYINT(1) NOT NULL,
    has_slotted_holes TINYINT(1) NOT NULL,
    image_location VARCHAR(255),
    primary key (ID)
);
</pre>

So, for every drilling, color and style, I have to create a set of data to insert. 
There were 400+ rows in this table, and I'd just been asked to add another 100 rows. Of course, the GUI doesn't include any admin support. So, I do this with a spreadsheet and awk every time. 

Today, I ran this query: 

<pre>
SELECT LEFT(operational_part_number, 3) AS result, 
        style_id, 
        is_front, 
        has_slotted_holes 
       FROM operational_part_number_old 
       GROUP BY result;
</pre>

The result was 12 rows.  I discovered that the **operational_part_number** was made up of three things: a prefix, the drilling_set, and the color.  And there were only 12 prefixes.

Some rework was in order:

<pre>
CREATE TABLE opn_prefix (
    opn_prefix VARCHAR(20) NOT NULL,
    style_id INT(10) NOT NULL,
    is_front TINYINT(1) NOT NULL,
    has_slotted_holes TINYINT(1) NOT NULL,
    image_location VARCHAR(255),
    primary key (opn_prefix)
);
</pre>

Ahhh.  That's better. Now, the magic comes in with a VIEW to make the web front-end happy:

<pre>
 CREATE or REPLACE VIEW operational_part_number AS
    SELECT CONCAT( opn_prefix.opn_prefix,drilling_set.holes_count, color.code )
        AS operational_part_number,
        style_id,
        drilling_set.id AS drilling_set_id,
        color.id AS color_id,
        is_front, has_slotted_holes, image_location
    FROM opn_prefix, drilling_set, color;
</pre>

I put that all in place, and everything worked.

The end result was that I added only one row to the opn_prefix table, and future updates to part numbers will be just as easy.  Tomorrow I am tackling the finished goods part number mapping to UPCs. I'm not sure I'll be able to automate the process as well.
