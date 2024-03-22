# SVN client/server version mismatch

Not a huge deal, but I spent a while fighting with various svn errors and
finally figured it out.

Unlike distributed VCS, svn relies on clients and a server repo to handle
source code. So if a svn 1.3.1 client checks out code the .svn folders are
created using that version.

When a 1.6.11 svn client comes a long and tries to do an update from a 1.6.11
server repo the svn client major differences can cause problems.

Such as:

  * ` log entry missing 'name' attribute `
  * ` svn: Error processing command 'rm' `

Posted in SVN | Leave a comment 


Original post date: December 15, 2010

Category: SVN