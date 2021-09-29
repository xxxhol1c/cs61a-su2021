.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet 
  FROM students 
  WHERE color = 'blue' and pet = 'dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song
  FROM students
  WHERE color = 'blue' and pet = 'dog';


CREATE TABLE matchmaker AS
  SELECT s1.pet, s1.song, s1.color, s2.color
  FROM students AS s1, students AS s2
  WHERE s1.pet = s2.pet and s1.song = s2.song and s1.time < s2.time;


CREATE TABLE sevens AS
  SELECT s.seven
  FROM students AS s, numbers AS n 
  WHERE s.number = 7 and n.'7' = 'True' and s.time = n.time;


CREATE TABLE favpets AS
  SELECT pet, count(*) AS counts
  FROM students
  GROUP BY pet
  ORDER BY count(*)
  DESC
  LIMIT 10;


CREATE TABLE dog AS
  SELECT pet, count(*) AS counts
  FROM students
  WHERE pet  = 'dog'
  GROUP BY pet;


CREATE TABLE bluedog_agg AS
  SELECT song, count(*) AS counts
  FROM bluedog_songs 
  GROUP BY song
  ORDER BY count(*)
  DESC;


CREATE TABLE instructor_obedience AS
  SELECT seven , instructor , COUNT(instructor)
  FROM students
  where seven = '7' 
  GROUP BY instructor;


CREATE TABLE smallest_int_having AS
  SELECT time, smallest
  FROM students
  GROUP BY smallest
  HAVING count(smallest) = 1;


CREATE TABLE smallest_int_count AS
  SELECT smallest, count(smallest)
  FROM students
  GROUP BY smallest
  ORDER BY smallest;














