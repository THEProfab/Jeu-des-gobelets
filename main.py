import re
import random

def affichageGrille(grille):
    for ligne in grille:
        for case in ligne:
            print(case, end="|")
        print()
        print("-+-+-+-+")
    print()

def validationGobelet(choixGobelet):
    if (choixGobelet!="p" or choixGobelet!="m" or choixGobelet!="g"):
        while (choixGobelet!="p" and choixGobelet!="m" and choixGobelet!="g"):
            choixGobelet = input("Veuillez choisir une taille valide (p, m ou g) : ")
    return choixGobelet

def peutJouer(joueurs, joueur, grille, valeursGobelets):
    # si le joueur n'a plus de gobelets, il ne peut plus jouer
    if (joueurs[tourDe]["petits"]==0 and joueurs[tourDe]["moyens"]==0 and joueurs[tourDe]["grands"]==0):
        return False

    # récupération de la plus petite valeur de gobelet présente dans la grille
    minValGrille = 3
    for ligne in range(1, len(grille)):
        for colonne in range(1, len(grille[ligne])):
            case = grille[ligne][colonne]
            if (case in valeursGobelets[1].keys()):
                if (valeursGobelets[1][case] < minValGrille):
                    minValGrille = valeursGobelets[1][case]
            elif (case in valeursGobelets[2].keys()):
                if (valeursGobelets[2][case] < minValGrille):
                    minValGrille = valeursGobelets[2][case]

    # récupération de la plus grande valeur de gobelet encore disponible pour le joueur
    clesJoueur = list(joueurs[joueur].keys())
    maxValDispoJoueur = 0
    for cle in clesJoueur:
        if (joueurs[joueur][cle]>0):
            valeur = valeursGobelets[joueur][representationGobelets[joueur][cle]]
            if (valeur > maxValDispoJoueur):
                maxValDispoJoueur = valeur

    # si la plus grande valeur de gobelet disponible pour le joueur est supérieure à celle la moins élevée de la grille, le joueur peut jouer sinon il ne peut plus
    if (maxValDispoJoueur > minValGrille):
        return True
    return False

def choixCase(grille, valeurGobeletChoisi, valeursGobelets):
    choixLigne = input("Choisissez la ligne de la grille où vous souhaitez placer votre gobelet (1 à 3) : ")

    # le choix de la ligne doit être un chiffre entre 1 et 3 pour être valide
    if (not(re.fullmatch('[1-3]', choixLigne))):
        while (not(re.fullmatch('[1-3]', choixLigne))):
            choixLigne = input("Veuillez choisir un numéro de ligne valide (1 à 3) : ")

    choixColonne = input("Choisissez la colonne de la grille où vous souhaitez placer votre gobelet (1 à 3) : ")

    # le choix de la colonne doit être un chiffre entre 1 et 3 pour être valide
    if (not(re.fullmatch('[1-3]', choixColonne))):
        while (not(re.fullmatch('[1-3]', choixColonne))):
            choixColonne = input("Veuillez choisir un numéro de colonne valide (1 à 3) : ")

    # on convertit les str en int pour pouvoir les utiliser comme index
    choixLigne = int(choixLigne)
    choixColonne = int(choixColonne)
    caseChoisie = grille[choixLigne][choixColonne]

    if (caseChoisie in valeursGobelets[1].keys()):
        valeurCaseChoisie = valeursGobelets[1][caseChoisie]
    elif (caseChoisie in valeursGobelets[2].keys()):
        valeurCaseChoisie = valeursGobelets[2][caseChoisie]

    if (valeurCaseChoisie >= valeurGobeletChoisi):
        print("Le gobelet choisi est plus petit que celui déjà présent sur la case choisie ! Veuillez choisir une autre case.")
        print()
        return choixCase(grille, valeurGobeletChoisi, valeursGobelets)
    else:
        return (choixLigne, choixColonne)

def gagne(joueurs, joueur, grille, representationGobelets):
    gobeletsJoueur = representationGobelets[joueur].values()
    taille = len(grille)

    # vérification sur les lignes
    for ligne in range(1, taille):
        gagne = True
        for colonne in range(1, taille):
            if (grille[ligne][colonne] not in gobeletsJoueur):
                gagne = False
                break
        if gagne:
            return gagne

    # vérification sur les colonnes
    for ligne in range(1, taille):
        gagne = True
        for colonne in range(1, taille):
            if (grille[colonne][ligne] not in gobeletsJoueur):
                gagne = False
                break
        if gagne:
            return gagne

    # vérification sur la diagonale descendante
    gagne = True
    for ligne in range(1, taille):
        if grille[ligne][ligne] not in gobeletsJoueur:
            gagne = False
            break
    if gagne:
        return gagne

    # vérification sur la diagonale ascendante
    gagne = True
    for ligne in range(1, taille):
        if grille[ligne][taille - ligne] not in gobeletsJoueur:
            gagne = False
            break
    if gagne:
        return gagne

    return False


print("Bienvenue dans le jeu des gobelets !")
print()
print("1) Nouvelle partie")
print("2) Options")
print("3) Crédits")
print("4) Quitter")
print()

choix = input("Entrez le chiffre correspondant à votre choix : ")
print()

while (choix!="4"):
    if (choix=="1"):
        print("Nouvelle partie :")
        print()
        file = open("options.txt", "r")
        lines = file.readlines()
        file.close()

        for line in lines:
            splited = line.split(" ")
            if (splited[0]=="Nombre"):
                nbJoueurs = splited[3].replace("\n", "") #on enlève le caractère de saut de ligne
            elif (splited[0]=="IA"):
                niveauIA = splited[2].replace("\n", "")

        grille = [[" ", "1", "2", "3"], ["1", " ", " ", " "], ["2", " ", " ", " "], ["3", " ", " ", " "]]
        joueurs = {1: {"petits": 2, "moyens": 3, "grands": 2}, 2: {"petits": 2, "moyens": 3, "grands": 2}}
        equivalenceGobelets = {"p": "petits", "m": "moyens", "g": "grands"}
        valeursGobelets = {1: {" ": 0, ".": 1, "x": 2, "X": 3}, 2: {" ": 0, "o": 1, "O": 2, "0": 3}}
        representationGobelets = {1: {"petits": ".", "moyens": "x", "grands": "X"}, 2: {"petits": "o", "moyens": "O", "grands": "0"}}

        print("Joueur 1 :", joueurs[1]["petits"], "petit(s) gobelet(s),", joueurs[1]["moyens"], "moyen(s) gobelet(s) et", joueurs[1]["grands"],"grand(s) gobelet(s).")
        print("Joueur 2 :", joueurs[2]["petits"], "petit(s) gobelet(s),", joueurs[2]["moyens"], "moyen(s) gobelet(s) et", joueurs[2]["grands"],"grand(s) gobelet(s).")
        print()

        affichageGrille(grille)
        tourDe = 1

        while (True):
            print("C'est au tour du Joueur",tourDe,"!")

            if (peutJouer(joueurs, tourDe, grille, valeursGobelets)):
                # jeu lors d'une partie 2 joueurs ou 1 joueur lors du tour de l'humain
                if (nbJoueurs=="2" or (nbJoueurs=="1" and tourDe==1)):
                    choixGobelet = input("Choisissez la taille du gobelet à poser (p, m ou g) : ")
                    choixGobelet = validationGobelet(choixGobelet)

                    if (joueurs[tourDe][equivalenceGobelets[choixGobelet]]==0):
                        while (joueurs[tourDe][equivalenceGobelets[choixGobelet]]==0):
                            choixGobelet = input("Vous ne possédez plus de ce type de gobelets, veuillez en choisir un autre type (p, m ou g) : ")
                            choixGobelet = validationGobelet(choixGobelet)

                    tailleGobelet = equivalenceGobelets[choixGobelet]
                    choixGobelet = representationGobelets[tourDe][tailleGobelet]
                    valeurGobeletChoisi = valeursGobelets[tourDe][choixGobelet]

                    caseChoisie = choixCase(grille, valeurGobeletChoisi, valeursGobelets)
                    grille[caseChoisie[0]][caseChoisie[1]] = choixGobelet

                else:
                    if (niveauIA == "Simple"):
                        # récupération de la plus grande valeur de gobelet encore disponible
                        clesJoueur = list(joueurs[2].keys())
                        maxValDispo = 0
                        for cle in clesJoueur:
                            if (joueurs[2][cle]>0):
                                valeur = valeursGobelets[2][representationGobelets[2][cle]]
                                if (valeur > maxValDispo):
                                    maxValDispo = valeur

                        # on fait une liste de toutes les cases sur lesquelles l'IA peut jouer (si la valeur de la case est trop élevée par rapport aux gobelets restants de l'IA, cette case n'est pas ajoutée)
                        casesValables = []
                        for ligne in range(1,len(grille)):
                            for colonne in range(1,len(grille[ligne])):
                                if (grille[ligne][colonne] in valeursGobelets[1].keys()):
                                    if (valeursGobelets[1][grille[ligne][colonne]] < maxValDispo):
                                        casesValables.append([ligne, colonne, valeursGobelets[1][grille[ligne][colonne]]])

                        caseChoisie = random.choice(casesValables)

                        # on place le gobelet de valeur +1 par rapport à la valeur de la case choisie sur cette dernière
                        for cle in valeursGobelets[2].keys():
                            if (valeursGobelets[2][cle]==caseChoisie[2]+1):
                                choixGobelet = cle
                                grille[caseChoisie[0]][caseChoisie[1]] = cle

                        # on récupère la taille du gobelet joué pour pouvoir l'enlever des gobelets de l'IA
                        for cle in representationGobelets[2].keys():
                            if (representationGobelets[2][cle]==choixGobelet):
                                tailleGobelet = cle

                    elif (niveauIA == "Avancée"):
                        print("Pas implémenté")
                        break

                joueurs[tourDe].update({tailleGobelet: joueurs[tourDe][tailleGobelet]-1}) # on enlève 1 au nombre de gobelets restants du type que le joueur vient de placer

            else:
                print("Vous ne pouvez pas jouer, vous passez votre tour !")

            print()
            print("Joueur 1 :", joueurs[1]["petits"], "petit(s) gobelet(s),", joueurs[1]["moyens"], "moyen(s) gobelet(s) et", joueurs[1]["grands"],"grand(s) gobelet(s).")
            print("Joueur 2 :", joueurs[2]["petits"], "petit(s) gobelet(s),", joueurs[2]["moyens"], "moyen(s) gobelet(s) et", joueurs[2]["grands"],"grand(s) gobelet(s).")
            print()
            affichageGrille(grille)

            if (gagne(joueurs, 1, grille, representationGobelets)):
                print("Le Joueur 1 a gagné !")
                break
            elif (gagne(joueurs, 2, grille, representationGobelets)):
                print("Le Joueur 2 a gagné !")
                break

            if (not(peutJouer(joueurs, 1, grille, valeursGobelets)) and not(peutJouer(joueurs, 2, grille, valeursGobelets))):
                print("Égalité, les deux joueurs ne peuvent plus jouer !")
                break

            if (tourDe==1):
                tourDe=2
            else:
                tourDe=1

    elif (choix=="2"):
        print("Options :")
        print("1) Type de jeu")
        print("2) IA")
        print("3) Retour")
        print()

        choixOptions = input("Entrez le chiffre correspondant à votre choix : ")
        print()

        while (choixOptions!="3"):
            if (choixOptions=="1"):
                print("Type de jeu :")
                print("1) Un joueur")
                print("2) Deux joueurs")
                print()
            elif (choixOptions=="2"):
                print("IA")
                print("1) Simple")
                print("2) Avancée")
                print()
            else:
                print("Votre choix est invalide !") #Si l'utilisateur entre un mauvais choix, retour au premier menu pour ne pas toucher au fichier d'options
                break

            choixType = input("Entrez le chiffre correspondant à votre choix : ")

            file = open("options.txt", "r")
            lines = file.readlines() #on récupère tout le fichier d'options
            file.close()

            file = open("options.txt", "w")
            for line in lines:
                splited = line.split(" ")
                if (splited[0]=="Nombre" and choixOptions=="1"): #Selon les choix faits, la bonne modification est effecuée
                    if (choixType=="1"):
                        splited[3] = "1\n"
                    elif (choixType=="2"):
                        splited[3] = "2\n"
                elif (splited[0]=="IA" and choixOptions=="2"):
                    if (choixType=="1"):
                        splited[2] = "Simple\n"
                    elif (choixType=="2"):
                        splited[2] = "Avancée\n"
                line = " ".join(splited)
                file.write(line)
            file.close()

            print()
            print("Options :")
            print("1) Type de jeu")
            print("2) IA")
            print("3) Retour")
            print()

            choixOptions = input("Entrez le chiffre correspondant à votre choix : ")
            print()

    elif (choix=="3"):
        print("Crédits :")
        print("Développeur : Marc BAYART")
        print("Version de Python utilisée : 3.10")
        print("Bibliothèques utilisées (internes) : random et re")
    else:
        print("Votre choix est invalide !")

    print()
    print("Bienvenue dans le jeu des gobelets !")
    print()
    print("1) Nouvelle partie")
    print("2) Options")
    print("3) Crédits")
    print("4) Quitter")
    print()

    choix = input("Entrez le chiffre correspondant à votre choix : ")
    print()
