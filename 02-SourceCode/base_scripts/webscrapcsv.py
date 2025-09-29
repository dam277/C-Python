import requests
from bs4 import BeautifulSoup
import csv


# récupère les links ou title comme liste de strings
def extraire_donnees(elements):
	resultat = []
	for element in elements:
		resultat.append(element.string)

	print(resultat)
	return resultat


# charger la donnée dans un fichier csv
def charger_donnees(nom_fichier, en_tete, links, title):
	with open(nom_fichier, 'w') as fichier_csv:
		writer = csv.writer(fichier_csv, delimiter=';')
		writer.writerow(en_tete)

		print(links, title)
		# zip permet d'itérer sur deux listes à la fois
		for link in links:
			print(link)
			writer.writerow([link, "lol"])

def etl():
	# lien de la page à scrapper
	url = "http://localhost:1311"
	reponse = requests.get(url)
	page = reponse.content

	# transforme (parse) le HTML en objet BeautifulSoup
	soup = BeautifulSoup(page, "html.parser")

	# récupération de tous les titres
	links = soup.find_all("a", class_="race")
	# récupération de toutes les title
	title = soup.find_all("p", class_="title")

	en_tete = ["title", "description"]
	links = extraire_donnees(links)
	title = extraire_donnees(title)
	charger_donnees("data.csv", en_tete, links, title)


etl()

