import random
from Game import GameJ
class Ia:

    def __init__(self,GameJ,player):
        self.GameJ=GameJ
        self.player=player


    def niveauFacile(self):
        if self.GameJ.pions_restant != 0:
            while 1:
                l = random.randint(0, 4)
                c = random.randint(0, 4)
                if self.GameJ.mettrePions(int(l), int(c)):
                    break
        else:
            while 1:
                ol = random.randint(0, 4)
                oc = random.randint(0, 4)
                nl = random.randint(0, 4)
                nc = random.randint(0, 4)
                if self.GameJ.movePions(int(ol), int(oc), int(nl), int(nc)):
                    break


    def alphaBeta(self, depth):
        alpha = -10000
        beta = 10000
        v = -10000
        tmp = 0
        print(self.GameJ.pions_restant)
        if self.GameJ.pions_restant > 0:

            meilleur_l = 0
            meilleur_c = 0
            for l in range(0, 5):
                for c in range(0, 5):
                    if self.GameJ.plateau[l][c]==0:
                        self.GameJ.plateau[l][c]=self.player

                        tmp = self.min(depth - 1, alpha, beta,l,c)
                        self.GameJ.plateau[l][c] = 0
                        if tmp > v:
                            v = tmp
                            meilleur_l = l
                            meilleur_c = c
            print("meilleur choix ")
            print("ligne: " + str(meilleur_l))
            print("colonne: " + str(meilleur_c))
            self.GameJ.plateau[meilleur_l][ meilleur_c]=self.player
            self.GameJ.pions_restant=self.GameJ.pions_restant-1
            self.GameJ.switchJoeur();
        else:
            meilleur_l1 = 0
            meilleur_c1 = 0
            meilleur_l2 = 0
            meilleur_c2 = 0
            for l in range(0, 5):
                for c in range(0, 5):
                    if self.GameJ.plateau[l][c] == self.player:
                        adjacents = self.GameJ.getAdjacent(l, c)
                        for ad in adjacents:
                            # verification des coordonnée
                            if self.GameJ.moviePionsRobot(l,c,ad[0],ad[1],self.player):

                                tmp = self.min(depth - 1, alpha, beta,l,c)
                                if tmp < v:
                                    v = tmp
                                    meilleur_l1 = l
                                    meilleur_c1 = c
                                    meilleur_l2 = ad[0]
                                    meilleur_c2 = ad[1]
                                #Pour reprendre l'etat normal du jeux
                                self.GameJ.plateau[l][c] = self.player
                                self.GameJ.plateau[ad[0]][ad[1]] = 0

            if self.GameJ.movePions(meilleur_l1, meilleur_c1, meilleur_l2, meilleur_c2):
                print(True)
            else:
                print(False)


    def min(self, depth, alpha, beta,x,y):
        if depth == 0 or self.GameJ.gagner(x,y):
            return self.eval(x,y)

        v = 10000
        if self.GameJ.pions_restant > 0:
            for l in range(5):
                for c in range(5):
                    if self.GameJ.plateau[l][c] == 0:
                        self.GameJ.plateau[l][c] = -1*self.player
                        tmp = self.max(depth - 1, alpha, beta,l,c)
                        self.GameJ.plateau[l][c] = 0
                        beta = tmp
                        if tmp < v:
                            v = tmp
                        if alpha >= beta:
                            return beta
        else:
            for l in range(5):
                for c in range(5):
                    if self.GameJ.plateau[l][c] == -1*self.player:
                        adjacents = self.GameJ.getAdjacent(l, c)
                        for ad in adjacents:
                            if self.GameJ.moviePionsRobot(l, c, ad[0], ad[1], -1*self.player):
                                tmp = self.max(depth - 1, alpha, beta,l,c)
                                self.GameJ.plateau[l][c] = -1*self.player
                                self.GameJ.plateau[ad[0]][ad[1]] = 0
                                beta = tmp
                                if tmp < v:
                                    v = tmp
                                if alpha >= beta:
                                    return beta
        return v

    def max(self, depth, alpha, beta,x,y):
        if depth == 0 or self.GameJ.gagner(x,y):
            return self.eval(x,y)

        v = -10000
        if self.GameJ.pions_restant > 0:
            for l in range(5):
                for c in range(5):
                    if self.GameJ.plateau[l][c] == 0:

                        self.GameJ.plateau[l][c]=self.player;
                        tmp = self.min(depth - 1, alpha, beta,l,c)
                        self.GameJ.plateau[l][c] = 0
                        alpha = tmp
                        if tmp > v:
                            v = tmp
                        if alpha >= beta:
                            return alpha
        else:
            for l in range(5):
                for c in range(5):
                    if self.GameJ.plateau[l][c] == self.player:
                        adjacents = self.GameJ.getAdjacent(l, c)
                        for ad in adjacents:
                            if self.GameJ.moviePionsRobot(l, c, ad[0], ad[1],  self.player):
                                tmp = self.max(depth - 1, alpha, beta)
                                self.GameJ.plateau[l][c] = self.player
                                self.GameJ.plateau[ad[0]][ad[1]] = 0
                                alpha = tmp
                                if tmp > v:
                                    v = tmp
                                if alpha >= beta:
                                    return alpha
        return v



    def eval(self,l,c):
        if self.GameJ.gagner(l,c):
            return self.player* 5
        value=0
        poids = [
            [0, 1, 0, 1, 0],
            [1, 2, 2, 2, 1],
            [0, 2, 3, 2, 0],
            [1, 2, 2, 2, 1],
            [0, 1, 0, 1, 0]
        ]
        for l in range(5):
            for c in range(5):
                if self.GameJ.plateau[l][c] != 0:
                    value = value + self.GameJ.board[l][c] * poids[l][c]

        return value


p= GameJ()
a=Ia(p,-1)




"""  def nextStatsPlace(self,plateau):
     ns=[]
     coordonnee=[]
     for i in range(0,5):
         for j in range(0,5):
             copyPlateau=copy.deepcopy(plateau)

             if copyPlateau.mettrePions(i,j):
                 ns.append(copyPlateau)
                 coordonnee.append([i,j])
                 copyPlateau.affichePl()
     return [ns,coordonnee]

 def nextStatesMovie(self,plateau):
     ns=[]
     coordonnee = []
     for i in range(0,5):
         for j in range(0,5):

             if self.GameJ.plateau[i][j]==self.player:

                 position=self.GameJ.positionAdjacente(i,j)

                 for pos in position:
                     copyPlateau = copy.deepcopy(plateau)
                     print(pos)
                     if copyPlateau.movePions(i,j,pos[0],pos[1]):
                         print("test")
                         ns.append(copyPlateau)
                         copyPlateau.affichePl()
                         coordonnee.append([i,j,pos[0],pos[1]])
     return [ns,coordonnee]
"""