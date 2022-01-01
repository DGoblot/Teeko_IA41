import copy
import random


class Ia:

    # GameJ c'est la classe Game
    # Player pour connaitre qu'elle joueur qui va jouer
    def __init__(self, GameJ, player, profondeur):
        self.GameJ = GameJ
        self.player = player
        self.profondeur = profondeur  # Profondeur determine la difficulte du jeu

    # Algorithme intelligent pour le niveau facile
    # IA choisit au hasard les emplacements
    def niveauFacile(self):
        if self.GameJ.pions_restant != 0:  # Il y a encore des pions non mis sur le plateau
            while 1:
                # Choisir les coordonnées du pion
                l = random.randint(0, 4)
                c = random.randint(0, 4)

                if self.GameJ.mettrePions(int(l), int(c)):  # Tester si possible de mettre le pion sur le plateau
                    break
        else:  # Tous les pions sont sur le plateau
            while 1:
                # Choisir les coordonnées à modifier
                ol = random.randint(0, 4)
                oc = random.randint(0, 4)
                # Choisir les coordonnées du futur pion
                nl = random.randint(max(0, ol - 1), min(ol + 1, 4))
                nc = random.randint(max(0, oc - 1), min(oc + 1, 4))
                if self.GameJ.movePionsPrendre(int(ol), int(oc)):
                    if self.GameJ.movePionsPoser(int(nl),int(nc)):  # Tester si possible de modifier la position du pion sur le plateau
                        break

    # Algorithme intelligent pour le niveau moyen  et difficile en utilisant l'algo minmax avec alphabeta
    def alphaBeta(self, depth):
        # initialisation des variables pour l'algorithme alphabeta
        alpha = -10000
        beta = 10000
        v = -10000
        tmp = 0
        # Faire une copie de la classe Game
        tmpGameJ = copy.deepcopy(self.GameJ)
        if tmpGameJ.pions_restant > 0:  # Il y a encore des pions non mis sur le plateau
            # Va contenir la meilleurs position de pion
            meilleur_l = 0
            meilleur_c = 0
            # Parcours tous le plateau
            for l in range(0, 5):
                for c in range(0, 5):
                    if tmpGameJ.plateau[l][c] == 0:  # Si c'est vide on insère un pion
                        tmpGameJ.plateau[l][c] = self.player
                        tmp = self.min(tmpGameJ, depth - 1, alpha, beta, l, c)  # appelle de la fonction min
                        tmpGameJ.plateau[l][c] = 0  # on supprime la modification faite sur le plateau
                        if tmp > v:  # Si la valeur tmp est plus grand on enregistre cette valeur ainsi que les coordonnées du pion
                            v = tmp
                            meilleur_l = l
                            meilleur_c = c
            self.GameJ.mettrePions(meilleur_l,meilleur_c)

        else:  # Tous les pions sont sur le plateau
            # Va contenir la meilleurs position du futur pion
            meilleur_l1 = 0  # Ancienne position
            meilleur_c1 = 0  # Ancienne position
            meilleur_l2 = 0  # Futur position
            meilleur_c2 = 0  # Futur position

            # Parcours tous le plateau
            for l in range(0, 5):
                for c in range(0, 5):
                    if tmpGameJ.plateau[l][c] == self.player:  # Si la position contient le pion de l'ia

                        adjacents = tmpGameJ.getAdjacent(l, c)  # Recherche des position adjacentes du pion

                        # Parcours toutes les positions adjacentes
                        for ad in adjacents:
                            # verification des coordonnées et les mettre sur le plateau
                            if tmpGameJ.moviePionsRobot(l, c, ad[0], ad[1], self.player):

                                tmp = self.min(tmpGameJ, depth - 1, alpha, beta, l,
                                               c)  # appelle de la fonction min
                                if tmp > v:  # Si la valeur tmp est plus grand on enregistre cette valeur ainsi que les coordonnées du pion
                                    v = tmp
                                    meilleur_l1 = l
                                    meilleur_c1 = c
                                    meilleur_l2 = ad[0]
                                    meilleur_c2 = ad[1]
                                # Pour reprendre l'etat normal du jeux
                                tmpGameJ.plateau[l][c] = self.player
                                tmpGameJ.plateau[ad[0]][ad[1]] = 0
            self.GameJ.movePionsPrendre(int(meilleur_l1), int(meilleur_c1))
            self.GameJ.movePionsPoser(int(meilleur_l2),int(meilleur_c2))

    def min(self, tmpGameJ, depth, alpha, beta, x, y):

        verif = tmpGameJ.gagner(x, y)  # vérifier s'il y a un gagnant
        if depth == 0 or verif[0]:
            return self.eval(tmpGameJ, verif[0], False)  # Appelle de la fonction eval

        v = 10000
        if tmpGameJ.pions_restant + depth - self.profondeur > 0:  # Pour savoir s'il y a encore des pions non utilisé

            for l in range(5):
                for c in range(5):
                    if tmpGameJ.plateau[l][c] == 0:  # Si position est vide l'opposant met son pion
                        tmpGameJ.plateau[l][c] = -1 * self.player

                        tmp = self.max(tmpGameJ, depth - 1, alpha, beta, l, c)  # Appelle de la fonction max

                        # Revient a l'etat précédent
                        tmpGameJ.plateau[l][c] = 0

                        # Mettre à jour des varaibles beta et v
                        beta = tmp
                        if tmp < v:
                            v = tmp
                        if alpha >= beta:
                            return beta
        else:

            for l in range(5):
                for c in range(5):
                    if tmpGameJ.plateau[l][
                        c] == -1 * self.player:  # Si il existe un pion de l'adversaire a cette position

                        adjacents = tmpGameJ.getAdjacent(l, c)  # Recherche des position adjacentes du pion

                        for ad in adjacents:
                            if tmpGameJ.moviePionsRobot(l, c, ad[0], ad[1],
                                                        -1 * self.player):  # Mettre à jour le plateau temporelle
                                tmp = self.max(tmpGameJ, depth - 1, alpha, beta, ad[0],
                                               ad[1])  # Appelle de la fonction max

                                # Revient a l'etat précédent
                                tmpGameJ.plateau[l][c] = -1 * self.player
                                tmpGameJ.plateau[ad[0]][ad[1]] = 0

                                # Mettre à jour des varaibles beta et v
                                beta = tmp
                                if tmp < v:
                                    v = tmp
                                if alpha >= beta:
                                    return beta
        return v

    def max(self, tmpGameJ, depth, alpha, beta, x, y):

        verif = tmpGameJ.gagner(x, y)  # vérifier s'il y a un gagnant
        if depth == 0 or verif[0]:
            return self.eval(tmpGameJ, verif[0], True)  # Appelle de la fonction eval

        v = -10000
        tmp = 0
        if tmpGameJ.pions_restant + depth - self.profondeur > 0:  # Pour savoir s'il y a encore des pions non utilisé

            for l in range(5):
                for c in range(5):
                    if tmpGameJ.plateau[l][c] == 0:  # Si position est vide

                        tmpGameJ.plateau[l][c] = self.player  # L'ia met un pion a cette position
                        tmp = self.min(tmpGameJ, depth - 1, alpha, beta, l, c)  # Appelle de la fonction min
                        tmpGameJ.plateau[l][c] = 0  # Annulation des changement sur la plateau temporelle

                        # Mettre a jour les varaibles v et alpha
                        alpha = tmp
                        if tmp > v:
                            v = tmp
                        if alpha >= beta:
                            return alpha
        else:
            for l in range(5):
                for c in range(5):
                    if tmpGameJ.plateau[l][c] == self.player:  # Si il existe un pion à cette position
                        adjacents = tmpGameJ.getAdjacent(l, c)  # Recherche des positions adjacents
                        for ad in adjacents:
                            if tmpGameJ.moviePionsRobot(l, c, ad[0], ad[1],
                                                        self.player):  # Mettre le pion sur le plateau temporelle
                                tmp = self.min(tmpGameJ, depth - 1, alpha, beta, ad[0],
                                               ad[1])  # Appelle de la fonction min

                                # Revenir à l'etat precedant
                                tmpGameJ.plateau[l][c] = self.player
                                tmpGameJ.plateau[ad[0]][ad[1]] = 0
                                # Mettre à jour les varaibles alpha et v
                                alpha = tmp
                                if tmp > v:
                                    v = tmp
                                if alpha >= beta:
                                    return alpha
        return v

    # type pour determiner max et min
    def eval(self, tmpGameJ, verif, type):
        value = 0

        if verif:  # Si il y a eu victoire
            value = 20

        else:  # calculer selon le poid et les pions adjacents
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
                        value = value + abs(tmpGameJ.plateau[l][c]) * poids[l][c] + tmpGameJ.countAdjacent(l, c, type)

        if not(type):  # Si le joueur qui active la fonction eval est l'opposant
            value = -1 * value
        return value
