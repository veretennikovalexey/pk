class Block:
    def __init__(self, name='', hardness=0, breakable=True):
        self.name = name
        self.hardness = hardness
        self.breakable = breakable

    def show_info(self):
        print(f'Блок: {self.name}')        
        print(f'Прочность: {self.hardness}')        
        print(f'Можно сломать: {self.breakable}')        
        print()

class Stone(Block):
    def set_properties(self):
        self.name = 'Stone'
        self.hardness = 10
        self.breakable = True

class Bedrock(Block):
    def set_properties(self):
        self.name = 'Bedrock'
        self.hardness = 999
        self.breakable = False

class GrassBlock(Block):
    def set_properties(self):
        self.name = 'GrassBlock'
        self.hardness = 1
        self.breakable = True




