# Import SQL files via psql command line scheduled task

This script will monitor a hot folder, take it’s contents and execute the
files against a postgres server.

Why post this? This python script in conjunction with a [ parameter setting
batch file ](./auto-execute-psql-
commands-via-batch-file/) can take SQL output and apply it to the postgres
database. Originally I was searching how to do this via DOS when I realized I
didn’t have all the error catching capability that I wanted.

Developing this came from trying to solve how to systematically apply changes
from other systems to one database. This script does not make a distinction
between files. So if one system outputs several files that need uploading and
separate files target the same record, last loaded is last applied.

I’ve simplified the script a little for ease of posting, this does require
system variable ` PGPASSWORD ` to run.

    
    
    import os, glob, shutil
    
    # count
    fileCount = 0
    
    # ASSUMES this file is above INCOMING/ BAD/ and ARCHIVE/
    filelist = glob.glob("INCOMING/*.sql")
    
    for file in filelist:
        # take the file and thrown it against psql
        # read psql --help for details about options
        # setting ON_ERROR_STOP to nothing tells psql to pass back an error status code
        errorlevel = os.system("psql -X -U some_user -d database --variable=ON_ERROR_STOP= -1 -w -f "+file)
    
        # check for errors (thrown by psql)
        if errorlevel != 0:
            # error was thrown, lets report it and stash the file
            print errorlevel
            shutil.move(file,"BAD/")
        else:
            print file + " processed"
            shutil.move(file,"ARCHIVE/")
            fileCount += 1
    
    print str(fileCount) + " files processed"
    

Posted in Postgres | Tagged psql , Python , scheduled task | Leave a comment 


Original post date: November 11, 2010

Category: Postgres