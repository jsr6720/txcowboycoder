# Auto execute psql commands via batch file

` psql ` via command line does not have an option for password. To run a
scheduled task using ` psql ` is pointless without full automation.

Warning postgres recommends against doing this, and instead use a [ password
file ](http://www.postgresql.org/docs/8.4/interactive/libpq-pgpass.html) .

I use this script to kick off the [ psql command in python
](http://txcowboycoder.wordpress.com/2010/11/11/import-sql-files-via-psql-
comma/) . But you can execute psql straight from the batch file, just check
the ` %ERRORLEVEL% ` batch variable from the calling method.

    
    
    @echo off
    
    REM scheduled task point to .bat files
    REM besides we need to make sure we have system variables in place
    
    REM export a password for use with the system (no quotes)
    SET PGHOST=host
    SET PGDATABASE=database
    SET PGUSER=user
    SET PGPASSWORD=user
    
    REM execute psql by file, even though echo is off, errors will still show
    psql -X --variable=ON_ERROR_STOP= -1 -w -f filename.sql
    

Posted in DOS | Tagged bat file , batch file , DOS , psql | 2 Comments 


Original post date: November 11, 2010

Category: DOS