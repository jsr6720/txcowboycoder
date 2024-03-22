# Keep code base clean – avoid unnecessary variable assignments

Can’t tell you how frustrating it is to find the context of a variable
stripped away by a [ meaningless re-assgiment
](http://my.safaribooksonline.com/book/software-engineering-and-
development/agile-development/9780136083238/meaningful-names/18) (login
required).

From Clean Code: A Handbook of Agile Software Craftsmanship:

> The name of a variable, function, or class, should answer all the big
> questions. It  
>  should tell you why it exists, what it does, and how it is used

```php 123456// doing this totally strips away any meaningful
context$my_temp_variable = $employee_salaries[$an_employee_name];$gross_salary
= $bonus_factor * $my_temp_variable; // hopefully the language constructs
allow full variable interaction$gross_salary = $bonus_factor *
$employee_salaries["Fred"] ```

Advertisement

Posted in Clean Code | Tagged clean code , temp variables | Leave a Comment » 


Original post date: July 14, 2011

Category: Clean Code