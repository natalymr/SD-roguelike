from game_messages import Message


class Fighter:
    """
    This is an interface for any entity that is able to fight.
    """

    def __init__(self, hp, defense, power):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power
        self.equip_attack_tool = 0
        self.equip_defense_tool = 0

    def take_damage(self, amount):
        results = []

        self.hp -= amount

        if self.hp <= 0:
            results.append({'dead': self.owner})

        return results

    def heal(self, amount):
        self.hp += amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def attack_bonus(self, amount):
        self.power += amount
        self.equip_attack_tool = amount

    def defense_bonus(self, amount):
        self.defense += amount
        self.equip_defense_tool = amount

    def attack(self, target):
        results = []

        damage = self.power - target.fighter.defense

        if damage > 0:
            results.append({'message': Message('{0} attacks {1} for {2} hit points.'.format(
                self.owner.name.capitalize(), target.name, str(damage)))})
            results.extend(target.fighter.take_damage(damage))
        else:
            results.append({'message': Message('{0} attacks {1} but does no damage.'.format(
                self.owner.name.capitalize(), target.name))})

        return results