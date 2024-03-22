# Automatic cron backup of PostgreSQL database

There are lots of great backup tools and utilities out there, but utilizing a
simple script and cron task to target specific PostgreSQL database is often
the fastest way to a locally based backup procedure.

The below shell script is run as the ` postgres ` user on a ` Linux version
2.6.9-42.0.3.ELsmp (Red Hat 3.4.6-3) ` with ` PostgreSQL 8.2.0 ` that has
support for command-line execution. Not that there is anything fancy in the
code that would require such specific versions.

Unique to the code is the ability to pass in a database name, or none at all
to backup the entire cluster. This code only connects and writes files
locally. Assumes appropriate permissions given to executing user. Maybe this
works just fine for you, otherwise feel free to make your own modifications.

Personally I gzip the output, but improvements could be made to prevent hard
disk saturation on larger databases and archiving utilities.

##  crontab

    
    
    # CRON table for postgres user.
    
    # run backup every night at 22:00 hours (10PM)
    0 22 * * * /var/lib/pgsql/backups/backup.sh database_name
    
    # run backup every week at midnight hour on sunday
    0 0 * * 0 /var/lib/pgsql/backups/backup.sh
    

##  backup.sh

    
    
    #!/bin/bash
    # This script will backup the postgresql database
    # and store it in a specified directory
    
    # PARAMETERS
    # $1 database name (if none specified run pg_dumpall)
    
    # CONSTANTS
    # postgres home folder backups directory
    # !! DO NOT specify trailing '/' as it is included below for readability !!
    BACKUP_DIRECTORY="/var/lib/pgsql/backups"
    
    # Date stamp (formated YYYYMMDD)
    # just used in file name
    CURRENT_DATE=$(date "+%Y%m%d")
    
    # !!! Important pg_dump command does not export users/groups tables
    # still need to maintain a pg_dumpall for full disaster recovery !!!
    
    # this checks to see if the first command line argument is null
    if [ -z "$1" ]
    then
    # No database specified, do a full backup using pg_dumpall
    pg_dumpall | gzip - > $BACKUP_DIRECTORY/pg_dumpall_$CURRENT_DATE.sql.gz
    
    else
    # Database named (command line argument) use pg_dump for targed backup
    pg_dump $1 | gzip - > $BACKUP_DIRECTORY/$1_$CURRENT_DATE.sql.gz
    
    fi
    

Posted in Bash , Postgres | Tagged backup , cron , pgsql , pg_dump , PostgreSQL , shell script | 6 Comments 


Original post date: June 3, 2011

Category: Bash