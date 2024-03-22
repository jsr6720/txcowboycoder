# 4D Log Event command and log level importance

I began experimenting with the 4D command [ ` LOG EVENT `
](http://doc.4d.com/4D-Language-Reference-12.1/System-Environment/LOG-
EVENT.301-479440.en.html) .

The documentation states the third parameter, importance, is optional. I’ve
never used console before, but I had to assign the importance parameter to `
Error Message ` for it to show in my console.

` Information Message ` (default) and ` Warning Message ` did not show.

    
    
    ` this works
    LOG EVENT(Into 4D Debug Message ;"My message";Error Message )
    
    ` using the default does not
    LOG EVENT(Into 4D Debug Message ;"Does not work" )
    

Posted in 4D | Tagged console , log event , mac console | Leave a comment 


Original post date: March 8, 2011

Category: 4D