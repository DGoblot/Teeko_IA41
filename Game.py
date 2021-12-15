class GameJ:

    # La valeur 0 dans le plateau indique qu'il n'a pas de pion
    # La valeur 1 c'est le peon du joueur 1
    # La valeur -1 c'est le peon du joueur 2 / robot

    # player c'est pour indique qu'
    def __init__(self):
        self.plateau = [[0, 0, 0, 1, 1],
                        [0, 0, 0, 1, 1],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0]]
        self.player = 1
        self.pions_restant = 8

    def affichePl(self):
        for i in range(0, 5):
            for j in range(0, 5):
                print(str(self.plateau[i][j]) + " ", end=" ")

            print("")
            print("--------------")

    def switchJoueur(self):
        if self.player == 1:
            self.player = -1
        else:
            self.player = 1

    def mettrePions(self, x, y):
        if (self.plateau[x][y] != 0):
            return False
        else:
            self.plateau[x][y] = self.player
            self.switchJoueur()
            self.pions_restant = self.pions_restant - 1
        pass

    def movePions(self):
        pass

    def gagner(self, x, y):#fonction vérifiant si le pion posé déclanche une victoire
        win = False
        colonne = [self.plateau[i][y] for i in range(len(self.plateau))]
        verif = [1, 1, 1, 1]
        verifCarre = [1, 1]
        if (self.player == -1):
            verif = [-1, -1, -1, -1]
            verifCarre = [-1, -1]

        print(verif)

        if (self.contient(verif, self.plateau[x])):#vérification d'une victoire en ligne
            win = True

        elif (self.contient(verif, colonne)):#vérification d'une victoire en colonne
            win = True
            print(self.contient(verif, colonne))

        elif (self.contient(verifCarre, self.plateau[x])):#vérification d'une victoire en carré
            carreInfo1 = self.contient(verifCarre, self.plateau[x])
            if (x != 0):
                carreInfo2 = self.contient(verifCarre, self.plateau[x-1])
                if (carreInfo2 and carreInfo1[1] == carreInfo2[1]):
                    win = True
            if (x != len(self.plateau) - 1):
                carreInfo2 = self.contient(verifCarre, self.plateau[x+1])
                if (carreInfo2 and carreInfo1[1] == carreInfo2[1]):
                    win = True
        else:#verification d'une victoire en diagonale
            if(x == y and self.contient(verif,[diag[i] for i, diag in enumerate(test.plateau)])):
                win = True
            elif(x+y == len(self.plateau) and self.contient(verif,[diag[-i-1] for i, diag in enumerate(test.plateau)])):#vérification sur les deux grandes diagonales
                win = True
        #TODO ajouter les verif diagonales manquantes
        






        if (win == True):
            return self.player
        else:
            return 0

    def contient(self, petite, grande):
        for i in range(len(grande) - len(petite) + 1):
            for j in range(len(petite)):
                if grande[i + j] != petite[j]:
                    break
            else:
                return True, i
        return False

    def presquegagner(self):
        pass

    def jouer(self):
        pass


test = GameJ()
test.__init__()
print(test.gagner(1, 4))
# p=PlateauJ()
# p.affichePl()
