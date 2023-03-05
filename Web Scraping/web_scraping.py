# Web Scraping 
import requests
import bs4

# 1) Grabbing the Title of a Page

# Use the requests library to grab the page

res = requests.get("http://www.example.com")

# This object is a requests.models.Response object.
# It contains the information from the website.

print(type(res))
print(res.text)

# Use BeautifulSoup library to analyze the extracted page

# Technically we could use our own custom script to loook for items in the string of res.text
# However, the BeautifulSoup library already has lots of built-in tools and methods to grab information from a string of this nature (basically an HTML file). 
# Using BeautifulSoup we can create a "soup" object that contains all the "ingredients" of the webpage. 
soup = bs4.BeautifulSoup(res.text, "lxml")
print(soup)

# Let's use the .select() method to grab elements

# We're looking for the "title" tage, so we'll pass in "title"
# Notice what is reutned here. It is a list containing all the title elements (along with their tags).
# You can use indexing or even looping to grab the elements from the list. Since this object is still a specialized tag, we can use method calls to grab just the text.
title_tag = soup.select("title")
""" 
print(title_tag)
print(title_tag[0])
print(type(title_tag[0]))
"""

site_paragraphs = soup.select("p")

# Use the .getText() method to grab the string
print(title_tag[0].getText())
print(site_paragraphs[0].getText())



# 2) Grabbing all elements of a class

# Let's try to grab all the section headings of the Wikipedia Article on Grace Hopper from this URL: https://en.wikipedia.org/wiki/Grace_Hopper
# First get the request
res2 = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
# Create a soup from requests
soup2 = bs4.BeautifulSoup(res2.text, "lxml")

# Now its time to figure out what we are actually looking for. 
# Inspect the element on the page to see that the section headers have the class "mw-headline". 
# Because this is a class and not a straight tag, we need to adhere to some syntax for CSS. 

print(soup2.select(".toctext"))

for item in soup2.select(".toctext"):
    print(item.text)



# 3) Getting an Image from a Website
# Let's attempt to grab the image of the Deep Blue Computer from this wikipedia article:  https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)

res3 = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")

soup3 = bs4.BeautifulSoup(res3.text, "lxml")
image_info = soup3.select(".thumbimage")

print(image_info)
len(image_info)

computer = image_info[0]
print(type(computer))

# You can make dictionary like calls for parts of the Tag.
# In this case, we are interested in the src , or "source" of the image, which should be its own .jpg or .png link:
comp_src_link = computer["src"]
print(comp_src_link)

# Now that you have the actual src link, you can grab the image with requests and get along with the .content attribute. 
# Note how we had to add https:// before the link, if you don't do this, requests will complain (but it gives you a pretty descriptive error code).
image_link = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png")

# The raw content (its a binary file, meaning we will need to use binary read/write methods for saving it)
print(image_link.content)

# Let's write this to a file.
# Note the 'wb' call to denote a binary writing of the file
f = open("/Users/aliemirkaragulle/Desktop/scraped_image.png", "wb")
f.write(image_link.content)
f.close()