import os
import requests
from bs4 import BeautifulSoup
from html2text import html2text
from sanitize_filename import sanitize
from urllib.parse import urlparse

# todo
## use the tempalte file to generate jekyll markdown
## actually get the code blocks in play
## find things with comments #comments">1 Comment</a>
## flatten category and tags into one array
## see if gpt4 does anything different with image capture


# Function to strip tags but keep text
def strip_tags_but_keep_text(element):
    for tag in element.find_all():
        tag.unwrap()

# Specify the path to your local HTML file
html_file_path = "./txCowboyCoderBlogHTML.html"

# Create a directory to store the exported Markdown files
output_dir = "./wordpress_export"
os.makedirs(output_dir, exist_ok=True)

# Read the local HTML file
with open(html_file_path, "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Find all a tags that wrap img tags
for a_tag in soup.find_all('a'):
    img_tag = a_tag.find('img')
    if img_tag:
        # Replace the a tag with its contents (the img tag)
        a_tag.replace_with(img_tag)

# Find all <div> elements with the pattern id="post-*"
div_elements = soup.find_all("div", id=lambda value: value and value.startswith("post-"))

# Iterate over each matching <div> element and export it to a Markdown file
for i, div_element in enumerate(div_elements):
    file_name = f"post-{i+1}.md"

    # Find the <div> element with class "posttitle"
    post_title_div = div_element.find("div", class_="posttitle")
    if post_title_div:
        # Extract the link text and convert it to a Markdown heading
        link_text = post_title_div.a.text.strip()
        markdown_heading = f"# {link_text}"

        #get a safe file name
        file_name = sanitize(link_text)

        post_date = post_title_div.p.text.strip().replace(' by James','')

        # Replace the post title div with the Markdown heading
        post_title_div.replace_with(markdown_heading)

    # Remove the div with id="jp-post-flair" if it exists
    post_flair_div = div_element.find("div", id="jp-post-flair")
    if post_flair_div:
        post_flair_div.decompose()

    # extract category and tags and remove
    post_info_p = div_element.find("p", {"class": "post-info"})
    post_info_a = post_info_p.find_all("a")
    post_category = post_info_a[0].text.strip()

    # now clean up that post title section
    strip_tags_but_keep_text(post_info_p)

    # Find all <img> elements
    imgs = div_element.find_all("img")
    for img_dom in imgs:
        # get the title and alt attributes and redirect link to local
        img_file_name = urlparse(img_dom.get("src")).path.split("/")[-1]
        # reset source to local
        img_dom["src"] = "/images/" + img_file_name

    # Find all <div> elements with class "syntaxhighlighter"
    code_divs = div_element.find_all("div", class_="syntaxhighlighter")
    for code_div in code_divs:
        # Extract the language and code from the code div
        language = code_div.get("class")[1]
        code = code_div.text.strip()

        # Create the Markdown code block with language specified
        markdown_code = f"""```{language}
        {code}
        ```
        """

        # Replace the code div with the Markdown code block
        code_div.replace_with(markdown_code)

    # Convert the HTML content to Markdown
    markdown_content = html2text(div_element.prettify())
    markdown_content = markdown_content + '\nOriginal post date: ' + post_date
    markdown_content = markdown_content + '\n\nCategory: ' + post_category

    # Generate a filename based on the index
    filename = f"{file_name}.md"

    # Save the <div> content to a Markdown file
    output_path = os.path.join(output_dir, filename)
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(markdown_content)
