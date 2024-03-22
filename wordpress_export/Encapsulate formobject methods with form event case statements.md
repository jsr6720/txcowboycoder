# Encapsulate form/object methods with form event case statements

Clean code principle: run targeted code only once, even if multiple executions
won’t ‘hurt anything’.

Make sure of this in 4D by encapsulating code with a ` Case of ` targeting
specific events and turn off unneeded events.

    
    
    C_LONGINT($vl_form_event)
    $vl_form_event:=Form event
    
    Case of
    	: ($vl_form_event=On Load )  ` or other event
    		  ` do code here
    	Else
    		  ` should not have this event enabled then
    
    End case
    

This provides clarity on what code is to execute for the specified event. It
also prevents code from [ executing multiple times
](./toggle-off-4d-form-events-for-
easier-debugging/ "Toggle off 4D form events for easier debugging") if new
events are selected for a form/object. I.e. enabling ` On Load ` with implicit
` On Click ` code already existing in the method.

I don’t type this every time I want to trap events. So I put the following in
my [ macro file ](http://doc.4d.com/4Dv12.1/help/Title/en/page1034.html) .

    
    
    <macro name="CaseOf Form event">
    	<text>
    		C_LONGINT($vl_form_event)
    		$vl_form_event:=Form event
    
    		Case of
    			: ($vl_form_event=<caret/> )
    				<selection/>
    		End case
    	</text>
    </macro>
    

***Note** the above macro does not generate the given source, its just a
starting point.

Posted in 4D | Tagged 4D , 4D v11 , case of , clean code , form event , macro | 1 Comment 


Original post date: May 3, 2011

Category: 4D