from requests import get

resultat = get("https://www.youtube.com/watch?v=95oWfc9l6lY&list=TLPQMjUxMTIwMjPax-fhD_CeFA&index=10")
print(resultat.content)