# Epoch/Unix timestamp command

Would really like to have a timestamp command that could return the number of
seconds elapsed since epoch.

4D commands ` Milliseconds ` and ` Tickcount ` return the time elapsed for the
current process.

SQL functions ` CURRENT_TIMESTAMP ` and ` CURTIME ` return HH:MM:SS not
seconds elapsed. (Never mind the apparent lack of a naming convention)

    
    
    C_LONGINT($seconds_since_epoch)
    ` Time is currently a command that requires parameters
    ` lets change it so no params = unix timestamp
    $seconds_since_epoch:=Time
    

Posted in Wish List | Tagged epoch , timestamp , time_t | Leave a comment 


Original post date: January 19, 2011

Category: Wish List