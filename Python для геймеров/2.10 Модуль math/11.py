from math import sqrt, pi 

mana = float( input() )
coefficient = float( input() )

r = sqrt( mana ) * coefficient
S = pi * r ** 2
L = 2 * pi * r

print( F'''\
Площадь защитного поля: { round( S, 2 ) }
Длина окружности защитного поля: { round( L, 2 ) }''' )


'''
Площадь защитного поля: 106.03
Длина окружности защитного поля: 36.5
'''