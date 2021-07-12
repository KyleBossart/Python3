from os import system
import time

# Health, Damage, Potion Values
hp = 10
dmg = 1
potion = 5

# Functions
system("clear")

def wait():
    time.sleep(1)

def game_over():
    print("GAME OVER")
    quit()

def take_potion():
    hp += 5

def take_damage():
    hp -= 1

def total_health():
    print("Current Health: " + str(hp))
    

# Want to play?
start = input("Do you want to play? ")
if start.lower() != "yes":
    print("Come back when you want to!")
    quit()
else:
    print("Okay, let's get started!")
    wait()

# Part 1
print("You wake up in a dark room with a single door.")
wait()
part1 = input("What would you like to do? ")
if part1.lower() != "open the door":
    print("When you attempt to " + str(part1.lower()) + " a rat kills you.")
    game_over()
else:
    print("You open the door and feel a cold breeze.")
    wait()

# Part 2
print("You take a step outside and find yourself in a dark forest.")
wait()
print("You see a rusty sword sitting on the ground and you pick it up.")
wait()
print("As you pick up the sword you notice a small creature running at you.")
wait()

# Part 2 - Attack or Run - Creature and Level Up
atk_or_run = input("Do you attack the creature with the sword or run? ")
if atk_or_run.lower() == "attack":
    print("You swing the sword at the creature and kill it, but take some damage in the process.")
    wait()
    take_damage()
    print("-5 Health. Total Health: " + total_health())
    wait()
    print("After killing the creature you feel stronger.")
    wait()
    print("Congratulations! You are level 2! Damage increased to 2.")
    dmg += 1

else:
    print("You run from the creature, but it catches up and kills you.")
    game_over()

# Part 3
print("After killing the creature, you search it and find a small health potion")