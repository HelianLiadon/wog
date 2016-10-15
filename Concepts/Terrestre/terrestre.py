import math

class Unit:
    dmg = {'tank' : 0, 'aviation': 0, 'artillery': 0}
    def attack(self, unit_type):
        return (self.dmg[unit_type] / 20.) * self.dmg_bonus
    def increase_att(self):
        if self.nbr == 0:
            self.dmg_bonus = 0
        elif self.func == "loga":
            self.dmg_bonus += self.nbr * math.log(self.day + 2, 2) / 4.
        elif self.func == "expo":
            self.dmg_bonus += self.nbr * math.pow(2, self.day - 10)
        else:
            raise Exception()

class Tank(Unit):
    def __init__(self, func, nbr=0):
        self.nbr = nbr
        self.day = 0
        self.func = func
        self.dmg = {'tank': 10, 'aviation': 2, 'artillery': 15}
        self.dmg_bonus = 0

class Aviation(Unit):
    def __init__(self, func, nbr=0):
        self.nbr = nbr
        self.day = 0
        self.func = func
        self.dmg = {'tank': 15, 'aviation': 8, 'artillery': 5}
        self.dmg_bonus = 0

class Artillery(Unit):
    def __init__(self, func, nbr=0):
        self.nbr = nbr
        self.day = 0
        self.func = func
        self.dmg = {'tank': 2, 'aviation': 18, 'artillery': 2}
        self.dmg_bonus = 0

units1 = { 'tank_log': Tank("loga"), 'tank_exp': Tank("expo"), 'aviation_log': Aviation('loga'), 'aviation_exp': Aviation('expo'), 'artillery_log': Artillery('loga'), 'artillery_exp': Artillery('expo') }
units2 = { 'tank_log': Tank("loga"), 'tank_exp': Tank("expo"), 'aviation_log': Aviation('loga'), 'aviation_exp': Aviation('expo'), 'artillery_log': Artillery('loga'), 'artillery_exp': Artillery('expo') }


def reinforcements(units):
    recruit = input("Reinforce?[y/N] ")
    if recruit == "y":
        units['tank_log'].nbr += int(input("Logarithmic Tanks: "))
        units['tank_exp'].nbr += int(input("Exponential Tanks: "))
        units['aviation_log'].nbr += int(input("Logarithmic Aviation: "))
        units['aviation_exp'].nbr += int(input("Exponential Aviation: "))
        units['artillery_log'].nbr += int(input("Logarithmic Artillery"))
        units['artillery_exp'].nbr += int(input("Exponential Artillery"))

def kill(units, unit_type, dmg):
    if units[unit_type + '_log'].nbr >= dmg / 2 and units[unit_type + '_exp'].nbr >= dmg / 2:
        units[unit_type + '_log'].nbr -= dmg/2
        units[unit_type + '_exp'].nbr -= dmg/2

    elif units[unit_type + '_log'].nbr >= dmg / 2:
        dmg -= units[unit_type + '_exp'].nbr
        units[unit_type + '_exp'].nbr = 0
        units[unit_type + '_log'].nbr -= dmg

    elif units[unit_type + '_exp'].nbr >= dmg / 2:
        dmg -= units[unit_type + '_log'].nbr
        units[unit_type + '_log'].nbr = 0
        units[unit_type + '_exp'].nbr -= dmg

    else:
        units[unit_type + '_log'].nbr = 0
        units[unit_type + '_exp'].nbr = 0

def turn():
    dmg_tanks1 = 0
    dmg_art1 = 0
    dmg_avia1 = 0
    dmg_tanks2 = 0
    dmg_art2 = 0
    dmg_avia2 = 0
    for unit in units1.values():
        dmg_tanks1 += unit.attack("tank")
        dmg_art1 += unit.attack("artillery")
        dmg_avia1 += unit.attack("aviation")
    for unit in units2.values():
        dmg_tanks2 += unit.attack("tank")
        dmg_art2 += unit.attack("artillery")
        dmg_avia2 += unit.attack("aviation")

    print("Damages:\n\tArmy1:\n\t\tAnti-tanks:{}\n\t\tAnti-artilllery:{}\n\t\tAnti-aviation:{}\n\tArmy2:\n\t\tAnti-tanks:{}\n\t\tAnti-artilllery:{}\n\t\tAnti-aviation:{}\n".format(round(dmg_tanks1), round(dmg_art1), round(dmg_avia1), round(dmg_tanks2), round(dmg_art2), round(dmg_avia2)))

    kill(units1, 'tank', dmg_tanks2)
    kill(units1, 'artillery', dmg_art2)
    kill(units1, 'aviation', dmg_avia2)
    kill(units2, 'tank', dmg_tanks1)
    kill(units2, 'artillery', dmg_art1)
    kill(units2, 'aviation', dmg_avia1)

    print("Surviving:\n\tArmy1:")
    for i in units1.keys():
        print("\t\t{}: {}".format(i, round(units1[i].nbr)))
    print("\tArmy2:")
    for i in units2.keys():
        print("\t\t{}: {}".format(i, round(units2[i].nbr)))


    print("=== Reinforcements ===\n\t---Army 1---")
    reinforcements(units1)
    print("\t---Army 2---")
    reinforcements(units2)

    for i in units1.values():
        i.day += 1
        i.increase_att()
    for i in units2.values():
        i.day += 1
        i.increase_att()

print("=== Reinforcements ===\n\t---Army 1---")
reinforcements(units1)
print("\t---Army 2---")
reinforcements(units2)

for i in units1.values():
    i.day += 1
    i.increase_att()
for i in units2.values():
    i.day += 1
    i.increase_att()


while True:
    alive = False
    for i in units1.values():
        if i.nbr > 0:
            alive = True
    for i in units2.values():
        if i.nbr > 0:
            alive = True
    if not alive:
        break
    turn()
