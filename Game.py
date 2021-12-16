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
            self.plateau[x][y]=self.player
            self.switchJoeur()
            self.pions_restant=self.pions_restant-1;
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
                        self.switchJoeur()
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
            print("Le joueur numero va jouer "+str(self.player))
            if (self.pions_restant == 0):
                print("Quelle pion modifier la position")
                while True:
                    print("Donner un ox et un oy")

                    ox = int(input())
                    oy = int(input())
                    if (ox >= 0 and ox < 5) and (oy >= 0 and oy < 5) and self.plateau[ox][oy]==self.player:
                        break
                    else:
                        print("Vous avez donner un ox et un oy faux")
                print("Quelle futur position")
                while True:
                    print("Donner un nx et un ny")
                    nx = int(input())
                    ny = int(input())
                    if (nx >= 0 and nx < 5) and (ny >= 0 and ny < 5) and self.movePions(ox,oy,nx,ny) :
                        break
                    else:
                        print("Vous avez donner un nx et un ny faux")


            else:
                while True:
                    print("Donner un x et un y")

                    x = int(input())
                    y = int(input())
                    if (x >= 0 and x < 5) and (y >= 0 and y < 5) and self.mettrePions(x,y):
                        break
                    else:
                        print("Vous avez donner un x et un y faux")


p=PlateauJ()

p.jouer()