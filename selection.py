import requests
from bs4 import BeautifulSoup


response = requests.get(
    "https://travel.ettoday.net/category/%E6%A1%83%E5%9C%92/%22")

soup = BeautifulSoup(response.text, "html.parser")

# How to extract content by using Keyword Argument

# Extract content from Website
# print(soup.prettify())

# result = soup.find("h3")
# print(result)

#  Extract content by 1 Keyword Argument and limit to 1
# result1 = soup.find_all("h3", itemprop= "headline", limit=1)
# print(result1)

# Extract content by 2 Keyword Argument and limit to 2
# result2 = soup.find_all(["h3","p"],limit= 2)
# print(result2)


# result = soup.find("div", itemprop = "itemListElement")
# print(result.select("a"))

# # Extract content by using CSS Keyword Argument
# titles = soup.find("p", class_ = "summary")
# print(titles)
#
# #Extract content by using CSS 2 Keyword Argument
# titles = soup.find_all("p", class_ = "summary", limit = 2)
# print(titles)

# Extract content by using find_parents
# result = soup.find("a",itemprop = "url")
# parents = result.find_parents("h3")
# print(parents)

# Extract Title and URL From Homepage
# titles = soup.find_all("h3", itemprop = "headline")
# for title in titles:
#     print(title.select_one("a"))

# Extract URL From Above Content
# titles = soup.find_all("h3", itemprop = "headline")
# for title in titles:
#     print(title.select_one("a").get("href"))

# Extract Title From Above Content Seperately
titles = soup.find_all("h3", itemprop="headline")
for title in titles:
    print(title.select_one("a").getText())









