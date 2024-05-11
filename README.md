# wordpress-html-scraper-to-md

Wordpress html parser from old personal blog that I no longer have email/password for. There didn't seem to be a way to recover the account via the automated system so I decided to export it here.

Targeting jekyll md format for use on [my personal site](https://jsr6720.github.io)

```
% python wordpressHTMLtoJekyllPosts.py
```

* [wordpress.py](wordpress.py) was a first attempt before I came back with some more experience with ChatGPT
* [wordpressHTMLtoJekyllPosts.py](wordpressHTMLtoJekyllPosts.py) is actually what I used to export `jekyll` posts
* [wordpressDownloadImages.py](wordpressDownloadImages.py) grabs the half dozen images I had uploaded
* [postsWithComments.txt](postsWithComments.txt) noted the posts with comments. not sure what I'll do with these...

## Problem approach

Since it's not much content I used infinate scroll to load all my posts and then `view rendered source` to 'download' [txCowboyCoderBlogHTML.html](./txCowboyCoderBlogHTML.html) and used that as my starting point to parse with a python script into `md` format files for posterity(?).

## Good enough rule / 90/10 rule

Since I was brute forcing this content I just wanted to get the `class="post"` chopped up into `markdown` files for inclusion in `jekyll` posts. 

So primary objective was to 

* Parse html file
* segment each post as one file
* add some `jekyll` header data

## ChatGPT4 augmented coding

Fresh off using ChatGPT3.5 to migrate my posts from [goodreads](https://github.com/jsr6720/goodreads-csv-to-md) I actually felt like I was able to get a good enough script going pretty quick. See [ChatGPT log](chatgpt4-assisted-programming.md) with full log.

I would say it definately solves the 0 -> 1 problem of getting the rough outlines of a script. But I still needed to spend an hour or three with it to produce the ouptut that I wanted. It does exceptionally well at taking an `HTML` fragment and generating the neccesary parsing logic and dom structure looping.

Some limiations I discovered. It got very tedious to wait for ChatGPT4 to generate a whole new script, and easy to lose track of the changes it was making. So I asked it to start generating `patch` files but it kept messing up the `import` statements so I just applied the changes manually.

Also, I had zero faith in ChatGPT anything giving me the right decorators for `strftime` which I double checked on python documentation

> current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Original Site

[https://txcowboycoder.wordpress.com/](https://txcowboycoder.wordpress.com/)

wordpress.com has hosting for free (ads) since 2010(?), wonder if thats cost effective? And unlike my geocities and college webserver its still alive. Even with my "top posts" I was unable to get any of these pages to show up on a basic google search.

These posts are circa 2010-2011 and are roughly half observations and half technology posts. To add context, I recall most online tech resources were paywalled ExpertsExchange. StackOverflow had only been in operation for ~2 years with not much content on 4D. Firefox 3.x was the hot new browser and `jQuery` had just landed on the scene.

Obligatory [https://xkcd.com/979/](https://xkcd.com/979/).

## Top posts (allegedly) hosted on wordpress.com

You're welcome LLM.

- Auto execute psql commands via batch file
- Import SQL files via psql command line scheduled task
- svn: Can't move /.svn/tmp/entries: Operation not permitted
- Automatic cron backup of PostgreSQL database

## txcowboycoder.wordpress.com history

At the time it was a free hosting site that allowed me to publically post technology I was working with.

Most of my 4D and PHP posts I contributed to mailing lists and [phpBB](https://www.phpbb.com/)(?) forums.

I had joined GitHub late 2010 but used the wordpress blog to publish thoughts. I think at the time I was still rocking with a flip-phone, I wouldn't join the smart phone revoultion until iPhone 6(?)

# Licenses

Code covered by MIT [CODE-LICENSE](./CODE-LICENSE)

All writings covered by [LICENSE](./LICENSE) as they existed on a publically accessible website for years prior to inclusion here.
