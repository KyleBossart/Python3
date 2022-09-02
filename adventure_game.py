from os import system
import time

# Health, Damage, Potion Values
hp = 10
dmg = 1
potion = 5
inventory_potion = 0

# Functions
system("clear")

def wait():
    time.sleep(1.5)

def game_over():
    print("GAME OVER")
    quit()

def total_health():
    print("Current Health: " + str(hp) + "/10.")

    

# Want to play?
start = input("Do you want to play? ")
if start.lower() != "yes":
    print("Come back when you want to!")
    quit()
else:
    print("Okay, let's get started!")
    wait()
    print("")
    print("")

# Part 1
print("You wake up in a dark room with a single door.")
wait()
part1 = input("What would you like to do? > ")
if part1.lower() != "open the door":
    wait()
    print("When you attempt to " + str(part1.lower()) + " a rat kills you.")
    wait()
    game_over()
else:
    print("")
    print("You open the door and feel a cold breeze... \n")
    wait()
    wait()

# Part 2
print("You take a step outside and find yourself in a dark forest. \n")
wait()
print("You see a rusty sword sitting on the ground and you pick it up. \n")
wait()
print("As you pick up the sword you notice a small creature running at you. \n")
wait()

# Part 2 - Attack or Run - Creature and Level Up
atk_or_run = input("Do you attack the creature with the sword or run? > ")
if atk_or_run.lower() == "attack":
    print("")
    print("You swing the sword at the creature... \n")
    wait()
    wait()
    print("and kill it! But you take some damage in the process. \n")
    wait()
    hp -= 5
    print(">> -5 Health.")
    total_health()
    print("")
    wait()
    print("After killing the creature you feel stronger... \n")
    wait()
    wait()
    print("Congratulations! You are level 2! Damage increased to 2. \n")
    dmg += 1
    wait()

else:
    print("You run from the creature, but it catches up and kills you.")
    game_over()

# Part 3
print("You search the creature's corpse and find a small health potion \n")
inventory_potion += 1
drink = input("Do you want to drink the potion and restore some health? >  ")
if drink.lower() == "yes":
    wait()
    print(" \nYou drink the potion and feel rejuvenated.")
    inventory_potion -= 1
    hp += 5
    wait()
    total_health()
