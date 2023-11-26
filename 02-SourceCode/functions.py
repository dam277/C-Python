def afficher_message():
    print("Bonjour, comment ça va ?")


afficher_message()


def afficher_nom_prenom(nom, prenom):
    """
    Cette fonction calc {nom}
    """
    print("Nom :", nom)
    print("Prénom :", prenom)

afficher_nom_prenom("Loup", "Damien")


def calculer_somme(a, b):
  resultat = a + b
  return resultat, a, b

somme = calculer_somme(2, 3)
print(somme) #Ce print affichera 5


help(afficher_nom_prenom)





while True:
    try:
        x = int(input("Entrez un nombre entier : "))
        break
    except ValueError:
        print("Oops ! Ce n'est pas un nombre entier. Essayez encore...")