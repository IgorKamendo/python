class Warrior:
    def __init__(self, health):
        self.health = health

    def attack(self):
        if self.health > 0:
            self.health -= 20
            return self.health
        else:
            self.health = 0
        return self.health


unit1 = Warrior(100)
unit2 = Warrior(100)

while unit2.health != 0 and unit1.health != 0:
    n = input("Атакует игрок 1 или 2? ")
    if n == "1":
        unit2.attack()
        print("Атаковал первый,осталось здоровья у второго: ", unit2.health)
    elif n == "2":
        unit1.attack()
        print("Атаковал второй,осталось здоровья у первого: ", unit1.health)
else:

    print("Игра закончена")
if unit2.health == 0:
    print("Выиграл первый игрок")
elif unit1.health == 0:
    print("Выиграл второй игрок")
