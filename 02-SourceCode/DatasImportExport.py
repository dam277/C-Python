# import csv

# with open('couleurs.csv') as fichier_csv:
#     reader = csv.reader(fichier_csv, delimiter=';')
#     for ligne in reader:
#         print(ligne)


import csv

# with open('couleurs.csv') as fichier_csv:
#     reader = csv.DictReader(fichier_csv, delimiter=';')
#     for ligne in reader:
#         print(ligne['nom'] + " travaille en tant que " + ligne['metier'] + " et sa couleur préférée est " + ligne['couleur_preferee'])


fieldnames = ['nom', 'description', 'prix', 'quantite']
produits = [{"nom" : 'test'}, {"nom" : 'test2'}, {"nom" : 'test3'}, {"nom" : 'test4'}]
file = "toto.csv"
writer = csv.DictWriter(file, fieldnames=fieldnames)

with open('produits.csv', mode='w', newline='') as file:
    writer.wr
    for produit in produits:
        writer.writerow(produit)