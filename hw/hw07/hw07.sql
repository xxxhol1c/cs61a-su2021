CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size 
  FROM dogs, sizes
  WHERE dogs.height > sizes.min AND dogs.height <= sizes.max;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT a.name
  FROM dogs as a,dogs as b,parents
  WHERE a.name = parents.child AND parents.parent = b.name
  ORDER BY b.height DESC ;


-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.child AS pair1, b.child AS pair2
  FROM parents AS a, parents AS b
  WHERE a.parent = b.parent AND a.child < b.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT 'The two siblings, ' || p.pair1 || ' plus '|| p.pair2||' have the same size: '|| s1.size
  FROM siblings AS p, size_of_dogs AS s1, size_of_dogs AS s2
  WHERE s1.name = p.pair1 AND s2.name = p.pair2 AND s1.size = s2.size;


-- Ways to stack 4 dogs to a height of at least 175, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height, n);
  INSERT INTO stacks_helper SELECT name, height, height, 1 FROM dogs;
  INSERT INTO stacks_helper SELECT dogs||', '||name, stack_height + height, height, n+1 FROM dogs, stacks_helper WHERE height > last_height;
  INSERT INTO stacks_helper SELECT dogs||', '||name, stack_height + height, height, n+1 FROM dogs, stacks_helper WHERE height > last_height;
  INSERT INTO stacks_helper SELECT dogs||', '||name, stack_height + height, height, n+1 FROM dogs, stacks_helper WHERE height > last_height;

CREATE TABLE stacks AS
  SELECT dogs, stack_height
  FROM stacks_helper
  WHERE stack_height >= 175
  ORDER BY stack_height ASC;


-- Total size for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  SELECT fur, sum(height)
  FROM dogs
  GROUP BY fur
  HAVING max(height) < 1.3 * avg(height) AND min(height) > 0.7 * avg(height);


-- Heights and names of dogs that are above average in height among
-- dogs whose height has the same first digit.
CREATE TABLE tallest AS
-- this question should revise the name ..?
  WITH avg_height AS(
    SELECT height/10 AS digit, avg(height) AS avg
    FROM dogs
    GROUP BY digit
    HAVING count(*) > 1)
  SELECT height, name
  FROM dogs, avg_height
  WHERE height/10 = digit AND height > avg;


-- non_parents is an optional, but recommended question
-- All non-parent relations ordered by height difference
CREATE TABLE non_parents AS
 WITH 
  ancestor AS (
  SELECT a.name AS first, b.name AS second
      FROM dogs AS a, dogs AS b, parents AS c, parents AS d
      WHERE a.name = c.child AND b.name = d.parent AND c.parent = d.child UNION -- grandparents
  SELECT e.name AS first, f.name AS second
      FROM ancestor AS g, dogs AS e, dogs AS f, parents AS h
      WHERE g.first = e.name AND g.second = h.child AND f.name = h.parent -- great-grandparents
      ),
  relation AS (
  SELECT first AS pair1, second AS pair2 FROM ancestor UNION
  SELECT second AS pair1, first AS pair2 FROM ancestor)
SELECT pair1, pair2
FROM dogs AS a,dogs AS b, relation
where pair1 = a.name AND pair2 = b.name 
ORDER BY a.height - b.height ASC;