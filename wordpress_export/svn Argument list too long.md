# svn: Argument list too long

Recently I needed to add thousands of files to an existing repository, but
every time I tried ` svn add * ` or the ` svn import ` functionality I got the
error:

` svn: Argument list too long `

I finally found help with [ this link ](http://www.arraystudio.com/as-
workshop/how-to-add-multiple-files-to-subversion.html) but it did not work
with file names with spaces.

So below I take the substring of the output in spaces and ? from the whole
line before adding the file.

    
    
    svn status | grep "^?" | awk '{ print substr($0,9,length($0))}' | while read f; do svn add "$f"; done
    

I’m sure more can be done to make this better, but this did the job I needed.
For example using ` ls ` to import to svn would be helpful. For now this only
works when ` svn status ` can be executed.

I think ` find ` is the best way to do this, with regex support; but again I
just hacked my way to the finish line.

Posted in SVN | Tagged svn add , terminal | Leave a comment 


Original post date: November 29, 2010

Category: SVN