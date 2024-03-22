# 4D Delay Process should not accept negative numbers

Working on a procedure that dynamically slows or speeds itself up based on
demand.

I had wrongly assumed that [ ` Delay Process `
](http://doc.4d.com/4Dv11.6/help/command/en/page323.html) would take a
negative number and either throw an error or no longer delay the process.

Solution: check for negative numbers and pass a positive number into the `
Delay Process ` command.

    
    
    ` 4D Server v11.8 HF2
    ` Running on xserve 10.5.6
    C_LONGINT($vl_ticks_to_wait;$vl_ticks_elapsed)
    
    ` our standard is to to wait 1 second
    $vl_ticks_to_wait:=60
    
    ` but in this last cycle we took 2 seconds to execute so we don't want to
    ` pause just go into the next cycle
    $vl_ticks_elapsed:=60*2
    
    While (True)
      ` just go with the concept of a loop here
      ` I would think that this would wait a maximum of 60 ticks down to none at all
      ` but when asked to delay a negative number no error is thrown, the process
      ` just becomes permanently "Delayed"
      Delay Process(Current Process;$vl_ticks_to_wait-$vl_ticks_elapsed)
    End While
    

Posted in 4D , Wish List | Tagged 4D , delay process | Leave a comment 


Original post date: March 18, 2011

Category: 4D