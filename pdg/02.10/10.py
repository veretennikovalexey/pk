from math import sqrt, log

level = int(input())
luck = float(input())
base_damage = 10 * log(level + 1, 2)
crit_damage = round( base_damage * ( 1 + luck * sqrt(level) ), 2 )

print( F'''\
Базовый урон: { round( base_damage, 2 ) }
Критический урон: { crit_damage }''')


'''
Sample Input:

10
0.5
Sample Output:

Базовый урон: 34.59
Критический урон: 89.29
'''
