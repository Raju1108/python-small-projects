import requests as rq
from bs4 import BeautifulSoup

url = input("Enter Link: ")
# Check if the URL starts with http or https
if "https" in url or "http" in url:
    data = rq.get(url)
else:
    data = rq.get("https://" + url)

soup = BeautifulSoup(data.text, "html.parser")
links = []

# Extract all 'href' attributes from <a> tags
for link in soup.find_all("a"):
    href = link.get("href")
    if href:  # Only add non-None values
        links.append(href)

# Save the first 10 links to a file
with open("myLinks.txt", 'a') as saved:
    print(links[:10], file=saved)

print("Links saved successfully to myLinks.txt")
