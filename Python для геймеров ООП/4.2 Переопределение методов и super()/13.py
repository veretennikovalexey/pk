class Tool:
    def __init__(self, material, durability=100):
        self.material = material
        self.durability = durability

    def use(self, block):
        self.durability -= 1


class Pickaxe(Tool):
    def use(self, block):
        super().use(block)
        if block == 'камень':
            self.durability -= 2
        elif block == 'обсидиан':
            self.durability -= 5
        else:    
            self.durability -= 1

        if self.material == 'алмаз':
            self.durability += 1

        if self.durability < 0:
            self.durability = 0    

'''
Износ кирки
'''