#play tictactoe against computer.
#game includes one difficultly level: medium

import random

grid = [[" "," "," "],[" "," "," "],[" "," "," "]]

def determine_winner():
 for i in range(3):
   if grid[i][0] == grid[i][1] == grid[i][2] != ' ':
     return grid[i][0]
   if grid[0][i] == grid[1][i] == grid[2][i] != ' ':
     return grid[0][i]
 if grid[0][0] == grid[1][1] == grid[2][2] != ' ':
   return grid[0][0]
 if grid[2][0] == grid[1][1] == grid[0][2] != ' ':
   return grid[2][0]
 return False



def print_grid():
 print "  a b c"
 skip = True
 i = 0
 for row in grid:
   if not skip :
     print "  -----"
   skip = False
   print str(i) + " " + "|".join(row)
   i += 1
 print ""

def get_playermove():
 while True:
   try:
     print "where do you want to go?"
     y = ord(raw_input("a,b,c: ")[0]) - ord('a')
     x = int(raw_input("0,1,2: "))
     return x, y
   except:
     print "your input was not recognized, please try again"

def playermove():
 while True:
   x, y = get_playermove()
   if grid[x][y] == " ":
     grid[x][y] = "x"
     return
   print "invalid move!"

def computermove():
 i = 0
 while grid[i/3][i%3] != " ":
   i += 1
 grid[i/3][i%3] = "o"
 print "\ncomputer makes it's move\n"

def gridfull():
 return False not in map(lambda row: " " not in row, grid)


def do_game():
 global grid
 grid = [[" "," "," "],[" "," "," "],[" "," "," "]]
 if random.random() > 0.5 :
   player_next = "x"
 else :
   player_next = "o"
 winner = False
 while not (winner or gridfull()):
   print_grid()
   if player_next == "x":
     playermove()
     player_next = "o"
   else :
     computermove()
     player_next = "x"
   winner = determine_winner()

 print_grid()
 if winner :
   print winner, "is the winner!"
 else :
   print "there is a tie!"



while True:
 do_game()
 if raw_input("play again? (y/n) ") != "y":
   "thanks for playing!  goodbye"
   break

