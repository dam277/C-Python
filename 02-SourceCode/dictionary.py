nouvelle_campagne = {
"responsable_de_campagne": "Jeanne d'Arc",
"nom_de_campagne": "Campagne nous aimons les chiens",
"date_de_début": "01/01/2020",
"influenceurs_importants": ["@MonAmourDeChien", "@MeilleuresFriandisesPourChiens"]
}
print(nouvelle_campagne)

taux_de_conversion = {}
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2
print(taux_de_conversion)
taux_de_conversion = dict()
taux_de_conversion['twitter'] = 3.4
taux_de_conversion['snapchat'] = 1.2
print(taux_de_conversion)

# Savoir si une clef existe dans le dictionnaire
if "twitter" in taux_de_conversion:
    print(True)
else :
    print(False)

print(taux_de_conversion.get("twitter"))
