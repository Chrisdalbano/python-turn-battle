import enemy
import player
import decorators as dec
import time
import random

def battle_simulation(player, enemy): #the game function
    print(dec.Decorators.test_decorator)
    print("[BATTLE JUST STARTED]\n [BETWEEN {} and the {}]".format(player.name, enemy.name))
    time.sleep(2)

    while True:
        #enemy.hp = player.attack(enemy) player and enemy would simulate a hit-hit battle
        print("Your turn, {}! \n {} \n ".format(player.name, dec.Decorators.player_decorator))
        enemy.hp = player.decision(player.player_actions, enemy) #the player decides his actions on combat
        time.sleep(1.0)
        print("{} turn \n {}".format(enemy.name, dec.Decorators.enemy_decorator))
        time.sleep(1.0)
        '''
        player.hp = enemy.attack(player) #the enemy attacks the player after his action
        '''
        player.hp = enemy.enemy_decision(player) #the enemy decides what action to takes based on player combat info
