class GameJ:

    # La valeur 0 dans le plateau indique qu'il n'a pas de pion
    # La valeur 1 c'est le peon du joueur 1
    # La valeur -1 c'est le peon du joueur 2 / robot

    # player c'est pour indique qu'
    def __init__(self):
        self.plateau = [[0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
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

    def gagner(self, x, y):#fonction vérifiant si le pion posé déclanche une victoire
        win = False
        colonne = [self.plateau[i][y] for i in range(5)]
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
            if(x == y):
                if(self.contient(verif,[diag[i] for i, diag in enumerate(self.plateau)])):
                    win = True
            if(x+y == 4):
                if(self.contient(verif,[diag[-i-1] for i, diag in enumerate(self.plateau)])):#vérification sur les deux grandes diagonales
                    win = True
            if(x == y-1):
                petiteDiag = []
                for i in range(4):
                    petiteDiag.append(self.plateau[i][i+1])
                if(self.contient(verif,petiteDiag)):
                    win = True
            if(x == y+1):
                petiteDiag = []
                for i in range(4):
                    petiteDiag.append(self.plateau[i+1][i])
                if(self.contient(verif,petiteDiag)):
                    win = True
            if(x+y == 3):
                petiteDiag = []
                for i in range(4):
                    petiteDiag.append(self.plateau[3-i][i])
                if(self.contient(verif,petiteDiag)):
                    win = True
            if(x+y == 5):
                petiteDiag = []
                for i in range(4):
                    petiteDiag.append(self.plateau[4-i][i+1])
                if(self.contient(verif,petiteDiag)):
                    win = True

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

# p=PlateauJ()
# p.affichePl()
