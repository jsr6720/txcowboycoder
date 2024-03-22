# Creating fields via SQL vs creating fields via structure editor

Beware when creating fields via SQL engine with 4Dv12/v11. [ Creating fields
via SQL does not allow setting field property “Map NULL values to blank
values” ](http://kb.4d.com/search/assetid=76119) . The suggested work around
is to define the field with ` NOT NULL ` constraint.

The different outcomes of the two ways to create fields is terrible behavior
because of [ lack of support for null values in the 4DDB engine
](http://txcowboycoder.wordpress.com/2011/06/07/allow-null-values-in-4db-
engine/ "Allow NULL values in 4DB engine") . 4D seems to assume developers are
either using 4D with all native code, or all SQL code, not hybrid solutions.

Ultimately the concern to the developer is having assumptions regarding the
data respected. Coming from previous version of 4D all fields have the
property checked for mapping null values to blank values. Legacy applications
can have code reliant on the assumption of no null values.

From 4D Docs on [ integrating 4D and the 4D SQL engine
](http://doc.4d.com/4Dv11.4 /help/Title/en/page370.html) :

> The NULL values are implemented in the 4D SQL language as well as in the 4D
> database engine. However, they are not supported in the 4D language

More red flags from the knowledge base:

[ Sorting fields w/NULLS changes the current selection
](http://kb.4d.com/search/assetid=75835)

> In version 11.4, if you have NULL values in any field and then do an ORDER
> BY on that field, any records that contain NULL values will be removed from
> the Current Selection.

Also [ displaying ](http://kb.4d.com/search/assetid=76069) and saving null
values to the database is even more difficult.

###  Create field via structure

By default the “Map NULL values to blank values” field property is enabled.  
![](/images/create_field_structure.png)

###  Create field via SQL

This field was created with ` NOT NULL ` constraint.  
![](/images/create_field_sql.png)

Posted in 4D | Tagged 4D , null , sql , v11 , v12 | Leave a comment 


Original post date: June 8, 2011

Category: 4D