from bs4 import BeautifulSoup
import markdownify
import os
import re
from datetime import datetime

def wordpress_html_to_markdown(file_path, output_dir):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    post_divs = soup.find_all("div", class_="post")

    print(post_divs)
    for post_div in post_divs:
        title = post_div.find("h2").get_text(strip=True)
        permalink = post_div.find("a", rel="bookmark")["href"]

        # Extract the date from postmetadata and parse it
        postmetadata = post_div.find("p", class_="postmetadata")

        # piggy-backing on known data format
        date_string = postmetadata.get_text(strip=True).split(" by ")[0]
        post_date = datetime.strptime(date_string.replace(' byJames', ''), "%B %d, %Y")
        date_formatted = post_date.strftime("%Y-%m-%d")

        post_content_div = post_div.find("div", class_="entry")
        html_content = str(post_content_div)
        markdown_content = markdownify.markdownify(html_content, heading_style="ATX")

         # Generate filename
        title_slug = re.sub(r'[\W_]+', '-', title).lower()
        filename = f"{date_formatted}-{title_slug}.md"
        
        # Write to file
        with open([filename,output_dir].join('/'), 'w', encoding='utf-8') as md_file:
            md_file.write(f"# {title}\n\n[Permanent Link]({permalink})\n\n{markdown_content}")


# Example usage
file_path = "txCowboyCoderBlogHTML.html"
output_dir = "jekyll_posts"
os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist
wordpress_html_to_markdown(file_path, output_dir)