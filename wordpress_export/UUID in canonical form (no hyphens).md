# UUID in canonical form (no hyphens)

4D v12 has a new function ` [ Generate UUID ](http://doc.4d.com/4D-Language-
Reference-12/Tools/Generate-UUID.301-186324.en.html) ` . This is a much
welcome feature, but fails to return an UUID in canonical (with hyphens) form
like everyone else.

It would appear that 4D has UUIDs for everything it stores internally
(structure export as xml) without hyphens. 4D has no comment on why it has
chosen to have ` Generate UUID ` return a UUID without hyphens.

Further, in v12 using the “UUID format” on an alpha field removes the
capability to set the length of said field. If I copy a UUID with hyphens, it
strips them out to save them to 32 length string.

4D says there is no benefit, other than convenience, from having an UUID field
and a 36 char alpha field with a trigger that stores UUID via ` Generate UUID
` into it.

Finally, the documentation says to refer to the design reference manual for
v12 for more information. Which isn’t out as of the time of this writing.

Posted in Wish List | Tagged 4D , UUID | Leave a comment 


Original post date: October 26, 2010

Category: Wish List