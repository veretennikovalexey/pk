class Npc:
    def talk(self):
        self.__think()
        print('NPC говорит...')

    def __think(self):
        print('NPC думает...')