class Miner:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def mine(self):
        print(f"{self.name} копает...")

class GoldMiner(Miner):
    def mine(self):
        self.inventory.append("золото")

class StoneMiner(Miner):
    def mine(self):
        self.inventory.append("камень")

miner1 = GoldMiner("Мух")
miner2 = StoneMiner("Зяб")

miner1.mine()
miner2.mine()

print(miner1.inventory)
print(miner2.inventory)