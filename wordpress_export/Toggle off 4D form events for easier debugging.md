# Toggle off 4D form events for easier debugging

**Default Setup**  
![default form events](/images/default_form_events.png)

When creating a new form in 4D v11 it comes with a range of events ‘enabled’
(see figure). I’m assuming this is for ease of development.

However, I advocate for turning off all events first and then [ enabling
specific events ](./encapsulate-
formobject-methods-with-form-event-case-statements/ "Encapsulate form/object
methods with form event case statements") on an as needed basis.

4D will go into each form method and object method that has the event enabled
and execute the method. When debugging this can be a real hassle because each
event will trigger even if there is no ‘real’ code executed. 4D can’t tell
what is in your methods and is just throwing events that the developer has
specified.

###  Example

Consider a simple form with a drop down chooser and two buttons. The form
level ` On Click ` event does not have to be enabled for the object to throw
the same event. However if there is code in the form method that is not
protected by a form event case statement it will be executed in addition to
the object method.

**Form Design View**

![simple form](/images/simple_form.png)

**Form method**

    
    
    ` executes on load and on click and whatever other events are triggered
    ` set a default choice for the array aTable (drop down chooser)
    aTables:=aTables{1}
    

**Object method**

    
    
    ` executes on click
    vTable_Chosen:=aTables
    

The object method goes first and gets the table name, but then the form method
‘resets’ the array location back to the first pointer. Moral of the story,
wrap your code.

Posted in 4D | Tagged 4D , 4Dv11 , clean code , debugger , event , form event | 2 Comments 


Original post date: May 2, 2011

Category: 4D