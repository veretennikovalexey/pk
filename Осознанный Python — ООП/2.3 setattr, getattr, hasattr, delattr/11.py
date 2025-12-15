class Pokemon:
    pass


pokemons = Pokemon()
creatures = ['pikachu', 'scyther', 'gyarados', 'gengar']

for creature in creatures:
    setattr(pokemons, creature, "")

for _ in ["lapras", "pikachu", "alakazam"]:
    print( hasattr(pokemons, _) )