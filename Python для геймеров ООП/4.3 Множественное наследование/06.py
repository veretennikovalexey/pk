class WarriorSkills:
    def __init__(self):
        print("Теперь вам доступны навыки Воина!")
        super().__init__() # BattleMage → WarrorSkills → MageSkills       


class MageSkills:
    def __init__(self):
        print("Теперь вам доступны навыки Мага!")        


class BattleMage(WarriorSkills, MageSkills):
    def __init__(self):
        print("Создаю Мага-Воина...")
        super().__init__() # BattleMage → WarrorSkills → MageSkills
        

hero = BattleMage()