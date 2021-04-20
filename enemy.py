import decorators as dc
import time
import random

class Enemy:
    myTurn = False

    enemy_actions = [
    'Attack '
    'Dodge '
    'Heal '
    ]

    def __init__(self, name, hp, str):
        self.name = name
        self.hp = hp
        self.str = str

        self.MAX_HP = hp
        self.behavior_counter = 100
        self.MAX_BEHAVIOR = 100
        self.myBehavior = 'AGGRESIVE'

    def behavior_types(self):
        behavior_list = [
        'PASSIVE',
        'AGGRESIVE',
        'SCARED',
        'HOPELESS'
        ]

    def attack(self, target, skill):

        hit = random.randint(int(self.str /2), self.str)

        if skill == 'BASIC':
            print('{} beastly strikes an attack.' .format(self.name))
            hit = random.randint(self.str - 1, self.str + 1)
            time.sleep(1.5)
            if hit > self.str + 1:
                print('Critical Strike!!!')

            time.sleep(0.5)

        elif skill == 'BITE':
            print('{} beastly strikes a huge bite' .format(self.name))
            hit = random.randint(int(self.str /2), self.str)
            healing = random.choice([hit - 1, hit])

            if target.is_dodging != True:
                if self.hp + healing > self.MAX_HP:
                    self.hp = self.MAX_HP
                else:
                    self.hp += healing

            else:
                print('{} dodges the bite!'.format(target.name))

            time.sleep(1.5)
            if hit > self.str + 1:
                print('Critical Strike!!!')

            time.sleep(0.5)


        if target.is_dodging == False:
            print('{}: -{} HP '.format(target.name, hit))
            if skill == 'BITE':
                print('{}: +{} HP'.format(self.name, healing))
            time.sleep(1.0)
            target.hp -= hit
        else:
            roll_a_coin = random.choice([1,2])
            counterattack = 0
            if roll_a_coin == 1:
                counterattack = int(hit/ 2)
                self.hp -= counterattack
            print('{}: Dodges the attack,\nand deals as a counterattack: {} DMG to {}'.format(target.name, counterattack, self.name))
            target.is_dodging = False

            if self.hp <= 0:
                time.sleep(1.0)
                print('{} dies!\n {} has won the combat!\n{}'.format(self.name, target.name, dec.Decorators.death_decorator))
                exit()

        if target.hp <= 0:
            time.sleep(1.0)
            print('{} dies!\n {} has won the combat!\n{}'.format(target.name, self.name, dec.Decorators.death_decorator))
            exit()

        elif skill == 'GG':
            hit = 0
            print('{} is very hopeless.\nHe rathers do nothing.'.format(self.name))

        return target.hp

    def pass_turn(self, next):
        self.myTurn = False
        next.myTurn = True
        pass

    def check_lives(self):
        return self.hp
        if self.hp <= 0:
            print('{} dies.'.format(self.name))


    def enemy_decision(self, target):

        if self.hp * 2 <= target.hp:
            self.behavior_counter -= 50
        elif self.hp < target.hp:
            self.behavior_counter -= 25
        elif self.hp > target.hp * 2:
            self.behavior_counter += 50
        elif self.hp > target.hp:
            self.behavior_counter += 25

        #resetting the behavior counter if it goes over
        if self.behavior_counter > 100:
            self.behavior_counter = 100

        #resetting the behavior counter if it goes under
        if self.behavior_counter < 0:
            self.behavior_counter = 0

        #establishing the enemys behavior based on stats
        if self.behavior_counter == 100:
            self.myBehavior = 'AGGRESIVE'
        elif self.behavior_counter > 50 and self.behavior_counter <= 75:
            self.myBehavior = 'PASSIVE'
        elif self.behavior_counter <= 50 and self.behavior_counter > 0 and self.hp - 1 < int(self.MAX_HP / 2):
            self.myBehavior = 'SCARED'
        elif self.behavior_counter <= 0 and self.hp - 1 < int(self.MAX_HP / 2) and (self.hp + 1) * 2 <= target.hp:
            self.myBehavior = 'HOPELESS'

        print('BEHAVIOR_COUNTER: {} \n BEHAVIOR_STATUS: {}'.format(self.behavior_counter, self.myBehavior))

        hit = random.randint(int(self.str /2), self.str)
        healing = random.choice([hit - 1, hit])

        if self.myBehavior == 'AGGRESIVE': #If the enemy is aggresive he's only going to attack no matter what
            return self.attack(target, 'BASIC')
            if self.behavior_counter <= 100 and self.hp == self.MAX_HP:
                if self.behavior_counter == 75:
                    self.behavior_counter += 25
                else:
                    pass
            else:
                self.behavior_counter -= 25
        elif self.myBehavior == 'PASSIVE':
            if self.myBehavior == 'PASSIVE':
                if self.hp < self.MAX_HP:
                    roll_a_coin = random.choice([1,2,3])
                    if self.hp + healing == self.MAX_HP:
                        if roll_a_coin == 2:
                            return self.attack(target, 'BITE')
                        else:
                            return self.attack(target, 'BASIC')

                    else:
                        roll_a_coin = random.choice([1,2,3,4,5])
                        if roll_a_coin == 2 or roll_a_coin == 5:
                            return self.attack(target, 'BITE')
                        else:
                            return self.attack(target, 'BASIC')

                else:
                    if hit >= self.hp:
                        return self.attack(target, 'BITE')
                    else:
                        roll_a_coin = random.choice([1,2,3])
                        if roll_a_coin == 1:
                            return self.attack(target, 'BITE')
                        else:
                            return self.attack(target, 'BASIC')

        elif self.myBehavior == 'SCARED':
            if self.myBehavior == 'SCARED':
                guess_one = random.randint(int(self.str /2), self.str)
                guess_two = random.randint(int(self.str /2), self.str)
                guess_three = random.randint(int(self.str /2), self.str)

                the_option = None

                if guess_one > guess_two and guess_one > guess_three:
                    the_option = guess_one
                elif guess_two > guess_three:
                    the_option = guess_two
                else:
                    the_option = guess_three

                if the_option >= target.hp:
                    print('{} : HAHA!!! you are dead!'.format(self.name))
                    return self.attack(target, 'BASIC')
                else:
                    roll_a_coin = random.choice([1,2,3,4])
                    if roll_a_coin == 3:
                        return self.attack(target, 'BASIC')
                    elif roll_a_coin == 4:
                        print('{} runs away like a coward! \n [END OF THE COMBAT]'.format(self.name))
                        print(dec.Decorators.player_run)
                        exit()
                    else:
                        return self.attack(target, 'BASIC')

        elif self.myBehavior == 'HOPELESS':
            roll_a_coin = random.choice([1,2,3])
            if self.myBehavior == 'HOPELESS' and (self.hp * 2) <= target.hp and self.hp + int(self.hp / 2) + 1 <= target.hp and (roll_a_coin == 1 or roll_a_coin == 3):
                return self.attack(target, 'GG')
            else:
                guess_one = random.randint(int(self.str /2), self.str)
                guess_two = random.randint(int(self.str /2), self.str)
                guess_three = random.randint(int(self.str /2), self.str)

                the_option = None

                if guess_one > guess_two and guess_one > guess_three:
                    the_option = guess_one
                elif guess_two > guess_three:
                    the_option = guess_two
                else:
                    the_option = guess_three

                if the_option >= target.hp:
                    print('{}: gonna try this one more time!'.format(self.name))
                    return self.attack(target, 'BASIC')
                else:
                    roll_a_coin = random.choice([1,2,3,4])
                    if roll_a_coin == 3 or roll_a_coin == 2:
                        return self.attack(target, 'BITE')
                    else:
                        return self.attack(target, 'BASIC')
