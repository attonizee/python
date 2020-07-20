class Pokemon(object):
    pokemons_type = {'fire': {
        'water': 0.5, 'grass': 2, 'fire': 0.5
    }, 'water': {
        'fire': 2, 'grass': 0.5, 'water': 0.5
    }, 'grass': {
        'fire': 0.5, 'water': 2, 'grass': 0.5}
        }
    def __init__(self, name, level, p_type, max_health, cur_health, is_knocked_out):
        self.name = name
        self.level = level
        self.p_type = p_type
        self.max_health = max_health
        self.cur_health = cur_health
        self.is_knocked_out = is_knocked_out

    def lose_health(self, damage):
        if self.cur_health != 0:
            self.cur_health -= damage
            return f'{self.name} lose {damage} health and has {self.cur_health} health'
        else:
            return f'{self.name} is knocked out'

    def regain_health(self, heal):
        if self.cur_health == 0:
            self.cur_health += heal
            return f'{self.name} is revived and has {self.cur_health} health'
        else:
            self.cur_health += heal
            return f'{self.name} is healed {heal} health'

    def knocked_out(self):
        if self.cur_health == 0:
            return f'{self.name} is knocked out'

    def attack(self, other_pokemon):
        pokemon = self.pokemons_type[self.p_type]
        modificator = pokemon[other_pokemon.p_type]
        damage = other_pokemon.level * modificator
        return damage

charmeleon = Pokemon('Charmeleon', 5, 'fire', 15, 15, False)
charizard = Pokemon('Charizard', 4, 'fire', 12, 12, False)

