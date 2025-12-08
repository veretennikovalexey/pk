class EnderChest:
    '''Сундук Края (Ender Chest)'''
    inventory = []

    def add(self, item):
        EnderChest.inventory.append(item)

    def show(self):
        return EnderChest.inventory