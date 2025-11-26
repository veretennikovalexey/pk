class Door:
# Закрытая дверь (на свежей земле)
    def __init__(self, required_level=1):
        self.required_level = required_level
        self.opened = False

    def open(self, key_level):
        if key_level >= self.required_level:
            self.opened = True
        return self.opened


class MagicDoor(Door):    
# Магическая дверь
    def __init__(self, required_level=1, mana_cost=10):
        super().__init__(required_level)
        self.mana_cost = mana_cost

    def open(self, key_level, has_master_key=False, mana=0):
        if super().open(key_level):
            return True
        elif has_master_key and mana >= self.mana_cost:
            self.opened = True   
        return self.opened