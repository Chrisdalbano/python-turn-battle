import decorators as dec
import random
import time

class Player:

    myTurn = False                  #checks if class's turn
    is_dodging = False              #checker for if this entity is dodging


    '''
    The following list defines all the actions that the character is able to choose
    '''

    player_actions = [
    "Attack",
    "Run",
    "Dodge",
    "Super"
    ]

    def __init__(self, name, hp, str):
        self.name = name
        self.hp = hp
        self.str = str

        self.super_attack = True            #The super attacks it's initialized True because it can only
                                            #be used once, and after used it becomes False
    def check_enemy_lives(self, target):
        return target.hp

    def pass_turn(self, next):
        self.myTurn = False
        next.myTurn = True
        pass


    '''
    The following attack function defines all the attack and their stats,
    checks the strength from the user and do some calculations to return
    the strike.

    As a default you have the basic attack and the super attack.
    '''

    def attack(self, target, skill):
        '''
        The 'target' parameter would be the entity that the skill is targetting
        The 'skill' parameter is the name of the ability that is going to be used
        '''

        time.sleep(1.0)
        if skill == 'bAttack':
            print('{} says: Here you go!, and strikes an attack.' .format(self.name))
            hit = random.randint(self.str - 2, self.str + 2)
            if hit > self.str + 1:
                print('Critical Strike!!!')

            time.sleep(1.0)
            print('{}: -{} HP '.format(target.name, hit))
            time.sleep(1.0)

            target.hp -= hit

            if target.hp <= 0:
                time.sleep(1.0)
                print('{} falls!\n {} has won the combat!!! \n{}'.format(target.name, self.name, dec.Decorators.death_decorator))
                exit()
            return self.check_enemy_lives(target)
            self.pass_turn(target)

        elif skill == 'sAttack':
            print('{} says: Here IT GOES' .format(self.name))
            hit = random.randint(self.str + 4, self.str + 6)
            if hit > self.str + 5:
                print('Critical Strike!!!')

            time.sleep(1.0)
            print('{}: -{} HP '.format(target.name, hit))
            time.sleep(1.0)

            target.hp -= hit

            if target.hp <= 0:
                time.sleep(1.0)
                print('{} falls!\n {} has won the combat!!! \n{}'.format(target.name, self.name, dec.Decorators.death_decorator))
                exit()
            return self.check_enemy_lives(target)
            self.pass_turn(target)

    def show_player_actions(self):
        return player_actions

    def decision(self, player_actions, target_enemy):
        '''
        The decision function checks the action that the entity decides to use
        'player_actions' returns the list of the actions that we have available
        'target_enemy' parameter is the target where the actions are being applied
        on
        '''
        print("[YOUR HP: {} ] \n[{} HP: {}] \n \n".format(self.hp, target_enemy.name, target_enemy.hp))
        my_actions = "][".join(player_actions)
        my_decision = input("What would you do? \n{}\n [your_action> ".format(my_actions))
        time.sleep(1.0)

        if my_decision.lower() == 'attack':
            time.sleep(1.0)
            print(dec.Decorators.decorator)
            return self.attack(target_enemy, 'bAttack')
            time.sleep(1.0)
            self.pass_turn(target_enemy)

        elif my_decision.lower() == 'super':
            if self.super_attack == True:
                self.super_attack = False       #Since the super attack can only be used once, it becomes False so we cannot use it.
                time.sleep(1.0)
                print(dec.Decorators.special_decorator)
                return self.attack(target_enemy, 'sAttack')
                time.sleep(1.0)
                self.pass_turn(target_enemy)

            else:
                print('You can only use the Super Attack once...')
                return self.decision(player_actions, target_enemy)

        elif my_decision.lower() == 'run':
            print(dec.Decorators.decorator)
            roll_a_coin = random.choice([1,2])
            if roll_a_coin == 1:
                time.sleep(1.0)
                print('You cannot escape this time...')
                time.sleep(1.0)
                return self.check_enemy_lives(target_enemy)
                self.pass_turn(target_enemy)
            else:
                time.sleep(1.0)
                print('Sucessfully escaped the combat like a coward\n {}'.format(dec.Decorators.player_run))
                exit()


        elif my_decision.lower() == 'dodge':

            '''
            The dodge decision checks if the bool is_dodging to determine if the entity is able to
            dodge the next strike
            '''
            print(dec.Decorators.decorator)
            roll_a_coin = random.choice([1,2,3])
            if roll_a_coin == 2:
                print('You dodge next strike')
                time.sleep(1.0)
                self.is_dodging = True  #We roll a dice, if it success then becomes True meaning that the entity will dodge the attack
                self.pass_turn(target_enemy)
                return self.check_enemy_lives(target_enemy)

            else:
                time.sleep(1.0)
                print('Fail to doge.')
                time.sleep(1.0)
                self.pass_turn(target_enemy)
                return self.check_enemy_lives(target_enemy)
        else:
            time.sleep(1.0)
            print('Thats not a valid action!\nType a valid action: \n')
            print(dec.Decorators.decorator)
            return self.decision(player_actions, target_enemy)
