# Modified({fieldname}) no longer works

4D finally did away with the Modified({fieldname}) command.

I’ve replaced it in our code base with

Old({fieldname})#fieldname

4D recommends using the Form Event and On Data Change event.

Posted in Misc | Tagged 4D | Leave a Comment » 


Original post date: March 28, 2014

Category: Misc