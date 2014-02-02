title: "Custom aggregates: a couple tips and ORDER BY in 9.0"
slug: custom-aggregates-a-couple-tips-and-order-by-in-9-0
id: 2059
date: 2010-09-30 16:09:17
tags: 
- 9.0
- custom aggregates
- features
- order by
- postgres
- postgresql
categories: 
- postgres
- postgresql

A friend asked about a way to report the first three semesters that a group of students were documented as being present, and report those values each in a column.  

The tricky thing is that the semesters students attend are rarely the same. I started out with a very naive query (and sorry for the bad formatting that follows.. i need to find some good SQL formatting markup) just to get some initial results: 

`
select student, 
(SELECT semester as sem1 FROM assoc a2 WHERE a2.student IN (a1.student) ORDER BY sem1 LIMIT 1) as sem1,
(SELECT semester as sem1 FROM assoc a2 WHERE a2.student IN (a1.student) ORDER BY sem1 LIMIT 1 offset 1) as sem2,
(SELECT semester as sem1 FROM assoc a2 WHERE a2.student IN (a1.student) ORDER BY sem1 LIMIT 1 offset 2) as sem3
FROM assoc a1
WHERE
student IN ( select student from assoc group by student HAVING count(*) > 2)
GROUP BY student;
`

That query pretty much sucks, requiring five sequential scans of 'assoc':

<pre>
                                     QUERY PLAN                                     
 HashAggregate  (cost=3913.13..315256.94 rows=78 width=2)
   ->  Hash Semi Join  (cost=1519.18..3718.08 rows=78017 width=2)
         Hash Cond: (a1.student = assoc.student)
         ->  Seq Scan on assoc a1  (cost=0.00..1126.17 rows=78017 width=2)
         ->  Hash  (cost=1518.20..1518.20 rows=78 width=32)
               ->  HashAggregate  (cost=1516.26..1517.42 rows=78 width=2)
                     Filter: (count(*) > 2)
                     ->  Seq Scan on assoc  (cost=0.00..1126.17 rows=78017 width=2)
   SubPlan 1
     ->  Limit  (cost=1326.21..1326.22 rows=1 width=3)
           ->  Sort  (cost=1326.21..1328.71 rows=1000 width=3)
                 Sort Key: a2.semester
                 ->  Seq Scan on assoc a2  (cost=0.00..1321.21 rows=1000 width=3)
                       Filter: (student = a1.student)
   SubPlan 2
     ->  Limit  (cost=1331.22..1331.22 rows=1 width=3)
           ->  Sort  (cost=1331.21..1333.71 rows=1000 width=3)
                 Sort Key: a2.semester
                 ->  Seq Scan on assoc a2  (cost=0.00..1321.21 rows=1000 width=3)
                       Filter: (student = a1.student)
   SubPlan 3
     ->  Limit  (cost=1334.14..1334.14 rows=1 width=3)
           ->  Sort  (cost=1334.14..1336.64 rows=1000 width=3)
                 Sort Key: a2.semester
                 ->  Seq Scan on assoc a2  (cost=0.00..1321.21 rows=1000 width=3)
                       Filter: (student = a1.student)
</pre>

So, he reminded me about custom aggregates!  I did a little searching and found an example function that I added an extra CASE statement that stops the aggregate from adding more than three items to the array returned:

`
CREATE FUNCTION array_append_not_null(anyarray,anyelement)  
RETURNS anyarray  
  AS '
SELECT CASE WHEN $2 IS NULL THEN $1 WHEN array_upper($1, 1) > 2 THEN $1 ELSE array_append($1,$2) END 
'
LANGUAGE sql IMMUTABLE RETURNS NULL ON NULL INPUT;  
`

And finally, I declared an aggregate:

`
CREATE AGGREGATE three_semesters_not_null (  
  sfunc = array_append_not_null,  
  basetype = anyelement,  
  stype = anyarray,  
  initcond = '{}'  
);
`

One problem though - we want the array returned to be only the **first** three semesters, rather than any three semesters a student has a record for. Meaning, we need to sort the information passed to the aggregate function. We could do this inside the aggregate itself (bubble sort, anyone?) or we can presort the input!  I chose presorting, to avoid writing a real ugly case statement.

My query (compatible with 8.3 or higher): 

`
SELECT sorted.student, three_semesters_not_null(sorted.semester) 
	FROM (SELECT student, semester from assoc order by semester ) as sorted
WHERE 
	sorted.student IN (select a.student from assoc a group by a.student HAVING count(*) > 2) 
GROUP BY sorted.student;
`

Which yields the much nicer query plan, requiring just two sequential scans: 

<pre>
                                      QUERY PLAN                                      
 HashAggregate  (cost=11722.96..11725.46 rows=200 width=64)
   ->  Hash Semi Join  (cost=10052.32..11570.82 rows=30427 width=64)
         Hash Cond: (assoc.student = a.student)
         ->  Sort  (cost=8533.14..8728.18 rows=78017 width=5)
               Sort Key: assoc.semester
               ->  Seq Scan on assoc  (cost=0.00..1126.17 rows=78017 width=5)
         ->  Hash  (cost=1518.20..1518.20 rows=78 width=32)
               ->  HashAggregate  (cost=1516.26..1517.42 rows=78 width=2)
                     Filter: (count(*) > 2)
                     ->  Seq Scan on assoc a  (cost=0.00..1126.17 rows=78017 width=2)

</pre>

I ran my queries by Magnus, and he reminded me that what I really needed was ORDER BY in my aggregate!  Fortunately, 9.0 has exactly this feature: 

`
SELECT student, 
       three_semesters_not_null(semester order by semester asc ) as first_three_semesters 
FROM assoc
WHERE student IN (select student from assoc group by student HAVING count(*) > 2) 
	GROUP BY student;
`

Which results in the following plan:

<pre>
                                        QUERY PLAN                                        
 GroupAggregate  (cost=11125.05..11711.15 rows=78 width=5)
   ->  Sort  (cost=11125.05..11320.09 rows=78017 width=5)
         Sort Key: public.assoc.student
         ->  Hash Semi Join  (cost=1519.18..3718.08 rows=78017 width=5)
               Hash Cond: (public.assoc.student = public.assoc.student)
               ->  Seq Scan on assoc  (cost=0.00..1126.17 rows=78017 width=5)
               ->  Hash  (cost=1518.20..1518.20 rows=78 width=32)
                     ->  HashAggregate  (cost=1516.26..1517.42 rows=78 width=2)
                           Filter: (count(*) > 2)
                           ->  Seq Scan on assoc  (cost=0.00..1126.17 rows=78017 width=2)

</pre>

A final alternative would be to transform the IN query into a JOIN:

`
SELECT a.student, 
	three_semesters_not_null(a.semester order by a.semester asc ) as first_three_semesters 
FROM assoc a 
	JOIN (select student from assoc group by student HAVING count(*) > 2) as b ON b.student = a.student
GROUP BY a.student;
`

And the plan isn't much different:

<pre>
                                        QUERY PLAN                                        
 GroupAggregate  (cost=11125.05..11711.15 rows=78 width=5)
   ->  Sort  (cost=11125.05..11320.09 rows=78017 width=5)
         Sort Key: a.student
         ->  Hash Join  (cost=1519.18..3718.08 rows=78017 width=5)
               Hash Cond: (a.student = assoc.student)
               ->  Seq Scan on assoc a  (cost=0.00..1126.17 rows=78017 width=5)
               ->  Hash  (cost=1518.20..1518.20 rows=78 width=32)
                     ->  HashAggregate  (cost=1516.26..1517.42 rows=78 width=2)
                           Filter: (count(*) > 2)
                           ->  Seq Scan on assoc  (cost=0.00..1126.17 rows=78017 width=2)

</pre>

Any other suggestions for this type of query? 

I've attached the file I was using to test this out. 
[custom_aggregates.sql](http://www.chesnok.com/daily/wp-content/uploads/2010/09/custom_aggregates.sql_1.txt)
