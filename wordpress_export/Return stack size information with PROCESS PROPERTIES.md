# Return stack size information with PROCESS PROPERTIES

See my [ official feature request ](http://forums.4d.fr/Post//5368969/1/) .

When executing processes that have the potential to use a large amount of
memory 4D recommends “allocating enough stack size to the process” to be
sufficient to do the job.

Well how would we know that?

I propose adding two additional return variables to [ ` PROCESS PROPERTIES `
](http://doc.4d.com/4Dv11.6/help/command/en/page336.html) . Stack Size and
Stack Utilized.

This would allow me to get a point in time measurement of what I allocated to
the process and how much the process is currently using of that allocated
stack.

>Product :4D – 4D Server  
>4D : v11 SQL r8  
>OS : Mac OS 10.5.7 or Windows

Posted in 4D , Wish List | Tagged execute on server , new process , PROCESS PROPERTIES , stack size | Leave a comment 


Original post date: March 21, 2011

Category: 4D