class Gun:
    def __init__(self, magazine_size, ammo_pack):
        self.__magazine_size = magazine_size
        self.__ammo_pack = ammo_pack
        self.__bullets_in_magazine = magazine_size 

    def __reload(self):
        print('Перезарядка...')
        if self.__magazine_size >= self.__ammo_pack: # магазин на 10 патронов, а в наличии только 3 патрона
            self.__bullets_in_magazine = self.__ammo_pack
            self.__ammo_pack = 0
        else:
            self.__bullets_in_magazine = self.__magazine_size 
            self.__ammo_pack -= self.__magazine_size  

    
    def shoot(self):        
        if self.__bullets_in_magazine == 0 and self.__ammo_pack == 0:
            print('Патроны закончились!')
            return
        
        if self.__bullets_in_magazine > 0:
            print('Выстрел!')
            self.__bullets_in_magazine -= 1
        else:            
            self.__reload()