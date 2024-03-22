# txcowboycoder
Wordpress export from old personal blog that I no longer have email/password for. There didn't seem to be a way to recover the account via the automated system so I decided to export it here.

https://txcowboycoder.wordpress.com/

## Problem approach

Loaded my old wordpress site, that wordpress.com has hosting for free (ads) since 2010(?), and decided that unlike my teenage geocities site I was going to save this content.

Since it's not much content I used infinate scroll to load all my posts and then ```view rendered source``` to 'download' [txCowboyCoderBlogHTML.html](./txCowboyCoderBlogHTML.html) and used that as my starting point to parse with a python script into ```md``` format files for posterity.

## Top posts (allegedly)

- Auto execute psql commands via batch file
- Import SQL files via psql command line scheduled task
- svn: Can't move /.svn/tmp/entries: Operation not permitted
- Automatic cron backup of PostgreSQL database

## Why github?

Well its another free hosting site and I wanted an excuse to play with python/chatGPT

Also, obligatory https://xkcd.com/979/ a small note that most of these posts are circa 2010-2011. To add context, I recall at that time online resources were paywalled ExpertsExchange and StackOverflow had only been in operation for ~2 years with not much content on 4D.

Most of my 4D and PHP posts came from mailing lists and [phpBB](https://www.phpbb.com/)(?) forums.

I had joined GitHub late 2010 but used this blog to publish thoughts. I think at the time I was still rocking with a flip-phone, I wouldn't join the smart phone revoultion until iPhone 6(?)

## But why one big script file

Because I'm doing this once. Procedurally...

```
python ./wordpressDownloadImages.py
python ./wordpress.py
```