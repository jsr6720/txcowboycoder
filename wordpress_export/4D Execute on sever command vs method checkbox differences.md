# 4D Execute on sever command vs method checkbox differences

I was troubleshooting some long executing code when I discovered the
difference between ` Execute on server ` command and it’s sibling checkbox in
the method properties.

What you need to know:

**Use checkbox** if you care about the results of the executed code, you want
the server to handle the processing and don’t care that the client waits for
the response.

**Use command** to detach the wait from the client and process the code
asynchronously.

I won’t go into much detail as it is well documented, but if you do some deep
reading.

**Tim Penner on “Command vs. Property”**

> One important difference is that the **_Execute on Server_ ** command always
> creates a new process, whether it is called in Client/Server mode or in
> single-user mode; the **_Execute on Server_ ** command still creates a new
> process.
>
> In contrast the _Execute on Server_ method attribute will not create a new
> process on the server, but will instead use a “twin” process of the client
> process that requested the execution. In Single-user mode, this method
> property has no affect and the method runs in the same process that
> requested its execution.

**More Information**  
Execute on Server attribute:  
[ http://www.4d.com/docs/CMU/CMU40945.HTM
](http://www.4d.com/docs/CMU/CMU40945.HTM)  
Execute on Server command:  
[ http://www.4d.com/docs/CMU/CMU00373.HTM
](http://www.4d.com/docs/CMU/CMU00373.HTM)  
Stored Procedures:  
[ http://www.4d.com/docs/CMU/CMU40975.HTM
](http://www.4d.com/docs/CMU/CMU40975.HTM)

Posted in 4D | Tagged 4D , execute on server , stored procedure | Leave a comment 


Original post date: January 31, 2011

Category: 4D