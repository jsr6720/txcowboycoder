# 4D based mirror component – take two

My first attempt to [ mirror data
](./mirroring-data-to-another-
database/) from 4D to another database didn’t work. So, I’m taking another
crack at it with lessons learned from my previous attempt.

My aim now is to make a component that will be transaction safe, and model
itself after the 4D KB article published about [ Synchronization and
Replication in v12 ](http://kb.4d.com/search/assetid=76224) (4D partner login
required). Since I am still using v11 and a v12 upgrade is not on the horizon,
I am taking my own approach.

**Component**

Allow definition of multiple ‘mirror preferences’. Each of these linkages
would define:

tables and fields to mirror  
-> table pk field name   
-> table last updated date/time field names   
-> boolean field name to escape mirroring (so you can accept changes to the mirrored database and write them back without mirroring them out again)   
interval to execute at  
service to utilize (soap, file, sql, plugin)  
last run date/time

@todo build synchronization of table/field names via alter table

**Process**

On the defined interval, or manually, the server process would spawn processes
to look at target tables for updated/new records (making it transaction safe)
and then of the records that were updated send over the target data.

Feel free to take it and run with it. Feedback and your thoughts welcome.

Say is there a market for companies that want to have their data available in
a SQL database of repute?

More post to follow.

Posted in 4D | Tagged 4d component , mirroring , v11 | Leave a comment 


Original post date: January 28, 2011

Category: 4D