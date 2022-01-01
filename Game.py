class GameJ:

    def __init__(self):
        self.plateau = [[0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0]]
        self.player = 1
        self.pions_restant = 8
        self.phase = 'Mettre'#Variable permettant de savoir quelle action sera effectuée lorsque l'utilisateur clique
                            #sur la fenêtre : 'Mettre' indique la phase initiale de pose de pions
                            #                 'PrendrePion' indique la phase de choix du pion à deplacer
                            #                 'PoserPion' indique la phase de pose du pion qui vient d'être pris
        self.temp = 0, 0#Variable indiqué le pion qui va être deplacé
        self.visualisation = [[0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0]]#Cette variable permet d'indiquer au joueur ou peut-il poser le pion pris

    def switchJoeur(self):
        if self.player == 1:
            self.player = -1
        else:
            self.player = 1

    def mettrePions(self, x, y):#Fonction permetant de poser les pions initiaux
        if (self.plateau[x][y] != 0):
            return False
        else:
            self.plateau[x][y] = self.player
            self.pions_restant = self.pions_restant - 1
            if self.pions_restant <= 1:
                self.verifVictoire(x, y)
            self.switchJoeur()
            if self.pions_restant == 0:
                self.phase = 'movePrendre'
            return True

    def movePionsPrendre(self, ox, oy):#Fonction permettant de prendre un pion du plateau
        if self.plateau[ox][oy] != self.player:
            return False
        else:
            self.temp = ox, oy
            for i in range(max(0, ox - 1), min(ox + 1, 4) + 1):
                for j in range(max(0, oy - 1), min(oy + 1, 4) + 1):
                    if self.plateau[i][j] == 0:
                        self.visualisation[i][j] = 1
            self.phase = 'movePoser'
            return True

    def movePionsPoser(self, nx, ny):#Fonction permettant de poser le pion pris précédemment
        if nx == self.temp[0] and ny == self.temp[1]:
            self.phase = 'movePrendre'
            for i in range(max(0, nx - 1), min(nx + 1, 4) + 1):
                for j in range(max(0, ny - 1), min(ny + 1, 4) + 1):
                    self.visualisation[i][j] = 0
            return False
        elif self.plateau[nx][ny] != 0:
            return False
        else:
            if nx == self.temp[0] + 1 or nx == self.temp[0] - 1 or nx == self.temp[0]:
                if ny == self.temp[1] + 1 or ny == self.temp[1] - 1 or ny == self.temp[1]:
                    self.plateau[self.temp[0]][self.temp[1]] = 0
                    self.plateau[nx][ny] = self.player
                    self.verifVictoire(nx, ny)
                    for i in range(5):
                        for j in range(5):
                            self.visualisation[i][j] = 0
                    self.phase = 'movePrendre'
                    self.switchJoeur()
                    return True
                else:
                    return False
            else:
                return False

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

    def verifVictoire(self, x, y):#Fonction verifiant la victoire et quittant le jeu si il y en a une
        verif = self.gagner(x, y)
        if verif[0]:
            if self.player == 1:
                print("le joueur Bleu a gagné")
            else:
                print("le joueur Rouge a gagné")
            exit()


    def gagner(self, x, y):  # fonction vérifiant si le pion posé déclanche une victoire
        win = False
        colonne = [self.plateau[i][y] for i in range(5)]

        if (self.player == -1):
            verif = [-1, -1, -1, -1]
            verifCarre = [-1, -1]
        else:
            verif = [1, 1, 1, 1]
            verifCarre = [1, 1]

        if (self.contient(verif, self.plateau[x])):  # vérification d'une victoire en ligne
            win = True
        elif (self.contient(verif, colonne)):  # vérification d'une victoire en colonne
            win = True

        elif (self.contient(verifCarre, self.plateau[x])):  # vérification d'une victoire en carré
            carreInfo1 = self.contient(verifCarre, self.plateau[x])
            if (x != 0):
                carreInfo2 = self.contient(verifCarre, self.plateau[x - 1])
                if (carreInfo2 and carreInfo1[1] == carreInfo2[1]):
                    win = True
            if (x != len(self.plateau) - 1):
                carreInfo2 = self.contient(verifCarre, self.plateau[x + 1])
                if (carreInfo2 and carreInfo1[1] == carreInfo2[1]):
                    win = True
        else:  # verification d'une victoire en diagonale
            if (x == y):
                if (self.contient(verif, [diag[i] for i, diag in enumerate(self.plateau)])):
                    win = True
            if (x + y == 4):
                if (self.contient(verif, [diag[-i - 1] for i, diag in
                                          enumerate(self.plateau)])):  # vérification sur les deux grandes diagonales
                    win = True
            if (x == y - 1):
                petiteDiag = []
                for i in range(4):
                    petiteDiag.append(self.plateau[i][i + 1])
                if (self.contient(verif, petiteDiag)):
                    win = True
            if (x == y + 1):
                petiteDiag = []
                for i in range(4):
                    petiteDiag.append(self.plateau[i + 1][i])
                if (self.contient(verif, petiteDiag)):
                    win = True
            if (x + y == 3):
                petiteDiag = []
                for i in range(4):
                    petiteDiag.append(self.plateau[3 - i][i])
                if (self.contient(verif, petiteDiag)):
                    win = True
            if (x + y == 5):
                petiteDiag = []
                for i in range(4):
                    petiteDiag.append(self.plateau[4 - i][i + 1])
                if (self.contient(verif, petiteDiag)):
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
            [0, -1], [0, +1],
            [+1, -1], [+1, 0], [+1, +1],
        ]

        for i in directions:
            if (0 <= l + i[0] <= 4 and 0 <= c + i[1] <= 4):
                adjacents.append([l + i[0], c + i[1]])
        return adjacents

    # le nombre de pion adjacent du meme joueur
    def countAdjacent(self, l, c, type):
        val = 1
        s = 0
        if not (type):
            val = -1

        adjacents = self.getAdjacent(l, c)

        for ad in adjacents:
            if self.plateau[ad[0]][ad[1]] == val:
                s = s + 1
        return s
