# Rubies for the holidays

Over the last two weeks I have been taking vacation and diving head first into
my [ first major ruby language project
](http://txcowboycoder.wordpress.com/2011/01/07/request-tracker-to-redmine-
migration/) .

Having never programed ruby before my gut reaction to the language is one
word: awesome.

The only drawback to it is my own misunderstanding of the limits to the
‘magic’ of ruby. I definitely fell prey to some PHP-esque syntax that is no
longer necessary.

My favorite so far: whatever is at the end of the action is returned.

    
    
    # never mind that this is built it
    def even (number)
      number % 2
    end
    
    @attr = even(2) {|r| r ? r : nil}
    

Biggest suprise: ` nil ` is an object and ` nil.id ` is ` 4 `

At any rate, programming a rake task in a ror application ( [ Redmine
](http://www.redmine.org) ) has been a fun and interesting challenge. I look
forward to using ruby more in my problem solving and application building
experiences.

Posted in Personal Musings | Tagged ror , ruby | Leave a comment 


Original post date: January 6, 2011

Category: Personal Musings