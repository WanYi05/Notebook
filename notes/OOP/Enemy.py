class Enemy:

    # type_of_enemy: str
    # health_points: int = 10
    # attack_damage: int = 1

    def __init__(self, type_of_enemy, health_points, attack_damage):
        # print('Create new enemy!')
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage


    def talk(self):
        print(f'I am a {self.__type_of_enemy}. Be prepared to fight!')

    def walk_forward(self):
        print(f'{self.__type_of_enemy} moves closer to you.')

    def attack(self):
        print(f'{self.__type_of_enemy} attacks for {self.attack_damage} damage')

    def special_attack(self):
        print('Enemy has no special ')

    def get_type_of_enemy(self):
        return self.__type_of_enemy