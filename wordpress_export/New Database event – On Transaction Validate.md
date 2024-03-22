# New Database event – On Transaction Validate

Right now there is no event thrown for VALIDATE/CANCEL transaction. I would
like Database event to also return “On validate transaction” and “On cancel
transaction”.

Why you ask? Because triggers are executed inside a transaction block, but if
I want to know when the transaction ended I have to write application layer
code for something 4D should know when it ended

So even though you can tell if you are in a transaction and what level the
transaction is at, you can never tell when that transaction has completed in a
trigger.

Vote for the [ feature request here
](http://forums.4d.fr/Post/EN/4622327/1/4622328) .

Posted in Wish List | Tagged 4D , database event , transaction | Leave a comment 


Original post date: November 4, 2010

Category: Wish List