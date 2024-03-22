# svn: Can’t move /.svn/tmp/entries: Operation not permitted

Another weird SVN error. I keep telling myself I need to re-checkout a clean
version of the svn repository, or better yet export to code, or even better
use git.

Regardless I found an obscure post with the solution. I had the problem again,
couldn’t find the post so here we go again. May need ` sudo ` privileges

I’ve replaced directory path with {folder root} for generic purposes.

**Error**

    
    
    $ svn commit -m "testing commit"
    svn: Commit failed (details follow):
    svn: Can't move '{folder root}/.svn/tmp/entries' to '{folder root}/.svn/entries': Operation not permitted
    

**Solution**

    
    
    $ chflags -R nouchg ./
    

What does this magic do? This changes the immutable flag on the file that
allows for editing of the hidden files. The commit should now work.

Unknown is how changing an immutable flag affects the windows system it runs
on. I am using terminal to access a samba mounted drive on ` /Volumes ` .

Posted in SVN | Tagged commit failed , svn commit , svn terminal | Leave a comment 


Original post date: January 10, 2011

Category: SVN