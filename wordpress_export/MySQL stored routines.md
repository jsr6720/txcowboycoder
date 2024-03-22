# MySQL stored routines

Recently I needed to added some functionality to MySQL (5.1) for a project I
am working on.

Several different stored routines needed to be written, so I went about
writing them. Having never written (what I know now are refered to as
“routines) for MySQL I went to the logical place: [ MySQL Documentaiton
](http://dev.mysql.com/doc/refman/5.1/en/stored-routines.html "MySQL Routine
Documentation") .

Being impatient I glanced at the first few lines and found this:

Header: “19.2. Using Stored Routines (Procedures and Functions)”  
My Thought: Ok, so MySQL considers routines to be either procedures or
functions, and because the documentation for both is all on one page, there
couldn’t be that much difference between the two.

In fact on the main landing page for routines, there is no mention of the
distinct differences between a procedure and a function.

All I’m asking is that MySQL create two separate pages for both ` CREATE
PROCEDURE ` and ` CREATE FUNCTION ` , or at the very least have a comparison
page for the have and have notes for the different routine types.

I won’t delve into the many differences as google returns the more relevant
results, but at a high level ` CREATE FUNCTION ` seems better suited for
simple non-cursor based routines that return values and ` CREATE PROCEDURE `
for more complicated cursor based routines.

Posted in MySQL | Tagged function , MySQL , stored procedure | Leave a comment 


Original post date: April 8, 2010

Category: MySQL