# 4D Database timestamp makes no sense

As part of the 4Dv11 upgrade timestamps were supposed to be included.

However once again 4D shows no developer sense in this feature:

> When pull[ing] data from a 4D data source over ODBC … be aware that when
> accessed via ODBC or SQL, the DATE field is treated as a SQL Timestamp
> field.

Really? So what should I do with my existing ODBC web code? Oh no problem,
just change your SQL statement to include ` DATE_TO_CHAR(my_field, "MM/DD/YY")
` commands. Or write a function that strips the time away from the data field.

Want to use that stored timestamp value in 4D? Forget it. No variable type of
` C_TIMESTAMP ` is available. Once again the features of the SQL engine cause
developers headache on the pure 4D side.

Maybe someday in the future 4D engineering will get the features in both
engines synchronized and making sense.

Posted in 4D | Tagged datetime , odbc , time | Leave a comment 


Original post date: January 20, 2011

Category: 4D