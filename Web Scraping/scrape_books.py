# Working with Multiple Pages and Items
import requests
import bs4

# GOAL: Get the title of every book with a 2 star rating

# Let's show a more realistic example of scraping a full site. The website: http://books.toscrape.com/index.html is specifically designed for people to scrape it. 
# Let's try to get the title of every book that has a 2 star rating and at the end just have a Python list with all their titles.
# We will do the following:

# 1. Figure out the URL structure to go through every page
# 2. Scrap every page in the catalogue
# 3. Figure out what tag/class represents the Star rating
# 4. Filter by that star rating using an if statement
# 5. Store the results to a list



# We can see that the URL structure is the following:
# http://books.toscrape.com/catalogue/page-1.html

# Home Page
"https://books.toscrape.com/catalogue/page-1.html"
# Page 2:
"http://books.toscrape.com/catalogue/page-2.html"
# Page 3:
"http://books.toscrape.com/catalogue/page-3.html"

# Page 1
page = 1
base_url = f"https://books.toscrape.com/catalogue/page-{page}.html"

# Start

res = requests.get(base_url)

# Now let's grab the products (books) from the get request result:
soup = bs4.BeautifulSoup(res.text, "lxml")
#print(soup)

# Now we can see that each book has the product_pod class. We can select any tag with this class, and then further reduce it by its rating.
products = soup.select(".product_pod")
#print(products)

# At the website, it states that: 1000 results - showing 1 to 20
# So, the len of the products being equal to 20 is consistent.
# Each of the product_pod is associated with one of the books.
#print(len(products))



# Manuel Example

example = products[0]
#print((example))
#print(type(example))
#print(example.attrs)

# Does the Book have 2 Stars or Not

# Now by inspecting the site we can see that the class we want is class='star-rating Two', 
# if you click on this in your browser, you'll notice it displays the space as a . , so that means we want to search for ".star-rating.Two"

# 1) First Approach 
#print("star-rating Two" in str(example))
#print("star-rating Three" in str(example))

# 2) Second Approach (Formal)
#example_two_stars = example.select(".star-rating.Two")
#print(example_two_stars)

#example_three_stars = example.select(".star-rating.Three")
#print(example_three_stars)

# Finding the Title When We Have a 2-Star Match

title = example.select("a")[1]["title"]

# Combine All
two_star_titles = []

# Iterate each page
for i in range(1, 51):
    page = i
    res = requests.get(base_url)

    soup = bs4.BeautifulSoup(res.text, "lxml")
    books = soup.select(".product_pod")

    # Iterate each book in a page
    for book in books:
        if len(book.select(".star-rating.Two")) != 0:
            two_star_titles.append(book.select('a')[1]['title'])

print(two_star_titles)