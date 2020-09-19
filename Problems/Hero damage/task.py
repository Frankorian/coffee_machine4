hero_damage = 100


def double_damage():
    global hero_damage
    hero_damage = hero_damage * 2

double_damage()

def disarmed():
    dis = int(hero_damage * 0.1)
    print(dis)

disarmed()

def power_potion():
    potion = hero_damage + 100
    print(potion)

power_potion()