import random


class Hero:
    def __init__(self, name, health=100):  # Убрал attack_power из параметров
        self.name = name
        self.health = health

    def attack(self, other):
        # Генерация случайного урона для каждой атаки
        attack_power = random.randint(20, 35)
        other.health -= attack_power
        print(f"{self.name} атакует {other.name} и наносит {attack_power} урона.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self):
        self.player = Hero(name="Игрок", health=100)
        self.computer = Hero(name="Компьютер", health=100)  # Убрал attack_power, т.к. он теперь не нужен

    def start(self):
        print("Игра начинается!")
        round_counter = 1
        while self.player.is_alive() and self.computer.is_alive():
            print(f"\nРаунд {round_counter}")
            self.player.attack(self.computer)
            if self.computer.is_alive():
                self.computer.attack(self.player)
            round_counter += 1
            print(f"Здоровье {self.player.name}: {self.player.health}")
            print(f"Здоровье {self.computer.name}: {self.computer.health}")

        if self.player.is_alive():
            print(f"\n{self.player.name} победил!")
        else:
            print(f"\n{self.computer.name} победил!")
        print("Игра закончена.")


# Запуск игры
game = Game()
game.start()