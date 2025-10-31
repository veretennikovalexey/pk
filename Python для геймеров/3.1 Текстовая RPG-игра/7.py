name, hero_class, health, armor, damage = input(), input(), int(input()), int(input()), float(input())

print( F'''\
=== Создание героя ===

Имя: {name}
Класс: {hero_class}
Здоровье: {health}, Броня: {armor}, Урон: {damage}''' )
  
guard_health, guard_armor, base_guard_attack = int(input()), int(input()), float(input())

magic_damage = round( damage * 1.5 - guard_armor, 1 )
guard_health -= magic_damage

guard_attack = round( base_guard_attack * 1.2 - armor, 1 )
health -= guard_attack

print( F'''
=== Магическое противостояние ===

{name} использовал магическую атаку и нанёс стражнику {magic_damage} урона!
Здоровье стражника теперь: {guard_health}
Стражник атаковал героя и нанёс {guard_attack} урона!
Здоровье героя теперь: {health}''' )

copper_coins = int(input())

cooper_weight = 25.6
silver_weight = 16.40
gold_weight = 31.103

total_weight_before = round(copper_coins * cooper_weight, 2)

gold_coins = copper_coins // 336
copper_coins %= 336

silver_coins = copper_coins // 28
copper_coins %= 28
total_weight_after = round(gold_coins * gold_weight + silver_coins * silver_weight + copper_coins * cooper_weight, 2)

print( F'''\
=== Лут ===

Вес до обмена: {total_weight_before}
Золото: {gold_coins}, Серебро: {silver_coins}, Медь: {copper_coins}
Вес после обмена: {total_weight_after}''')

from math import sqrt;

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())

distance = sqrt( (x2-x1) ** 2 + (y2-y1) ** 2 )
distance = round( distance, 2 )

print( F'''\
=== Я свободен! ===

Расстояние между мной ({x1}; {y1}) и ближайшим поселением ({x2}; {y2}) составляет {distance} точек''')

a1, p1, a2, p2, a3, p3 = [int(input()) for _ in 'дорога']
s = [ a1 * p1, a2 * p2, a3 * p3 ]

print( F'''\
=== Травушки-муравушки ===

Ожидаемая прибыль: { max(s) } медяков''' )

надо_золото, надо_серебро, надо_медь = int(input()), int(input()), int(input()) 

хватает = gold_coins >= надо_золото and silver_coins >= надо_серебро and copper_coins >= надо_медь

print( F'''\
=== Дай грош – не отгребёшь ===

Требуемая сумма: Золотые: {надо_золото}, Серебряные: {надо_серебро}, Медные: {надо_медь}
Средств хватает: {хватает}''' )


