import random
from Game import GameJ
class Ia:

    def __init__(self,GameJ,player):
        self.GameJ=GameJ
        self.player=player


    def niveauFacile(self):
        if self.GameJ.pions_restant != 0:
            while 1:
                x = random.randint(0, 4)
                y = random.randint(0, 4)
                if self.GameJ.mettrePions(int(x), int(y)):
                    break
        else:
            while 1:
                x = random.randint(0, 4)
                y = random.randint(0, 4)
                a = random.randint(0, 4)
                b = random.randint(0, 4)
                if self.GameJ.movePions(int(x), int(y), int(a), int(b)):
                    break


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


def alphaBeta(self, depth):
    alpha = -10000
    beta = 10000
    v = -10000
    tmp = 0
    if self.GameJ.pions_restant > 8:
        meilleur_l = 0
        meilleur_c = 0
        for l in range(0, 5):
            for c in range(0, 5):
                if self.GameJ.mettrePions(l, c):
                    self.GameJ.pions_restant +=1
                    tmp = self.min(depth - 1, alpha, beta)
                    GameJ.plateu[l][c] = 0
                    if tmp < v:
                        v = tmp
                        meilleur_l = l
                        meilleur_c = c
        self.GameJ.mettrePions(meilleur_l, meilleur_c)
    else:
        meilleur_l1 = 0
        meilleur_c1 = 0
        meilleur_l2 = 0
        meilleur_c2 = 0
        for l in range(0, 5):
            for c in range(0, 5):
                if self.GameJ.player == self.player:
                    adjacents = self.GameJ.getAdjacent(l, c)
                    for ad in adjacents:
                        self.GameJ.movePions(l, c, ad[0], ad[1])
                        tmp = self.min(depth - 1, alpha, beta)
                        if tmp < v:
                            v = tmp
                            meilleur_l1 = l
                            meilleur_c1 = c
                            meilleur_l2 = ad[0]
                            meilleur_c2 = ad[1]
                        self.GameJ.plateau[l][c] = self.player
                        self.GameJ.plateau[ad[0]][ad[1]] = 0

    self.GameJ.movePions(meilleur_l1, meilleur_c1, meilleur_l2, meilleur_c2)

    def min(self, depth, alpha, beta):
        if depth == 0 or self.GameJ.gagner():
            return self.eval()

        v = 10000
        if self.GameJ.pions_restant > 0:
            for l in range(5):
                for c in range(5):
                    if self.GameJ.mettrePions(l, c):
                        self.GameJ.pions_restant += 1
                        tmp = self.max(depth - 1, alpha, beta)
                        self.GameJ.plateau[l][c] = 0
                        beta = tmp
                        if tmp < v:
                            v = tmp
                        if alpha >= beta:
                            return beta
        else:
            for l in range(5):
                for c in range(5):
                    if self.GameJ.player == self.player:
                        adjacents = self.GameJ.getAdjacent(l, c)
                        for ad in adjacents:
                            self.GameJ.movePions(l, c, ad[0], ad[1])
                            tmp = self.max(depth - 1, alpha, beta)
                            beta = tmp
                            if tmp < v:
                                v = tmp
                            if alpha >= beta:
                                return beta
        return v

    def max(self, depth, alpha, beta):
        if depth == 0 or self.GameJ.gagner():
            return self.eval()

        v = -10000
        if self.GameJ.pions_restant > 0:
            for l in range(5):
                for c in range(5):
                    if self.GameJ.mettrePions(l, c):
                        self.GameJ.pions_restant += 1
                        tmp = self.min(depth - 1, alpha, beta)
                        self.GameJ.plateau[l][c] = 0
                        alpha = tmp
                        if tmp > v:
                            v = tmp
                        if alpha >= beta:
                            return alpha
        else:
            for l in range(5):
                for c in range(5):
                    if self.GameJ.player == self.player:
                        adjacents = self.GameJ.getAdjacent(l, c)
                        for ad in adjacents:
                            self.GameJ.movePions(l, c, ad[0], ad[1])
                            tmp = self.max(depth - 1, alpha, beta)
                            alpha = tmp
                            if tmp > v:
                                v = tmp
                            if alpha >= beta:
                                return alpha
        return v



def eval(self):
    if self.GameJ.gagner():
        return self.player* 5
    value=0;
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


