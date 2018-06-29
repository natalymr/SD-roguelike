class BasicMonster:
    """
    This is an interface for ai-monsters.
    """

    def take_turn(self, target, game_map, entities):
        """
        This function determines the behavior of monsters that are close to the player.
        """
        results = []

        monster = self.owner

        if game_map.fov[monster.x, monster.y]:
            if monster.distance_to(target) >= 2:
                monster.move_towards(target.x, target.y, game_map, entities)

            elif target.fighter.hp > 0:
                attack_results = monster.fighter.attack(target)
                results.extend(attack_results)

        return results