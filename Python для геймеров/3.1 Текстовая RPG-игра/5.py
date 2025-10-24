from math import sqrt;

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())

distance = sqrt( (x2-x1) ** 2 + (y2-y1) ** 2 )
distance = round( distance, 2 )

print( F'''\
=== Я свободен! ===

Расстояние между мной ({x1}; {y1}) и ближайшим поселением ({x2}; {y2}) составляет {distance} точек''')

'''
=== Я свободен! ===

Расстояние между мной (x1; y1) и ближайшим поселением (x2; y2) составляет {distance} точек
'''