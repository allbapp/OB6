# Создайте простую текстовую боевую игру, где игрок
# и компьютер управляют героями с различными характеристиками.
# Игра состоит из раундов, в каждом раунде игроки по очереди наносят урон друг другу,
# пока у одного из героев не закончится здоровье.
 # Требования:
# 1. Используйте ООП (Объектно-Ориентированное Программирование) для создания классов героев.
# 2. Игра должна быть реализована как консольное приложение.
# Классы:
# Класс `Hero`:
# - Атрибуты:
# - Имя (`name`)
# - Здоровье (`health`), начальное значение 100
# - Сила удара (`attack_power`), начальное значение 20
# - Методы:
# - `attack(other)`: атакует другого героя (`other`), отнимая здоровье в размере своей силы удара
# - `is_alive()`: возвращает `True`, если здоровье героя больше 0, иначе `False`
# Класс `Game`:
# - Атрибуты:
# - Игрок (`player`), экземпляр класса `Hero`
# - Компьютер (`computer`), экземпляр класса `Hero`
# - Методы:
# - `start()`: начинает игру, чередует ходы игрока и компьютера,
# пока один из героев не умрет. Выводит информацию о каждом ходе
# (кто атаковал и сколько здоровья осталось у противника) и объявляет победителя.

import random
class Hero:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health


    def attack(self, other):
        self.attack_power = random.randint(20, 35)
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")

    def is_alive(self):
        return self.health > 0

class Game(Hero):
    def __init__(self):
        self.player = Hero("Игрок", 100)
        self.computer = Hero("Компьютер", 100)

    def start(self):
        print("Игра начинается!")
        round_counter = 1
        while self.player.is_alive() and self.computer.is_alive():
            print(f"\nРаунд {round_counter}")
            self.player.attack(self.computer)
            if self.computer.is_alive():
                self.computer.attack(self.player)
            round_counter += 1
            print(f"Здоровье {self.player.name} : {self.player.health}")
            print(f"Здоровье {self.computer.name} : {self.computer.health}")

        if self.player.is_alive():
            print(f"{self.player.name} Победил!")
        else:
            print(f"{self.computer.name} Победил!")
        print("Игра закончена.")


game = Game()
game.start()
