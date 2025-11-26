class Fire:
  def cast(self):
    print('Огонь')    

class Air:
  def cast(self):
    print('Воздух')    

class Water:
  def cast(self):
    print('Вода')    

class Earth:
  def cast(self):
    print('Земля')    

class Avatar(Air, Water, Earth, Fire):
  def cast(self):
    print('Аватар владеет всеми стихиями!')

aang = Avatar()
aang.cast()
  

