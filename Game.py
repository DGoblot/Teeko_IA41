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

    def gagner(self, x, y):
        win = False
        colonne = [self.plateau[i][y] for i in range(len(self.plateau))]
        verif = [1, 1, 1, 1]
        verifCarre = [1, 1]
        if (self.player == -1):
            verif = [-1, -1, -1, -1]
            verifCarre = [-1, -1]

        print(verif)

        if (self.contient(verif, self.plateau[x])):
            win = True

        elif (self.contient(verif, colonne)):
            win = True
            print(self.contient(verif, colonne))

        elif (self.contient(verifCarre, self.plateau[x])):
            carreInfo1 = self.contient(verifCarre, self.plateau[x])
            if (x != 0):
                carreInfo2 = self.contient(verifCarre, self.plateau[x-1])
                if (carreInfo2 and carreInfo1[1] == carreInfo2[1]):
                    win = True
            if (x != len(self.plateau) - 1):
                carreInfo2 = self.contient(verifCarre, self.plateau[x+1])
                if (carreInfo2 and carreInfo1[1] == carreInfo2[1]):
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

    def presquegagner(self):
        pass

    def jouer(self):
        pass


test = GameJ()
test.__init__()
print(test.gagner(1, 4))
# p=PlateauJ()
# p.affichePl()
