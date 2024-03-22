# Ruby Rakefile auto executes includes

When the custom [ rake task
](./request-tracker-to-redmine-
migration/) to migrate data from one system to another was implemented our
cron job stopped working.

It looked like it was trying to execute the contents of the custom rake file
every time a call to ` rake -f Rakefile ` was made.

The problem ended up being Redmine’s Rakefile was set to include all defined
task in a ` {root}/lib/tasks ` directory. Anything not in a namespace was
executing regardless of the rake task called.

**Custom rake task**

    
    
    # code here executes all the time
    puts 'I execute ever time rake -f Rakefile RAILS_ENV="{env}" is executed'
    
    namespace :redmine do
      desc "Migrate from RT3 to Redmine"
      task :a_task  => :environment do
        # code here only executes when it's called
        puts 'I execute only when my namespace:task is invoked rake -f Rakefile redmine:a_task RAILS_ENV="{env}" is executed'
       end
    end
    

**Redmine’s Rakefile**

    
    
    # Add your own tasks in files placed in lib/tasks ending in .rake,
    # for example lib/tasks/switchtower.rake, and they will automatically be available to Rake.
    
    require(File.join(File.dirname(__FILE__), 'config', 'boot'))
    
    require 'rake'
    require 'rake/testtask'
    require 'rake/rdoctask'
    
    require 'tasks/rails'
    

Posted in Ruby | Tagged namespace , rake | Leave a comment 


Original post date: January 17, 2011

Category: Ruby