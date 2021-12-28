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

    def mettrePions(self,l,c):
        if(self.plateau[l][c]!=0):
            return  False
        else:
            self.plateau[l][c]=self.player
            self.pions_restant=self.pions_restant-1
            self.switchJoeur()
            return  True

    def moviePionsRobot(self,ol,oc,nl,nc,p):
        if nl == ol + 1 or nl == ol - 1 or nl == ol:
            if nc == oc or nc == oc + 1 or nc == oc - 1:
                if self.plateau[nl][nc] == 0:
                    self.plateau[ol][oc] = 0
                    self.plateau[nl][nc] = p

                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


    def movePions(self,ol,oc,nl,nc):
        if self.plateau[ol][oc]==0 :
            return False
        else:
            if nl == ol + 1 or nl == ol - 1 or nl == ol:
                if nc == oc or nc == oc + 1 or nc == oc - 1:
                    if self.plateau[nl][nc] == 0:
                        self.plateau[ol][oc] = 0
                        self.plateau[nl][nc] = self.player
                        self.switchJoeur()
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

    def jouer(self):

            print("Le joueur numero " +str(self.player) + " va jouer.")
            if (self.pions_restant == 0):
                print("Modifier la position de quel pion ?")
                while True:
                    print("Donner un ox et un oy")

                    ol = int(input())
                    oc = int(input())
                    if (ol >= 0 and ol < 5) and (oc >= 0 and oc < 5) and self.plateau[ol][oc]==self.player:
                        break
                    else:
                        print("old ligne ou old colonne incorrect")
                print("Quelle nouvelle position ?")
                while True:
                    print("Donner un nx et un ny")
                    nl = int(input())
                    nc = int(input())
                    if (nl >= 0 and nl < 5) and (nc >= 0 and nc < 5) and self.movePions(ol,oc,nl,nc) :
                        #verif = self.gagner(nl,nc)
                        #if(verif[0]):
                        #   print("Le joueur " + str(verif[1]) + " a gagné.")
                        #   exit()
                        #self.switchJoeur()
                        break
                    else:
                        print("nl ou nc incorrect")

            else:
                while True:
                    print("Donner un x et un y")

                    l = int(input())
                    c = int(input())
                    if (l >= 0 and l < 5) and (c >= 0 and c < 5) and self.mettrePions(l,c):
                        #verif = self.gagner(l,c)
                        #if(verif[0]):
                        #    print("Le joueur " + str(verif[1]) + " a gagné.")
                        #   exit()
                        #self.switchJoeur()
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

    def getAdjacent(self, l, c):
        adjacents = []
        directions = [
            [-1, -1], [-1, 0], [-1, +1],
            [0, -1],           [0, +1],
            [+1, -1], [+1, 0], [+1, +1],
        ]

        for i in directions:
            if( 0 <= l + i[0] <= 4 and 0 <= c + i[1] <= 4):
                adjacents.append([l + i[0],c + i[1]])
        return adjacents


    def presqueGagner(self,l,c):
        return  False

    def countAdjacent(self,l,c,type):
        val=1
        s=0;
        if not(type):
            val=-1

        adjacents=self.getAdjacent(l,c)
        print(adjacents)
        for ad in adjacents:
            if self.plateau[ad[0]][ad[1]]==val:
                s=s+1


        return s