class GameJ:

    def __init__(self):
        self.plateau = [[0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0]]
        self.player = 1
        self.pions_restant = 8

    def affichePl(self):
        for i in range(0,5):
            for j in range(0,5):
                print(str(self.plateau[i][j])+" ", end =" ")

            print("")
            print("--------------")

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
            return  True

    def movePions(self,ox,oy,nx,ny):
        if self.plateau[ox][oy]==0 :
            return False
        else:
            if nx == ox + 1 or nx == ox - 1 or nx == ox:
                if ny == oy or ny == oy + 1 or ny == oy - 1:
                    if self.plateau[nx][ny] == 0:
                        self.plateau[ox][oy] = 0
                        self.plateau[nx][ny] = self.player
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

    def jouer(self):
        while True:
            p.affichePl()
            print("Le joueur numero " +str(self.player) + " va jouer.")
            if (self.pions_restant == 0):
                print("Modifier la position de quel pion ?")
                while True:
                    print("Donner un ox et un oy")

                    ox = int(input())
                    oy = int(input())
                    if (ox >= 0 and ox < 5) and (oy >= 0 and oy < 5) and self.plateau[ox][oy]==self.player:
                        break
                    else:
                        print("ox ou oy incorrect")
                print("Quelle nouvelle position ?")
                while True:
                    print("Donner un nx et un ny")
                    nx = int(input())
                    ny = int(input())
                    if (nx >= 0 and nx < 5) and (ny >= 0 and ny < 5) and self.movePions(ox,oy,nx,ny) :
                        verif = self.gagner(nx,ny)
                        if(verif[0]):
                            print("Le joueur " + str(verif[1]) + " a gagné.")
                            exit()
                        self.switchJoeur()
                        break
                    else:
                        print("nx ou ny incorrect")

            else:
                while True:
                    print("Donner un x et un y")

                    x = int(input())
                    y = int(input())
                    if (x >= 0 and x < 5) and (y >= 0 and y < 5) and self.mettrePions(x,y):
                        verif = self.gagner(x,y)
                        if(verif[0]):
                            print("Le joueur " + str(verif[1]) + " a gagné.")
                            exit()
                        self.switchJoeur()
                        break
                    else:
                        print("x ou y incorrect")

    def gagner(self, x, y):#fonction vérifiant si le pion posé déclanche une victoire
        win = False
        colonne = [self.plateau[i][y] for i in range(5)]
        verif = [1, 1, 1, 1]
        verifCarre = [1, 1]
        if (self.player == -1):
            verif = [-1, -1, -1, -1]
            verifCarre = [-1, -1]

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

p=GameJ()

p.jouer()