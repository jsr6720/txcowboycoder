# Define constants without a plugin

Would be nice if there were a way to define constants for use in 4D without
creating a plugin. There is an [ outstanding feature request
](http://forums.4d.fr/Post//1470873/1/4687683) for this already.

Logically I would think defining them in the ` On Server Startup ` database
method would be a good place for them. Or having it as part of the explorer
menu options.

Code could look like this if defined programatically:

    
    
    ` we want a constant for use throughout 4D
    C_{datatype}_CONSTANT("Constant name";value)
    

Posted in Wish List | Tagged 4D constants , plugin | Leave a comment 


Original post date: November 18, 2010

Category: Wish List