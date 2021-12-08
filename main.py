print("Bienvenue dans le jeu des gobelets !")
print()
print("1) Nouvelle partie")
print("2) Options")
print("3) Crédits")
print("4) Quitter")
print()

choix = int(input("Entrez le chiffre correspondant à votre choix : "))
print()

while (choix!=4):
    if (choix==1):
        print("Nouvelle partie")
    elif (choix==2):
        print("Options :")
        print("1) Type de jeu")
        print("2) IA")
        print("3) Retour")
        print()

        choixOptions = int(input("Entrez le chiffre correspondant à votre choix : "))
        print()

        while (choixOptions!=3):
            if (choixOptions==1):
                print("Type de jeu :")
                print("1) Un joueur")
                print("2) Deux joueurs")
                print()
            elif (choixOptions==2):
                print("IA")
                print("1) Simple")
                print("2) Avancée")
                print()
            else:
                print("Votre choix est invalide !") #Si l'utilisateur entre un mauvais choix, retour au premier menu pour ne pas toucher au fichier d'options
                break

            choixType = int(input("Entrez le chiffre correspondant à votre choix : "))

            file = open("options.txt", "r")
            lines = file.readlines() #on récupère tout le fichier d'options
            file.close()

            file = open("options.txt", "w")
            for line in lines:
                splited = line.split(" ")
                if (splited[0]=="Nombre" and choixOptions==1): #Selon les choix faits, la bonne modification est effecuée
                    if (choixType==1):
                        splited[3] = "1\n"
                    elif (choixType==2):
                        splited[3] = "2\n"
                elif (splited[0]=="IA" and choixOptions==2):
                    if (choixType==1):
                        splited[2] = "Simple\n"
                    elif (choixType==2):
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

            choixOptions = int(input("Entrez le chiffre correspondant à votre choix : "))
            print()

    elif (choix==3):
        print("Crédits :")
        print("Développeur : Marc BAYART")
        print("Version de Python utilisée : 3.10")
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

    choix = int(input("Entrez le chiffre correspondant à votre choix : "))
    print()
