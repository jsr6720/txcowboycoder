# Active record find_each in batches

I wanted to iterate over an active record in batches. Found a [ great example
](http://guides.rubyonrails.org/active_record_querying.html#retrieving-
multiple-objects-in-batches) but for my needs I wanted to walk backwards over
the batch.

Needless to say it’s not possible. I don’t mind ` find_each ` limited to the
id field, but ` DESC ` would be nice.

    
    
    model.find_each(:batch_size => 200, :order => "DESC") do |instance|
      puts instance.inspect
    end
    # => You can't specify an order, it's forced to be model.id ASC
    

Posted in Ruby on Rails | Tagged find each , ruby active record | Leave a comment 


Original post date: January 13, 2011

Category: Ruby on Rails