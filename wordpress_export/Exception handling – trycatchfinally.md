# Exception handling – try/catch/finally

I know there is the ` ON ERR CALL ` but personally I think that fragments the
code into separate methods. Having a concept of ` THROWS ` would be icing on
the cake.

I’m not advocating the removal of ` ON ERR CALL ` but I would love to just do
something like below for simple try/catch concepts.

I suppose this type of concept is available with 4Dv12 and PHP, but not
natively.

    
    
    ` this is my method that is called when ANY error is thrown
    ON ERR CALL("catch error")
    
    ` throws error which goes into "catch error" method call
    $result:=Create document($1) ` none specified
    

Posted in Wish List | Tagged 4D , programming structure , try catch | Leave a comment 


Original post date: October 21, 2010

Category: Wish List