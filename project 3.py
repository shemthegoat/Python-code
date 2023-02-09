# This is a simple choose your own adventure game

# Define the different locations in the game
def start():
  print("You wake up in a forest.")
  print("You see a lake nearby, a path ahead, and a light off in the distance.")
  action = input("Which one do you want to go towards? ")
  if action == "lake":
    lake()
  elif action == "path":
    path()
  elif action == "light":
    light()
  else:
    print("Invalid choice")
    start()

def lake():
  print("You walk towards the lake and see a small boat.")
  action = input("Do you want to get in the boat? ")
  if action == "yes":
    print("You get in the boat and start rowing. You see a cave on the other side of the lake.")
    cave()
  elif action == "no":
    print("You decide not to get in the boat and turn back.")
    start()
  else:
    print("Invalid choice")
    lake()

def path():
  print("You walk down the path and see a small cabin.")
  action = input("Do you want to go inside? ")
  if action == "yes":
    print("You go inside the cabin and find an old man sitting by the fire.")
    old_man()
  elif action == "no":
    print("You decide not to go inside the cabin and continue down the path.")
    start()
  else:
    print("press enter to return")
    path()

def light():
  print("You walk towards the light and see a group of people standing around a campfire.")
  action = input("Do you want to join them? ")
  if action == "yes":
    print("You join the group around the campfire and spend the night talking and roasting marshmallows. Yay you won the game!")
  elif action == "no":
    print("You decide not to join the group and turn back.")
    start()
  else:
    print("press enter to return")
    light()

# Define the actions you can
  old_man()
 

start()
