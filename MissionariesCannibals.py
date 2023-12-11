### Your code ###
boat_side = 'Right'
missionaries_on_right=3
cannibals_on_right=3
missionaries_on_left=0
cannibals_on_left=0
missionaries=0
cannibals=0
print("M = "+str(missionaries_on_left)+" C = "+str(cannibals_on_left)+" |------B| M = "+str(missionaries_on_right)+" C = "+str(cannibals_on_right))


while((missionaries+cannibals)<=2):
  missionaries=int(input("Enter number of missionaries on the boat: "))
  cannibals=int(input("Enter number of cannibals on the boat: "))
  if((missionaries+cannibals)>2):
    print("Invalid move 1")
    continue


  if(missionaries>missionaries_on_right or cannibals>cannibals_on_right):
    print("Invalid move 2")
    continue

  ### Your code ###
  missionaries_on_right-=missionaries
  cannibals_on_right-=cannibals
  missionaries_on_left+=missionaries
  cannibals_on_left+=cannibals

  ### Your code ###
  boat_side='Left'
  if(boat_side=='Left'):
    print("Boat is on left side.")
  else:
    print("Boat is on right side.")
  print("M = "+str(missionaries_on_left)+" C = "+str(cannibals_on_left)+" |B-----| M = "+str(missionaries_on_right)+" C = "+str(cannibals_on_right))

  ### Your code ###


  missionaries=int(input("Enter number of missionaries on the boat: "))
  cannibals=int(input("Enter number of cannibals on the boat: "))
  ### Your code ###
  if(missionaries>missionaries_on_left or cannibals>cannibals_on_left):
    print("Invalid move 2")
    continue

  ### Your code ###
  missionaries_on_left-=missionaries
  cannibals_on_left-=cannibals
  missionaries_on_right+=missionaries
  cannibals_on_right+=cannibals

  ### Your code ###
  boat_side='Right'
  if(boat_side=='Right'):
    print("Boat is on right side.")
  else:
    print("Boat is on left side.")
  print("M = "+str(missionaries_on_left)+" C = "+str(cannibals_on_left)+" |-----B| M = "+str(missionaries_on_right)+" C = "+str(cannibals_on_right))

  ### Your code ###
  if(missionaries_on_right>0 and (missionaries_on_right<cannibals_on_right)):
    print("You Lose")
  if(missionaries_on_left>0 and (missionaries_on_left<cannibals_on_left)):
    print("You Lose")

  ### Your code ###
  if(missionaries_on_left==3 and cannibals_on_left==3):
    print("You win")

