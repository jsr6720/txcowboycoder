# 4D DSN-less ODBC connection

Took me forever to figure this out because the docs out there for 4D are
minimal.

Easy configuration of multiple data sources is crucial if you want to use
CodeIgniter or any other framework that allows configuration files to control
the deployment and connection to various databases.

```nogutter // get the connection resource$connect = odbc_connect('DRIVER={4D
v11 ODBC
Driver};SSL=false;SERVER=192.168.1.100;PORT=19812;UID=user;PWD=password',"","");
```

I played with various different ways of doing this connection string, and
found the above the most straight forward. You can leave password blank if
there isn’t one.

Now if only they would make a linux odbc driver…

Posted in 4D | Tagged 4D ODBC driver , DSN | 7 Comments 


Original post date: March 30, 2011

Category: 4D