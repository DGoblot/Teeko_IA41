
class PlateauJ:

    #La valeur 0 dans le plateau indique qu'il n'a pas de pion
    #La valeur 1 c'est le peon du joueur 1
    #La valeur -1 c'est le peon du joueur 2 / robot

    #player c'est pour indique qu'
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
            self.plateau[x][y]=self.player()
            self.switchJoeur()
            self.pions_restant=self.pions_restant-1;
        pass

    def movePions(self):
        pass


    def gagner(self):
        pass

    def presquegagner(self):
        pass

    def jouer(self):
        pass

p=PlateauJ()
p.affichePl()