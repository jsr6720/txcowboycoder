# Get last month’s date range in PHP

I needed to get last month’s valid date range in php for running reports. A
quick google search showed the top results for accomplishing this used ` for `
loops that subtracted/added days from now until casting as a date object
returned false.

Needless to say, no way am I doing that. So below I have a code snippet that
returns the valid start and end date of the previous month. This could be
modified in a variety of ways to suit your needs. Needless to say I was
disappointed that ` strtotime ` did not accept “First day of last month”.

```php 12345678910// this returns a date string which I need, but removing the
casting as a date// returns a unix timestamp value more useful for
calculations$first_of_last_month =
date('m/d/y',mktime(0,0,0,date('m')-1,1,date('y')));$end_of_last_month =
date('m/d/y',mktime(0,0,0,date('m'),0,date('y'))); // if run on
03/01/11var_dump($first_of_last_month, $end_of_last_month);// outputs//
string(8) "02/01/11"// string(8) "02/28/11" ```

Posted in PHP | Tagged date , monthly date range , php | 2 Comments 


Original post date: February 10, 2011

Category: PHP