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



'''
Урон героя = (Базовый урон героя × 1.5) - Броня стражника
'''

'''
=== Магическое противостояние ===

{name} использовал магическую атаку и нанёс стражнику {magic_damage} урона!
Здоровье стражника теперь: {guard_health}
Стражник атаковал героя и нанёс {guard_attack} урона!
Здоровье героя теперь: {health}
'''

'''
=== Создание героя ===

Имя: Зизифус
Класс: Маг
Здоровье: 85, Броня: 13, Урон: 12.5

=== Магическое противостояние ===

Зизифус использовал магическую атаку и нанёс стражнику 13.8 урона!
Здоровье стражника теперь: 14.2
Стражник атаковал героя и нанёс 5.3 урона!
Здоровье героя теперь: 79.7
'''