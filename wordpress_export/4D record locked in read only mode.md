# 4D record locked in read only mode

Was doing a bit of 4D v11 programming when I discovered this conundrum. I
found it to be confusing, but maybe it makes perfect sense to everyone else.

When showing a record to a user with the table in read only mode, 4D returns `
True ` for ` LOCKED ` even though ` LOCKED ATTRIBUTES ` returns nothing. This
occurs only when using ` LOAD RECORD ` with a table in read only mode.

I would expect that 4D would not see this as a locked record, or return system
information for ` LOCKED ATTRIBUTES ` . Further, when another process accesses
this record in read write mode, 4D does not report this record to be locked,
and it can be loaded modified and saved.

    
    
    ` "Save" button on a form in READ ONLY mode
    ` record is displayed in variables
    ` with DIALOG command
    
    C_LONGINT($Event)
    $Event:=Form event
    
    Case of
    	: ($Event=On Clicked )
    		  ` first we need to make sure we can load the record
    		  ` I would expect 4D to return false, since the table is in read only mode
    		If (Not(Locked([Table])))
    			  ` map the variables back to data values
    			[Table]data:=v_data
    		Else
    			` instead I end up here with results 0, "", "", "" respectively
    			LOCKED ATTRIBUTES([Table];$process;$4d_user;$session_user;$process_name)
    		End if
    
    End case
    

However, if ` UNLOAD RECORD ` is execute after getting the data into variables
the record is no longer ` LOCKED `

Posted in 4D | Tagged 4D v11 , locked record , read only mode | Leave a comment 


Original post date: March 2, 2011

Category: 4D