def bixestile(annee):
    """
    Check if it's a leap year return a boolean
    """
    return ((annee % 4 == 0) and (annee % 100 != 0)) or (annee % 400 == 0)


def calcul_joue_de_semaine():
    """
    coding the methode 3 from 
    https://fr.wikibooks.org/wiki/Curiosit%C3%A9s_math%C3%A9matiques/Trouver_le_jour_de_la_semaine_avec_une_date_donn%C3%A9e#M%C3%A9thode_3

    to check what day it was at any date given in "(DD/MM/AAAA)" format

    """
    valeur_mois = {"01": 0, "02": 3, "03": 3, "04": 6, "05": 1,
                   "06": 4, "07": 6, "08": 2, "09": 5, "10": 0, "11": 3, "12": 5}
    valeur_siecle = {"16": 6, "17": 4, "18": 2, "19": 0, "20": 6, "21": 4}
    nom_mois = {"01": "Janvier", "02": "Février", "03": "Mars", "04": "Avril", "05": "Mai", "06": "Juin",
                "07": "Juillet", "08": "Août", "09": "Septembre", "10": "Octobre", "11": "Novembre", "12": "Décembre"}
    jour_de_la_semaine = {0: "Dimanche", 1: "Lundi", 2: "Mardi",
                          3: "Mercredi", 4: "Jeudi", 5: "Vendredi", 6: "Samedi"}

    date = str(input("entre l'année (JJ/MM/AAAA)"))

#     calculate : (2 last digit of year + (two last digit of year)//4 + month (in digit)
#                  + the value according to the month)
    total = (int)(date[8:])+((int)(date[8:])//4) + \
        (int)(date[:2])+valeur_mois[date[3:5]]

#     check if it's a leap year and if it's january of february, and substract 1 if it's true
    if bixestile((int)(date[6:])) and (date[3:5] == "01" or date[3:5] == "02"):
        total -= 1
#         add value according to century
    total += valeur_siecle[date[6:8]]

#     keeping the rest of a division
    total = total % 7

#     check i it's a 1st of a month and change the print if that's the case
    if date[:2] == "01":
        print("Le 1er ", nom_mois[date[3:5]], " ",
              date[6:], " était un ", jour_de_la_semaine[total])
    else:
        print("Le ", date[:2], " ", nom_mois[date[3:5]], " ",
              date[6:], " était un ", jour_de_la_semaine[total])


calcul_joue_de_semaine()
