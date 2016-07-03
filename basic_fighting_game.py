# Modules
from colorama import *
from random import *
from sys import *
import os

# Global Variables
usr_health = 100
enm_health = 100
usr_level = 1
rcv = True
fcv = False
enm_dmg = 0

# Start game
while rcv:
    enm_level = randint(1,4) * usr_level
    usr_health = 100
    enm_health = 100
    usr_health = usr_health * usr_level
    enm_health = enm_health * enm_level
    print("An enemy has appeared \n")
    fcv = True
    while fcv:
        if usr_health > 1:
            enm_dmg = randint(1,5) * enm_level
            print("Enemy Health: " + str(enm_health) + " | Enemy Level: " + str(enm_level))
            print("Player Health: " + str(usr_health) + " | Player Level: " + str(usr_level) + "\n")
            action = raw_input("[1] Attack | [2] Defend: ")
            print("\n")
            if action == "1":
                if enm_health < 1:
                    usr_level = usr_level + 1
                    fcv = False
                    os.system("clear")
                else:
                    dmg = randint(5,10) * usr_level
                    enm_health = enm_health - dmg
                    print("User does " + str(dmg) + " damage! \n")
            elif action == "2":
                print("user guards \n")
                enm_dmg = enm_dmg / 2
            else:
                print("user guards \n")
                enm_dmg = enm_dmg / 2
            usr_health = usr_health - enm_dmg
            print("enemy does " + str(enm_dmg) + " damage! \n")
        else:
            fcv = False
            rcv = False
            print("Game over")
