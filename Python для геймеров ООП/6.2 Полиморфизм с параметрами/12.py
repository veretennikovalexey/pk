class Trap:
    def use(self, seconds):
        print("Ловушка активируется!")

def activate(item):
    item.use(7)

activate(Trap())        