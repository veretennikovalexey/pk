import math

угол, скорость = int( input() ), int( input() )
# угол, v = 45, 30

x = math.radians( угол )
g = 9.8 # м/с²

d = round( v**2 * math.sin( 2 *x ) / g, 2 )

print( F'''\
Дальность полета птицы: { d } метров''' )

'''
Дальность полета птицы: 91.84 метров
'''