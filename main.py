import decorators
import enemy
import player
import battles
import time
import random


def main():
    #define the characters to fight
    Jale = player.Player('Jale', 25, 3)                 #Defining the stats of the player 'name', 'hp', 'strength'
    Demonmonster = enemy.Enemy('Demonmonster', 20, 4)   #Defining the stats of the enemy 'name', 'hp', 'strength'

    '''
    Can always define more players and enemies, but the class needs to be modified so you can target more than
    one single object
    '''

    battles.battle_simulation(Jale, Demonmonster)       #If defining more than one character/enemy need to add to the parameters

if __name__ == '__main__':
    main()
