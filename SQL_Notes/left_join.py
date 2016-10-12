-- Here are two tables describing bugs found in some programs.
-- The "programs" table gives the name of each program and the files
-- that it's made of.  The "bugs" table gives the file in which each
-- bug was found.
--
-- create table programs (
--    name text,
--    filename text
-- );
-- create table bugs (
--    filename text,
--    description text,
--    id serial primary key
-- );
--
-- The query below is intended to count the number of bugs in each
-- program. But it doesn't return a row for any program that has zero
-- bugs. Try running it as it is.  Then change it so that the results
-- will also include rows for the programs with no bugs.  These rows
-- should have a 0 in the "bugs" column.

select programs.name, count(bugs.filename) as num
   from programs left join bugs
        on programs.filename = bugs.filename
   group by programs.name
   order by num;
