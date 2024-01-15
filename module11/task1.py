import random
from Warrior import Warrior

class Program:
    @staticmethod
    def main():
        firstWarrior = Warrior()
        secondWarrior = Warrior()
        while not firstWarrior.is_dead() and not secondWarrior.is_dead():
            match random.randint(0, 2):
                case 0:
                    secondWarrior.take_damage(firstWarrior.get_power())
                    print(f"Атаковал первый юнит. У второго юнита осталось {secondWarrior.get_health()} здоровья")
                case 1:
                    firstWarrior.take_damage(secondWarrior.get_power())
                    print(f"Атаковал второй юнит. У первого юнита осталось {firstWarrior.get_health()} здоровья")
        print(f"Одержал победу {'первый' if secondWarrior.is_dead() else 'второй'} юнит")

if __name__ == '__main__':
    Program.main()