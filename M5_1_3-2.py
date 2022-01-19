import random


class Warrior:
    def __init__(self, health, endurance, armor):
        self.health = health
        self.endurance = endurance
        self.armor = armor

    def attack(self):
        if self.endurance > 0:
            self.endurance -= 10
            return self.endurance

        else:
            self.endurance = 0
            return self.endurance

    def defend(self):
        if self.armor > 0:
            self.armor -= random.randint(0, 10)
            return self.armor

        elif self.armor < 0:
            self.armor = 0
            return self.armor

        if self.health > 10 and self.armor > 0 and self.endurance > 0:
            self.health -= random.randint(0, 20)
            return self.health


        elif self.health > 10 and not self.armor > 0 and self.endurance > 0:
            self.health -= random.randint(10, 20)
            return self.health

        elif self.health > 10 and self.armor > 0 and not self.endurance > 0:
            self.health -= random.randint(0, 10)
            return self.health

        elif self.health > 10 and not self.armor > 0 and not self.endurance > 0:
            self.health -= random.randint(0, 10)
            return self.health

        else:
            self.health = 10
        return self.health


unit1 = Warrior(100, 100, 100)
unit2 = Warrior(100, 100, 100)

while unit2.health > 10 and unit1.health > 10:

    n = random.randint(1, 4)
    if n == 1:
        unit1.attack()
        print("Атаковал первый,осталось выносливости у первого: ", unit1.endurance)
        unit2.defend()
        print("Атаковал первый,осталось брони у второго: ", unit2.armor, "Осталось здоровья у второго: ", unit2.health)
    elif n == 2:
        unit2.attack()
        print("Атаковал второй,осталось выносливости у второго: ", unit2.endurance)
        unit1.defend()
        print("Атаковал второй,осталось брони у первого: ", unit1.armor, "Осталось здоровья у первого: ", unit1.health)
    elif n == 3:
        unit1.attack()
        print("Атаковал первый,осталось выносливости у первого: ", unit1.endurance)
        unit2.attack()
        print("Атаковал второй,осталось выносливости у второго: ", unit2.endurance)
        unit2.defend()
        print("Атаковал первый,осталось брони у второго: ", unit2.armor, "Осталось здоровья у второго: ", unit2.health)
        unit1.defend()
        print("Атаковал второй,осталось брони у первого: ", unit1.armor, "Осталось здоровья у первого: ", unit1.health)
    elif n == 4:
        print("Оба защищаются")

else:

    print("Pollice verso")
if unit2.health <= 10:
    print("Выиграл первый игрок")
elif unit1.health <= 10:
    print("Выиграл второй игрок")
