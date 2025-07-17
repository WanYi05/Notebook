"""
from Enemy import *

enemy1 = Enemy()
enemy2 = Enemy()
enemy2.health_points = 100

print(enemy2.health_points)

"""
# ---------------------------------------

"""
from Enemy import *

enemy = Enemy()
enemy.type_of_enemy = "Zombie"


print(f'{enemy.type_of_enemy} has {enemy.health_points} health points and can do an attack of {enemy.attack_damage}')

"""

# ---------------------------------------

# Abstraction

# from Enemy import *

# enemy = Enemy()
# enemy.type_of_enemy = 'Zombie'

# print(enemy.talk())
# print(enemy.walk_forward())
# print(enemy.attack())

# zombie = Enemy('Zombie', 10, 1)
# zombie.__type_of_enemy = "Ogre"

# big_zombie = Enemy('Big zombie', 100, 10)

# zombie.type_of_enemy = 'Zombie'
# zombie.attack_damage = 1
# zombie.health_points = 10

# print(zombie.type_of_enemy)
# print(zombie.talk())


# print(zombie.get_type_of_enemy())

# print("-------------------")

# Inheritance in Python

# from Enemy import *
# from Zombie import *
# from Ogre import *

# zombie = Zombie(10, 1)
# ogre = Ogre(20, 3)

# print(zombie.get_type_of_enemy())
# print(zombie.talk())

# print(zombie.walk_forward())
# print(zombie.spread_disease())

# print(f'{zombie.get_type_of_enemy()} has {zombie.health_points} health points and can do attack of {zombie.attack_damage}')
# print(f'{ogre.get_type_of_enemy()} has {ogre.health_points} health points and can do attack of {ogre.attack_damage} ')

# zombie.talk()
# ogre.talk()



print("-------------------")

# Polymorphism in Python

from Zombie import *
from Ogre import *
import random

def battle (e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        print('-----------------')
        e1.special_attack()
        e2.special_attack()
        print(f'{e1.get_type_of_enemy()}: {e1.health_points} HP left')
        print(f'{e2.get_type_of_enemy()}: {e2.health_points} HP left')
        e2.attack()
        e1.health_points -= e2.attack_damage
        e1.attack()
        e2.health_points -= e1.attack_damage

    print('------------')

    if e1.health_points > 0:
        print(f'{e1.get_type_of_enemy()} wins!')

    else:
        print(f'{e2.get_type_of_enemy()} wins!')


zombie = Zombie(10, 1)
ogre = Ogre(20, 3)

# battle(zombie)
# battle(ogre) 

battle(zombie, ogre)