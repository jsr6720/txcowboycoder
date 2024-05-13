from bs4 import BeautifulSoup
import markdownify
import os
import re
from datetime import datetime
import uuid

def wordpress_html_to_markdown(file_path, output_dir):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    post_divs = soup.find_all("div", class_="post")

    comments_download_later = []

    for post_div in post_divs:
        title = post_div.find("h2").get_text(strip=True)
        permalink = post_div.find("a", rel="bookmark")["href"]

        # Extract the date from postmetadata and parse it
        postmetadata = post_div.find("p", class_="postmetadata")

        # piggy-backing on known data format
        date_string = postmetadata.get_text(strip=True).split(" by ")[0]
        post_date = datetime.strptime(date_string.replace(' byJames', ''), "%B %d, %Y")
        date_formatted = post_date.strftime("%Y-%m-%d")

        # Remove the "jp-post-flair" div
        post_flair_div = post_div.find("div", id="jp-post-flair")
        if post_flair_div:
            post_flair_div.decompose()

        # make it into markdown
        post_content_div = post_div.find("div", class_="entry")
        html_content = str(post_content_div)
        markdown_content = markdownify.markdownify(html_content, heading_style="ATX")

         # Generate filename
        title_slug = re.sub(r'[\W_]+', '-', title).lower()
        filename = f"{date_formatted}-{title_slug}.md"

        # Extract the categories and tags
        post_info = post_div.find("p", class_="post-info")
        categories = [a.get_text(strip=True) for a in post_info.find_all("a", rel="category tag")] or []
        # I'm not coming back to fix this. but jekyll tags are whitespace deliminiated, not comma. Silly assumption or I can blame ChatGPT...
        tags = [a.get_text(strip=True) for a in post_info.find_all("a", rel="tag")] or []
        # also also the quotation marks do nothing to contain the strings in jekyll and tags are case-sensative
        # if for whatever reason you're using this script as a starting point you'll want to lower() remove duplicates and actually validate against jekyll docs
        tags_str = '"' + ('", "').join(tags) + '"'

        # Check for comments
        comments = post_info.find("a", href=re.compile(r'#comments'))
        has_comments = comments is not None

        if (has_comments):
            comments_download_later.append(comments)

        # jekyll metadata
        guid = str(uuid.uuid4())
        post_generated_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

               # Create Jekyll header
        jekyll_header = f"""---
layout: post
author: James Rowe
title:  "{title}"
date:   "{date_formatted} 00:00:00 -0400"
tags: wordpress txcowboycoder {tags_str}
uid: {guid}
---
"""
               # Create Jekyll footer
        jekyll_footer = f"""---

##### Author's Note

Initial `md` Generated using [https://github.com/jsr6720/wordpress-html-scraper-to-md](https://github.com/jsr6720/wordpress-html-scraper-to-md)

Original Wordpress categories: {categories}

Original Wordpress tags: {tags_str}

Original Wordpress comments: {comments}

##### Significant revisions

tags: {{{{ page.tags | join: ", " }}}} <!-- todo move this somewhere -->

- {{{{ "{post_generated_date}" | date_to_string: "ordinal", "US" }}}} Converted to jekyll markdown format and copied to personal site
- {{{{ page.date | date_to_string: "ordinal", "US" }}}} Originally published on [txcowboycoder wordpress site]({permalink})

##### EOF/Footnotes

"""
        
        # Write to file
        with open((output_dir+'/'+filename), 'w', encoding='utf-8') as md_file:
            md_file.write(f"{jekyll_header}\n\n## {title}\n\n{markdown_content}\n\n{jekyll_footer}")



    # now deal with comments by just saving them off for later
    with open('postsWithComments.txt', 'w', encoding='utf-8') as comments_file:
        comments_file.write('\n'.join(str(v) for v in comments_download_later))


# Example usage
file_path = "txCowboyCoderBlogHTML.html"
output_dir = "jekyll_posts"
os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist
wordpress_html_to_markdown(file_path, output_dir)
