# This month’s date range

I noticed that many people search for ‘this month’s date range’. The trick
lies in knowing which month you want to go to and that [ mktime
](http://us.php.net/mktime) can automatically find the end of the month by
passing 0 into the day field.

Well in no short order here it is:

```php 123456789// casting as date object, otherwise it returns a unix
timestamp$first_of_this_month =
date('m/d/y',mktime(0,0,0,date('m'),1,date('y')));$end_of_this_month =
date('m/d/y',mktime(0,0,0,date('m')+1,0,date('y'))); // if run on
4/01/11var_dump($first_of_this_month,$end_of_this_month);// outputs//
string(8) "04/01/11"// string(8) "04/30/11" ```

Posted in PHP | Tagged date range , php 5.3 | Leave a comment 


Original post date: April 1, 2011

Category: PHP