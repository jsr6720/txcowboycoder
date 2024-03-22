# Clear empty object methods to avoid developer confusion

Part of working with any code base is understanding what is already developed.
Luckily [ shields ](http://kb.4d.com/search/assetid=37121) help show actions
associated with objects in the form editor. However, an object method shield
will show for empty (‘blank’) object methods. We should clear any empty object
methods to avoid confusion and optimize the code base.

###  Example

Two objects on a form, both with an object method shield indicating the
presence of an object method.

![two objects with method shield](/images/object_methods.png)

The last developer removed the object method content from the ` variable `
input area but did not explicitly clear the object method. This falsely
indicates object method content, and worse yet 4D will execute the blank
object method for [ each event enabled
](./toggle-off-4d-form-events-for-
easier-debugging/ "Toggle off 4D form events for easier debugging") on that
object.

The best approach is to [ clear the object method
](http://kb.4d.com/search/assetid=33479 "4D Tech Tip - Clear Object Method")
so that no shield displays, and reduce the number of lines the 4D engine
executes.

###  Solution

![](/images/object_menu_clear.png)  
Select the object to clear the method from, then from the ` Object ` drop down
menu select ` Clear Object Method `

###  Results

No misleading shields and no more tracing through empty object method.  
![Object method cleared](/images/object_cleared.png)

Posted in 4D | Tagged 4D , clean code , object method , optimization , shield | Leave a comment 


Original post date: May 25, 2011

Category: 4D