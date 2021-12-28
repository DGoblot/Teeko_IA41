from Game import GameJ
from ia import Ia

game = GameJ()

ia = Ia(game,-1,1)

game.affichePl()
print("\n")

while(True):
   game.jouer()
   print("\n")

   game.affichePl()
   print("\n")

   ia.alphaBeta(1,0)
   print("\n")

   game.affichePl()
   print("\n")

print("Game finished!\n")
if (game.winner() == 1):
    print("Congrats, you have won this game!\n")
else:
   print("Booo, you lost :(")
