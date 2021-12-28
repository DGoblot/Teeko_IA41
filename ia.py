import copy
import random
from Game import GameJ
class Ia:

    #GameJ c'est la classe Game
    #Player pour connaitre qu'elle joueur qui va jouer
    def __init__(self,GameJ,player,profondeur):
        self.GameJ=GameJ
        self.player=player
        self.profondeur=profondeur


    #Algorithme intelligent pour le niveau facile
    #IA choisit au hasard les emplacements
    def niveauFacile(self):
        if self.GameJ.pions_restant != 0: #Il y a encore des pions non mis sur le plateau
            while 1:
                #Choisir les coordonnées du pion
                l = random.randint(0, 4)
                c = random.randint(0, 4)

                if self.GameJ.mettrePions(int(l), int(c)):#Tester si possible de mettre le pion sur le plateau
                    break
        else: #Tous les pions sont sur le plateau
            while 1:
                # Choisir les coordonnées à modifier
                ol = random.randint(0, 4)
                oc = random.randint(0, 4)
                # Choisir les coordonnées du futur pion
                nl = random.randint(0, 4)
                nc = random.randint(0, 4)
                if self.GameJ.movePions(int(ol), int(oc), int(nl), int(nc)):#Tester si possible de modifier la position du pion sur le plateau
                    break

    #Algorithme intelligent pour le niveau moyen  et difficile
    def alphaBeta(self, depth,niveau):
        #initialisation des variables pour l'algorithme alphabeta
        alpha = -10000
        beta = 10000
        v = -10000
        tmp = 0

        tmpGameJ=copy.deepcopy(self.GameJ)

        if tmpGameJ.pions_restant > 0:#Il y a encore des pions non mis sur le plateau

            #Va contenir la meilleurs position de pion
            meilleur_l = 0
            meilleur_c = 0
            for l in range(0, 5):
                for c in range(0, 5):
                    if tmpGameJ.plateau[l][c]==0:
                        tmpGameJ.plateau[l][c]=self.player
                        #print("\n")
                        #print("(nombre de peons non fini Afficher la teeko pour le noued max profondeur "+str(self.profondeur-depth))
                        #tmpGameJ.affichePl()
                        #print("\n")
                        tmp = self.min(tmpGameJ,niveau,depth - 1, alpha, beta,l,c)
                        tmpGameJ.plateau[l][c] = 0
                        if tmp > v:
                            v = tmp
                            meilleur_l = l
                            meilleur_c = c

            self.GameJ.plateau[meilleur_l][ meilleur_c]=self.player

            #Modifier le nombre de pion et quelle joueur va jouer
            self.GameJ.pions_restant=self.GameJ.pions_restant-1
            self.GameJ.switchJoeur();
        else: #Tous les pions sont sur le plateau
            meilleur_l1 = 0
            meilleur_c1 = 0
            meilleur_l2 = 0
            meilleur_c2 = 0
            for l in range(0, 5):
                for c in range(0, 5):
                    if tmpGameJ.plateau[l][c] == self.player:

                        adjacents = tmpGameJ.getAdjacent(l, c)
                        for ad in adjacents:
                            # verification des coordonnée
                            if tmpGameJ.moviePionsRobot(l,c,ad[0],ad[1],self.player):
                                #print("\n")
                                #print("(nombre de peons fini Afficher la teeko pour le noued max profondeur " + str(
                                #    self.profondeur - depth))
                                #tmpGameJ.affichePl()
                                #print("\n")
                                tmp = self.min(tmpGameJ,niveau,depth - 1, alpha, beta,l,c)
                                if tmp > v:
                                    v = tmp
                                    meilleur_l1 = l
                                    meilleur_c1 = c
                                    meilleur_l2 = ad[0]
                                    meilleur_c2 = ad[1]
                                #Pour reprendre l'etat normal du jeux
                                tmpGameJ.plateau[l][c] = self.player
                                tmpGameJ.plateau[ad[0]][ad[1]] = 0

            if self.GameJ.movePions(meilleur_l1, meilleur_c1, meilleur_l2, meilleur_c2):
                print(True)
            else:
                print(False)


    def min(self,tmpGameJ,niveau ,depth, alpha, beta,x,y):
        #print("min")
        #print("depth= "+str(depth))
        verif = tmpGameJ.gagner(x, y)
        if depth == 0 or verif[0]:
            #print("out")
            return self.eval(tmpGameJ,verif[0],x,y,niveau,False)

        v = 10000
        if tmpGameJ.pions_restant + depth - self.profondeur > 0:
            #print("vrai")

            for l in range(5):
                for c in range(5):
                    if tmpGameJ.plateau[l][c] == 0:
                        tmpGameJ.plateau[l][c] = -1*self.player
                        #print("\n")
                        #print("(nombre de peons non fini Afficher la teeko pour le noued min profondeur " + str(
                        #    self.profondeur - depth))
                        #tmpGameJ.affichePl()
                        #print("\n")
                        tmp = self.max(tmpGameJ,niveau,depth - 1, alpha, beta,l,c)
                        tmpGameJ.plateau[l][c] = 0
                        beta=tmp
                        if tmp < v:
                            v = tmp
                        if alpha >= beta:
                            return beta
        else:
            #print("faux")
            for l in range(5):
                for c in range(5):
                    if tmpGameJ.plateau[l][c] == -1*self.player:
                        adjacents = tmpGameJ.getAdjacent(l, c)
                        for ad in adjacents:
                            if tmpGameJ.moviePionsRobot(l, c, ad[0], ad[1], -1*self.player):
                                #print("\n")
                                #print("(nombre de peons fini Afficher la teeko pour le noued min profondeur " + str(
                                #    self.profondeur - depth))
                                #tmpGameJ.affichePl()
                                #print("\n")
                                tmp = self.max(tmpGameJ,niveau,depth - 1, alpha, beta,ad[0],ad[1])
                                tmpGameJ.plateau[l][c] = -1*self.player
                                tmpGameJ.plateau[ad[0]][ad[1]] = 0
                                beta = tmp
                                if tmp < v:
                                    v = tmp
                                if alpha >= beta:
                                    return beta
        return v

    def max(self,tmpGameJ,niveau, depth, alpha, beta,x,y):
        #print("max")
        #print("depth= " + str(depth))
        verif = tmpGameJ.gagner(x, y)
        if depth == 0 or verif[0]:
         #   print("out")
            return self.eval(tmpGameJ,verif[0],x,y,niveau,True)

        v = -10000
        tmp=0
        if tmpGameJ.pions_restant + depth - self.profondeur  > 0:
          #  print("vrai")

            for l in range(5):
                for c in range(5):
                    if tmpGameJ.plateau[l][c] == 0:

                        tmpGameJ.plateau[l][c]=self.player;
                        #print("\n")
                        #print("(nombre de peons non fini Afficher la teeko pour le noued max profondeur " + str(
                        #self.profondeur - depth))
                        #tmpGameJ.affichePl()
                        #print("\n")
                        tmp = self.min(tmpGameJ,niveau,depth - 1, alpha, beta,l,c)
                        tmpGameJ.plateau[l][c] = 0
                        alpha = tmp
                        if tmp > v:
                            v = tmp
                        if alpha >= beta:
                            return alpha
        else:
           # print("faux")
            for l in range(5):
                for c in range(5):
                    if tmpGameJ.plateau[l][c] == self.player:
                        adjacents = tmpGameJ.getAdjacent(l, c)
                        for ad in adjacents:
                            if tmpGameJ.moviePionsRobot(l, c, ad[0], ad[1],  self.player):
                            #    print("\n")
                            #    print("(nombre de peons  fini Afficher la teeko pour le noued max profondeur " + str(
                            #    self.profondeur - depth))
                            #     tmpGameJ.affichePl()
                            #    print("\n")
                                tmp = self.max(tmpGameJ,niveau,depth - 1, alpha, beta,ad[0],ad[1])
                                tmpGameJ.plateau[l][c] = self.player
                                tmpGameJ.plateau[ad[0]][ad[1]] = 0
                                alpha=tmp
                                if tmp > v:
                                    v = tmp
                                if alpha >= beta:
                                    return alpha
        return v



    def eval(self,tmpGameJ,verif,l,c,niveau,type):
        value = 0
        if verif:
            value =10

        else:
            poids = [
                [0, 1, 0, 1, 0],
                [1, 2, 2, 2, 1],
                [0, 2, 3, 2, 0],
                [1, 2, 2, 2, 1],
                [0, 1, 0, 1, 0]
            ]
            for l in range(5):
                for c in range(5):
                    if tmpGameJ.plateau[l][c] != 0:
                        value = value + abs(tmpGameJ.plateau[l][c])* poids[l][c] + tmpGameJ.countAdjacent(l,c,type)



        return value







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