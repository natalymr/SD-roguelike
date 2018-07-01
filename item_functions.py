from game_messages import Message


def heal(*args, **kwargs):
    entity = args[0]
    colors = args[1]
    amount = kwargs.get('amount')

    results = []

    if entity.fighter.hp == entity.fighter.max_hp:
        results.append({'consumed': False, 'message': Message('You are already at full health', colors.get('yellow'))})
    else:
        entity.fighter.heal(amount)
        results.append({'consumed': True, 'message': Message('Your wounds start to feel better!', colors.get('green'))})

    return results


def equip_base_weapon(*args, **kwargs):
    entity = args[0]
    colors = args[1]
    amount = kwargs.get('amount')

    results = []

    if entity.fighter.equip_attack_tool == 0:
        entity.fighter.attack_bonus(amount)
        results.append({'consumed': False, 'message': Message('You feel yourself more powerful', colors.get('green'))})
    else:
        results.append({'consumed': False, 'message': Message('You are already have a weapon', colors.get('yellow'))})

    return results


def equip_base_armor(*args, **kwargs):
    entity = args[0]
    colors = args[1]
    amount = kwargs.get('amount')

    results = []

    if entity.fighter.equip_defense_tool == 0:
        entity.fighter.defense_bonus(amount)
        results.append({'consumed': False, 'message': Message('You feel yourself more protected', colors.get('green'))})
    else:
        results.append({'consumed': False, 'message': Message('You are already have a weapon', colors.get('yellow'))})

    return results


def drop(*args):
    pass


def drop_defense_tool(*args):
    entity = args[0]
    entity.fighter.defense -= entity.fighter.equip_defense_tool
    entity.fighter.equip_defense_tool = 0


def drop_attack_tool(*args):
    entity = args[0]
    entity.fighter.power -= entity.fighter.equip_attack_tool
    entity.fighter.equip_attack_tool = 0
