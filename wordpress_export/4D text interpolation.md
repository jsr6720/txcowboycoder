# 4D text interpolation

For text string building I am very fond of php’s interpolate feature:

```php 1234# my variable$name = "Joe Bob";# my command$my_sentence = "Hello
{$name}!"; ```

In 4D the same can be accomplished with text objects.

    
    
    `have a table [Table]full_name
    ` this is the typed string for the text
    ` notice the "<" and ">" enclosing the field reference
    vt_object:="Hello <[Table]full_name>!"
    ` outputs "Hello Joe Bob!" assuming that was what was loaded in the record
    

Posted in 4D | Tagged 4d text object , interpolate , tip | Leave a comment 


Original post date: March 11, 2011

Category: 4D