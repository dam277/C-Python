from requests import get
from bs4 import BeautifulSoup

# resultat = get("https://www.youtube.com/watch?v=95oWfc9l6lY&list=TLPQMjUxMTIwMjPax-fhD_CeFA&index=10")
# print(resultat.text)


url = "http://localhost:121"
page = get(url)
soup = BeautifulSoup(page.content, "html.parser")

# Voir le code html source
#print(soup)

print(soup.title)
print(soup.find_all("a", class_="race"))