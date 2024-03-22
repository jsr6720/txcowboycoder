# Embedding CSS file in html e-mail

Sending html e-mails opens a whole can of worms on the many [ ways e-mail can
be viewed ](http://www.alistapart.com/articles/cssemail/) . There is also no
guarantee your e-mail will look as intended.

Instead of linking to a remote css file that may be blocked, or prompt the
user with a scary ‘prevented external content to load’ error message, we can
use PHP to pull the file directly. This adheres to the DRY principle and keeps
the code base clean.

Use the [ file_get_contents ](http://php.net/file_get_contents) function in
place of linking a style sheet via an html ` style ` element.

I would also recommend a try/catch block in case the ` file_get_contents `
command fails.

##  Solution

In head section:

```xml 12345<style type="text/css" media="screen"> <!-- we do this to embed
the file contents into the e-mail. <?php echo
file_get_contents("../common/css/blueprint/screen.css"); ?> \--></style> ```

Posted in PHP | Tagged clean code , CSS , email , embed , php | Leave a Comment » 


Original post date: July 13, 2011

Category: PHP