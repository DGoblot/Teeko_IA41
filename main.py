from Game import GameJ
from ia import Ia

game = GameJ()

ia = Ia(game,-1)

game.affichePl()
print("\n")

while(game.gagner() == 0):
   game.jouer()
   game.affichePl()
   ia.alphaBeta(4)
   game.affichePl()

print("Game finished!\n")
if (game.winner() == 1):
    print("Congrats, you have won this game!\n")
else:
   print("Booo, you lost :(")
