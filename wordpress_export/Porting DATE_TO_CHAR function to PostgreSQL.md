# Porting DATE_TO_CHAR function to PostgreSQL

This allows multiple data stores but without rewriting all sql queries. Note
you have to create two functions, one to accept dates, the other to accept
times.

Specifically the 4D SQL function [ ` DATE_TO_CHAR `
](http://doc.4d.com/4D-SQL-Reference-12.1/Functions/DATE-TO-
CHAR.300-494541.en.html) . Luckily PostgreSQL has the equivalent as a
formatting function [ ` to_char `
](http://www.postgresql.org/docs/8.4/static/functions-formatting.html) .

For business reasons it’s not practical to replace all instances of `
DATE_TO_CHAR ` to ` to_char ` .

##  Solution

Create a function in the postgresql data base that maps the ` DATE_TO_CHAR `
function to ` to_char ` . Luckily the formatting options I need are available.

Now ` SELECT DATE_TO_CHAR(DateField1, "YYYY-MM-DD") FROM Table1 ` will return
the correct value regardless of the database queried. It’s important to note
this works great for getting integer values from dates and casting as date
objects. If queries rely on returning non-iso formatting your mileage may
vary.

    
    
    -- Function: date_to_char(date, text)
    CREATE OR REPLACE FUNCTION date_to_char(date, text)
      RETURNS text AS
    $BODY$
      DECLARE
      BEGIN
           RETURN to_char($1,$2)::text;
      END;
      $BODY$
      LANGUAGE plpgsql VOLATILE
      COST 100;
    ALTER FUNCTION date_to_char(date, text) OWNER TO postgres;
    
    
    
    -- Function: date_to_char(time without time zone, text)
    CREATE OR REPLACE FUNCTION date_to_char(time without time zone, text)
      RETURNS text AS
    $BODY$
      DECLARE
      BEGIN
           RETURN to_char($1,$2)::text;
      END;
      $BODY$
      LANGUAGE plpgsql VOLATILE
      COST 100;
    ALTER FUNCTION date_to_char(time without time zone, text) OWNER TO postgres;
    

Posted in 4D , Postgres | Tagged 4D SQL , Postgres , SQL function | Leave a comment 


Original post date: July 11, 2011

Category: 4D