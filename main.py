class Hero:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack


class Boss:
    def __init__(self, health, attack):
        self.health = health
        self.attack = attack


class Witcher(Hero):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.revive_chance = 0.5

    def revive_hero(self, fallen_hero):
        if random.random() < self.revive_chance:
            print(f"{self.name} оживляет {fallen_hero.name}, пожертвовав своей жизнью.")
            fallen_hero.health = 100
            self.health = 0
        else:
            print("Шанс оживления не сработал.")


class Magic(Hero):
    def __init__(self, name, health, attack, bonus_attack):
        super().__init__(name, health, attack)
        self.bonus_attack = bonus_attack

    def increase_attack(self):
        self.attack += self.bonus_attack


class Hacker(Hero):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)

    def hack_boss(self, boss):
        stolen_health = random.randint(10, 30)
        boss.health -= stolen_health
        self.health += stolen_health
        print(f"{self.name} взламывает босса и передает {stolen_health} здоровья себе.")


# Создание героев и босса
witcher = Witcher("Геральт", 100, 20)
magic = Magic("Мерлин", 120, 15, 5)
hacker = Hacker("Хакер", 90, 25)
boss = Boss(500, 40)

# Пример использования суперспособностей
magic.increase_attack()
print(f"{magic.name} усиливает атаку на {magic.bonus_attack}.")

hacker.hack_boss(boss)

fallen_hero = Hero("Погибший герой", 0, 0)
witcher.revive_hero(fallen_hero)

import random

class Golem(Hero):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.damage_reduction = 0.2  # Уменьшение урона от босса на 20%

    def take_damage(self, damage):
        reduced_damage = damage * self.damage_reduction
        self.health -= reduced_damage

class Avrora(Hero):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.invisibility_used = False

    def activate_invisibility(self):
        if not self.invisibility_used:
            print(f"{self.name} входит в режим невидимости.")
            self.invisibility_used = True
        else:
            print("Режим невидимости уже был активирован.")

    def take_damage(self, damage):
        if self.invisibility_used:
            print(f"{self.name} получает урон от босса.")
            self.health -= damage
            print(f"Босс получает {damage} урона от {self.name}.")
            boss.health += damage

class Druid(Hero):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.angel_summoned = False
        self.crow_summoned = False

    def summon_helper(self, medic=None):
        if not self.angel_summoned and not self.crow_summoned:
            summon_type = random.choice(["angel", "crow"])
            if summon_type == "angel":
                print(f"{self.name} призывает помощника - ангела.")
                self.angel_summoned = True
                medic.heal_power += 10  # Увеличение способности медика на лечение
            else:
                print(f"{self.name} призывает помощника - ворона.")
                self.crow_summoned = True
                if boss.health < 250:  # Если у босса осталось менее 50% здоровья
                    boss.attack *= 1.5  # Увеличение урона босса на 50%

class Thor(Hero):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)

    def attack_boss(self):
        if random.random() < 0.3:  # Шанс оглушить босса
            print(f"{self.name} оглушает босса на 1 раунд.")
            boss.stunned = True

class TrickyBastard(Hero):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.play_dead_round = random.randint(1, 5)  # Раунд, в котором он сыграет мертвого
        self.dead = False

    def play_dead(self, current_round):
        if current_round == self.play_dead_round:
            print(f"{self.name} притворяется мертвым.")
            self.dead = True
            self.health = 0

class Antman(Hero):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.default_size = "normal"

    def change_size(self):
        sizes = ["normal", "small", "large"]
        new_size = random.choice(sizes)
        if new_size != self.default_size:
            if new_size == "small":
                self.health -= 20
                self.attack -= 5
            elif new_size == "large":
                self.health += 20
                self.attack += 5
            self.default_size = new_size
            print(f"{self.name} изменил размер на {new_size}.")

class Deku(Hero):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)

    def attack_boss(self):
        attack_strength = random.choice([0.2, 0.5, 1.0])
        damage_taken = 0
        if attack_strength > 0:
            damage_taken = attack_strength * self.attack
            self.health -= damage_taken
            print(f"{self.name} атакует босса с силой {attack_strength * 100}% и теряет {damage_taken} здоровья.")
        return attack_strength * self.attack

class Kamikadze(Hero):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)

    def sacrifice(self, target):
        if random.random() < 0.8:  # Шанс попасть точно в цель
            target.health -= target.health / 2
            print(f"{self.name} жертвует собой и наносит половину своего здоровья урона {target.name}.")
        else:


            target.health -= target.health / 4
            print(f"{self.name} промахивается и наносит половину своего здоровья урона {target.name}.")

class Samurai(Hero):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)

    def throw_shuriken(self):
        shuriken_type = random.choice(["virus", "vaccine"])
        if shuriken_type == "virus":
            boss.health -= random.randint(10, 30)
            print(f"{self.name} кидает вирус и наносит урон боссу.")
        else:
            boss.health += random.randint(10, 30)
            print(f"{self.name} кидает вакцину и лечит босса.")

class Bomber(Hero):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)

    def explode(self):
        print(f"{self.name} взрывается и наносит боссу дополнительный урон.")
        boss.health -= 100

class Reaper(Hero):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)

    def calculate_damage(self):
        if self.health < 0.3 * self.max_health:
            return 3 * self.attack
        elif self.health < 0.15 * self.max_health:
            return 2 * self.attack
        else:
            return self.attack
