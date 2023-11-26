races_de_chien = ["golden retriever", "chihuahua", "terrier", "carlin"]
for chien in races_de_chien:
    print(chien)

for x in range(5):
    print(f"{x} bouteilles de bières au mur !")

capacite_maximale = 10
capacite_actuelle = 3
while capacite_actuelle < capacite_maximale:
    capacite_actuelle += 1
    print(capacite_actuelle)

print("test")


for i in range(10):
    if i == 5:
        break
    print(i)


liste = [1, 2, 3, 4, 5]
# Boucle for sur la liste
for element in liste:
    if element == 3:
        # Si l'élément vaut 3, on passe à l'itération suivante sans exécuter le reste du code
        continue
    # Dans tous les autres cas, on exécute le reste du code
    print(element)