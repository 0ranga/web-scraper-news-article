import requests
import sys
from bs4 import BeautifulSoup

arguments_from_CLI = sys.argv


# r = requests.get("https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/")
r = requests.get(arguments_from_CLI[1])

html_doc = r.text
soup = BeautifulSoup(html_doc, 'html.parser')

title = soup.select('[data-qa="headline-text"]')[0].text
author = soup.select('[data-qa="author-name"]')[0].text
date = soup.select('[data-qa="display-date"]')[0].text
content = soup.find_all(class_="article-body")[0]
content = content.get_text(separator=' ')


print(f"Title of article is:\n{title}\n")
print(f"{author} wrote this article on {date}. \n\nContent of article:\n")
print(content)