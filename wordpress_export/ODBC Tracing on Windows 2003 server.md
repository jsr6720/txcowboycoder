# ODBC Tracing on Windows 2003 server

Trying to diagnose a connection rejection problem by using the [ trace odbc
](http://support.microsoft.com/kb/274551) call functionality in windows.

What they kb article doesn’t mention is that you have to restart the IIS Admin
service to get it to start writing to the log file. Or restart the box. Also,
make sure you have permissions to write to the target directory, and that the
appropriate user is targeted that is connecting via ODBC.

Posted in Misc | Tagged odbc , odbc tracing , windows server | Leave a comment 


Original post date: January 26, 2011

Category: Misc