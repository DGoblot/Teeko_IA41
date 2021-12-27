import time


class GameJ:

    def __init__(self):
        self.plateau = [[0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0]]
        self.player = 1
        self.pions_restant = 8
        self.phase = 'Mettre'
        self.temp = 0,0

    def switchJoeur(self):
        if self.player==1:
            self.player=-1
        else:
            self.player=1

    def mettrePions(self,x,y):
        if(self.plateau[x][y]!=0):
            return  False
        else:
            self.plateau[x][y]=self.player
            self.pions_restant=self.pions_restant-1
            if self.pions_restant <= 1:
                self.verifVictoire(x, y)
            self.switchJoeur()
            if self.pions_restant == 0:
                self.phase = 'movePrendre'
            return True

    def movePionsPrendre(self, ox, oy):
        if self.plateau[ox][oy] != self.player:
            return False
        else:
            self.temp = ox,oy
            self.phase = 'movePoser'
            return True

    def movePionsPoser(self, nx, ny):
        if nx == self.temp[0] and ny == self.temp[1]:
            self.phase = 'movePrendre'
            return True
        elif self.plateau[nx][ny]!=0:
            return False
        else:
            if nx == self.temp[0] + 1 or nx == self.temp[0] - 1 or nx == self.temp[0]:
                if ny == self.temp[1] + 1 or ny == self.temp[1] - 1 or ny == self.temp[1]:
                    self.plateau[self.temp[0]][self.temp[1]] = 0
                    self.plateau[nx][ny] = self.player
                    self.verifVictoire(nx, ny)
                    self.phase = 'movePrendre'
                    self.switchJoeur()
                    return True
                else:
                    return False
            else:
                return False

    def verifVictoire(self, x, y):
        verif = self.gagner(x, y)
        if(verif[0]):
            print("Le joueur " + str(verif[1]) + " a gagné.")
            exit()

    def gagner(self, x, y):#fonction vérifiant si le pion posé déclanche une victoire
        win = False
        colonne = [self.plateau[i][y] for i in range(5)]

        if (self.player == -1):
            verif = [-1, -1, -1, -1]
            verifCarre = [-1, -1]
        else:
            verif = [1, 1, 1, 1]
            verifCarre = [1, 1]

        if (self.contient(verif, self.plateau[x])):#vérification d'une victoire en ligne
            win = True
        elif (self.contient(verif, colonne)):#vérification d'une victoire en colonne
            win = True

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
            return True, self.player
        else:
            return False, 0

    def contient(self, petite, grande):
        for i in range(len(grande) - len(petite) + 1):
            for j in range(len(petite)):
                if grande[i + j] != petite[j]:
                    break
            else:
                return True, i
        return False
