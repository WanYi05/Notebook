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

# Abstration

from Enemy import *

# enemy = Enemy()
# enemy.type_of_enemy = 'Zombie'

# print(enemy.talk())
# print(enemy.walk_forward())
# print(enemy.attack())

zombie = Enemy()
zombie.type_of_enemy = 'Zombie'

print(zombie.attack())
