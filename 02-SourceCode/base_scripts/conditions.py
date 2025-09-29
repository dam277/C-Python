condition = 1
condition_string = "one"

if condition_string == "one" :
    print("1")
elif condition == 2 :
    print("2")
else :
    print("3")
neige = False
milieu_semaine = False

if neige or milieu_semaine :
    print("on sort pas")

if not neige and not milieu_semaine :
    print("on sort")



fruit = "pomme"
match fruit:
    case "pomme":
        print("J'aime les pommes !")
    case "banane":
        print("Je n'aime pas les bananes.")
    case "orange":
        print("Les oranges sont bonnes pour la santé.")
    case _:
        print("Je ne connais pas ce fruit.")