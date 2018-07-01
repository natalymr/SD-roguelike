import unittest
from entity import Entity
from item import Item
from item_functions import heal, equip_base_armor, equip_base_weapon

from fighter import Fighter
from inventory import Inventory
from render_functions import RenderOrder
import engine
fighter_component = Fighter(hp=30, defense=2, power=5)
inventory_component = Inventory(26)
player = Entity(0, 0, '@', (255, 255, 255), 'Player', blocks=True, render_order=RenderOrder.ACTOR,
                fighter=fighter_component, inventory=inventory_component)

colors = {
    'dark_wall': (0, 0, 100),
    'dark_ground': (50, 50, 150),
    'light_wall': (130, 110, 50),
    'light_ground': (200, 180, 50),
    'desaturated_green': (63, 127, 63),
    'darker_green': (0, 127, 0),
    'dark_red': (191, 0, 0),
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'orange': (255, 127, 0),
    'light_red': (255, 114, 114),
    'darker_red': (127, 0, 0),
    'violet': (127, 0, 255),
    'yellow': (255, 255, 0),
    'blue': (0, 0, 255),
    'green': (0, 255, 0)
}

class TestHPInteraction(unittest.TestCase):

    def test_attack(self):
        self.assertEqual(player.fighter.hp, 30)
        fighter_component.attack(player)
        self.assertNotEqual(player.fighter.hp, 30)

    def test_heal(self):
        player.fighter.hp = 27
        self.assertEqual(player.fighter.hp, 27)
        player.fighter.heal(3)
        self.assertEqual(player.fighter.hp, 30)

    def test_extra_heal(self):
        player.fighter.hp = 29
        self.assertEqual(player.fighter.hp, 29)
        player.fighter.heal(3)
        self.assertEqual(player.fighter.hp, 30)


class TestCheckItemBonus(unittest.TestCase):

    def test_healing_potion(self):
        fighter_component.attack(player)
        item_component = Item(use_function=heal, amount=4)
        item = Entity(0, 0, '!', colors.get('violet'), 'Healing Potion', render_order=RenderOrder.ITEM,
                      item=item_component)
        player.fighter.hp = 27
        item.item.use_function(player, colors, amount=4)
        self.assertEqual(player.fighter.hp, 30)
        item.item.use_function(player, colors, amount=4)
        self.assertEqual(player.fighter.hp, 30)

    def test_base_weapon(self):
        item_component = Item(use_function=equip_base_weapon, amount=5)
        item = Entity(0, 0, '?', colors.get('red'), 'Base weapon', render_order=RenderOrder.ITEM,
                       item=item_component)
        self.assertEqual(player.fighter.power, 5)
        item.item.use_function(player, colors, amount=5)
        self.assertEqual(player.fighter.power, 10)
        item.item.use_function(player, colors, amount=5)
        self.assertEqual(player.fighter.power, 10)

    def test_base_defense(self):
        item_component = Item(use_function=equip_base_armor, amount=3)
        item = Entity(0, 0, '?', colors.get('blue'), 'Base armor', render_order=RenderOrder.ITEM,
                       item=item_component)
        self.assertEqual(player.fighter.defense, 2)
        item.item.use_function(player, colors, amount=3)
        self.assertEqual(player.fighter.defense, 5)
        item.item.use_function(player, colors, amount=3)
        self.assertEqual(player.fighter.defense, 5)


if __name__ == '__main__':
    unittest.main()