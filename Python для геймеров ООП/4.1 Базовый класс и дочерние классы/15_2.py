class Block:
    def __init__(self, name:str, hardness:int=None, breakable:bool=None):
        self.name = name
        self.hardness = hardness
        self.breakable = breakable

    def show_info(self):
        print(f'Блок: {self.name}')        
        print(f'Прочность: {self.hardness}')        
        print(f'Можно сломать: {self.breakable}')        
        print()


class Stone(Block):
    def __init__(self):
        super().__init__(type(self).__name__)

    def set_properties(self):
        self.hardness = 10
        self.breakable = True


class Bedrock(Block):
    def __init__(self):
        super().__init__(type(self).__name__)

    def set_properties(self):
        self.hardness = 999
        self.breakable = False


class GrassBlock(Block):
    def __init__(self):
        super().__init__(type(self).__name__)

    def set_properties(self):
        self.hardness = 1
        self.breakable = True


'''
Anonymous 551300997
https://stepik.org/users/551300997/profile
https://stepik.org/lesson/1978938/step/15?discussion=12668999&thread=solutions&unit=2006692
'''


