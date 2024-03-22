# Use CAST in 4D volatile SQL statements

Hint, to avoid hair pulling use the 4D function [ ` CAST `
](http://doc.4d.com/4Dv12.1/help/Title/en/page18321.html) to explicitly type [
data types ](http://doc.4d.com/4Dv12.1/help/Title/en/page18465.html) in 4D SQL
statements.

Consider the following for boolean field [ODBCTest]FieldBoolean.

    
    
    // 4Dv12.1 sees this as a string assignment to boolean
    // FieldBoolean = true throws an unfound column error
    Begin SQL
    	UPDATE ODBCTest
    	SET FieldBoolean = 'true'
    	WHERE id=29168
    End SQL
    

This will throw error 1108:

    
    
    Error code: 1108
    Operation VK_STRING  = VK_BOOLEAN  is not type safe.
    component: 'SQLS'
    task 11, name: 'P_2'
    

However, using ` CAST ` will give us the desired result.

    
    
    // also works: CAST(1 as BOOLEAN)
    Begin SQL
    	UPDATE ODBCTest
    	SET FieldBoolean =CAST( 'true' as BOOLEAN)
    	WHERE id=29168
    End SQL
    

Of course it would be nice if [ 4D compiler could detect these
](http://txcowboycoder.wordpress.com/2011/04/25/compiler-warning-on-possible-
loss-of-precision/ "Compiler warning on possible loss of precision") types of
problems before they occur.

Posted in 4D | Tagged 4D , CAST , data types , Error code: 1108 , sql | 1 Comment 


Original post date: April 26, 2011

Category: 4D