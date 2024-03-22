# Reverse PostgreSQL into model with undefined data types

Recently while importing a new physical schema from PostgreSQL 8.4 into Oracle
Data Integrator(ODI) via JDBC driver all of the tables were reversing into the
model without data types defined for text, double precision, smallint, integer
and boolean.

If one or two fields are missing it’s easy enough to set the data type
manually for the column, but for a whole mess of tables and thousands of
fields it’s unrealistic.

The solution is to define the proper data types using the physical
architecture tab with PostgreSQL internal names for the data types. Even
though by default there is one for integer, looking at the [ data type
definitions
](http://www.postgresql.org/docs/8.2/static/datatype.html#DATATYPE-TABLE)
smallint maps to int2, integer maps to int4, double precision maps to float8,
boolean maps to bool.

Using these aliases which are used internally by PostgreSQL for historical
reasons in the ODI Physical Architecture will fix the missing data types
during the reverse process.

Posted in Oracle Data Integrator | Tagged data types , ODI , PostgreSQL , reverse | Leave a comment 


Original post date: June 30, 2011

Category: Oracle Data Integrator