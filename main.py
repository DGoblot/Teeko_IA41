from Game import GameJ
from ia import Ia
import time
game = GameJ()
ia1 = Ia(game,1,1)
ia2 = Ia(game,-1,1)

game.affichePl()
print("\n")

while(True):
   ia1.alphaBeta(1,0)

   game.affichePl()
   print("\n")

   time.sleep(5)
   ia2.alphaBeta(1,0)
   print("\n")

   game.affichePl()
   print("\n")

print("Game finished!\n")
if (game.winner() == 1):
    print("Congrats, you have won this game!\n")
else:
   print("Booo, you lost :(")
