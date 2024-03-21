"""
File: wordpressDownloadImages.py
Author: ChatGPT 3.5
Description: This script just rips the original images into a directory so I can link them
"""

import os
import requests
from bs4 import BeautifulSoup

# Specify the path to your local HTML file
html_file_path = "./txCowboyCoderBlogHTML.html"

# Read the local HTML file
with open(html_file_path, "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Find all image elements on the page
img_tags = soup.find_all("img", {"data-orig-file": True})

# Iterate over each image element and download the images
for img_tag in img_tags:
    # Extract the image URL
    image_url = img_tag["data-orig-file"]
    
    # Send a GET request to the image URL
    image_response = requests.get(image_url)
    
    # Check if the request was successful
    if image_response.status_code == 200:
        # Extract the filename from the URL
        filename = os.path.basename(image_url)
        
        # Specify the path where you want to save the image
        save_path = os.path.join("images", filename)
        
        # Write the image data to the file
        with open(save_path, "wb") as f:
            f.write(image_response.content)
        
        print(f"Image '{filename}' downloaded successfully.")
    else:
        print(f"Failed to download the image from '{image_url}'.")
