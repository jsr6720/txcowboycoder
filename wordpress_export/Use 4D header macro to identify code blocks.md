# Use 4D header macro to identify code blocks

Standard installation of 4Dv11 comes with a [ set of macros
](http://kb.4d.com/search/assetid=76246) to use in design mode.

The one I find most useful is the ` Header ` macro. This macro takes my name,
date time stamp, the method name and places it directly into whatever type of
method I’m working in.

Most analogous to function/class/package documentation blocks in other
languages, they are also an excellent starting point for other developers
looking at your code. In 4D specifically, header blocks also serve as
insurance against a corrupted structure file.

After repairing a corrupted structure file, [ ` orphan method(s) `
](http://kb.4d.com/search/assetid=76268) can appear without context. The
orphan methods are not linked to the original code, and the type of method
(object/form/project) and original method name are lost.

Worse, the repair process could have replaced the original code in it’s
entirety with a comment “ ` automatically repaired method ` “.

The ` method_name ` tag of the macro generates the text as shown in the title
portion of the method editor. So a project method will render ` Method:
Project_Method ` while form and object methods will render ` Method: Form
Method [Table]Form ` and ` Method: Object Method [Table].Form.Object `
respectively.

A header documents all the missing information to find the original code
location and the confidence to delete or restore the orphan code. Having the
headers in place has definitely saved me lots of time analyzing and recovering
from a structure corruption.

###  Example Macro

    
    
    <macro name="Header">
    <text>` ----------------------------------------------------
    ` User name (OS): <user_os/>
    ` Date and time: <date format="0"/>, <time format="0"/>
    ` ----------------------------------------------------
    ` Method: <method_name/>
    ` Description
    ` <caret/>
    `
    ` Parameters
    ` ----------------------------------------------------
    </text>
    

**Note** The above macro is formatted for v11. 4D v12 has ` // ` for
commenting out lines

A tech tip on creating header content automatically.  
[ 4D Tech Tip – Header Macro ](http://kb.4d.com/search/assetid=49171)

Posted in 4D | Tagged 4D , auto-comment , automatically repaired method , clean code , corrupt , macro , method header , orphan method , structure | Leave a comment 


Original post date: June 2, 2011

Category: 4D