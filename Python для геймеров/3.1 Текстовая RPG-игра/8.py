name       = input()    # Герой имя   (строка)
hero_class = input()    # Герой класс (строка)
health = int(input())   # Герой здоровье (целое число)
armor  = int(input())   # Герой броня    (целое число)
damage = float(input()) # Герой базовый урон (дробное число)

print( F'''\
=== Создание героя ===

Имя: {name}
Класс: {hero_class}
Здоровье: {health}, Броня: {armor}, Урон: {damage}\n''' )

guard_health = int(input())       # Стражник здоровье (целое число)
guard_armor  = int(input())       # Стражник броня    (целое число)
base_guard_attack= float(input()) # Стражник базовый урон (дробное число)

copper_coins = int(input()) # Монеты медные (натуральное число)

x1 = float(input()) # Герой 
y1 = float(input()) # Герой
x2 = float(input()) # Поселение
y2 = float(input()) # Поселение

grass1_amnt = int(input()) # Трава 1 количество
grass1_cost = int(input()) # Трава 1 цена
grass2_amnt = int(input()) # Трава 2 количество 
grass2_cost = int(input()) # Трава 2 цена 
grass3_amnt = int(input()) # Трава 3 количество  
grass3_cost = int(input()) # Трава 3 цена 

payment_gold   = int(input()) # Плата за вход в город золото 
payment_silver = int(input()) # Плата за вход в город серебро 
payment_copper = int(input()) # Плата за вход в город медь

can_enter = False

new_name = input() # Герой новое имя (строка)

magic_damage = round( damage * 1.5 - guard_armor, 1 )
guard_health -= magic_damage

guard_attack = round( base_guard_attack * 1.2 - armor, 1 )
health -= guard_attack

COOPER_WEIGHT = 25.6
SILVER_WEIGHT = 16.40
GOLD_WEIGHT = 31.103

total_weight_before = round(copper_coins * COOPER_WEIGHT, 2)

gold_coins = copper_coins // 336
copper_coins %= 336

silver_coins = copper_coins // 28
copper_coins %= 28

total_weight_after = round(gold_coins * GOLD_WEIGHT + silver_coins * SILVER_WEIGHT + copper_coins * COOPER_WEIGHT, 2)

distance = ( (x2-x1) ** 2 + (y2-y1) ** 2 ) ** 0.5
distance = round( distance, 2 )

profit = [ grass1_amnt * grass1_cost, 
           grass2_amnt * grass2_cost,
           grass3_amnt * grass3_cost ]

can_enter = gold_coins >= payment_gold and silver_coins >= payment_silver and copper_coins >= payment_copper

gold = gold_coins - payment_gold
silver = silver_coins - payment_silver
copper = copper_coins - payment_copper
copper += max(profit) # продали травы 150 монет
gold += copper // 336
copper %= 336
silver += copper // 28
copper %= 28

total_weight = round(gold * GOLD_WEIGHT + silver * SILVER_WEIGHT + copper * COOPER_WEIGHT, 2)

print( F'''\
=== Магическое противостояние ===

{name} использовал магическую атаку и нанёс стражнику {magic_damage} урона!
Здоровье стражника теперь: {guard_health}
Стражник атаковал героя и нанёс {guard_attack} урона!
Здоровье героя теперь: {health}

=== Лут ===

Вес до обмена: {total_weight_before}
Золото: {gold_coins}, Серебро: {silver_coins}, Медь: {copper_coins}
Вес после обмена: {total_weight_after}

=== Я свободен! ===

Расстояние между мной ({x1}; {y1}) и ближайшим поселением ({x2}; {y2}) составляет {distance} точек

=== Травушки-муравушки ===

Ожидаемая прибыль: { max(profit) } медяков

=== Дай грош – не отгребёшь ===

Требуемая сумма: Золотые: {payment_gold}, Серебряные: {payment_silver}, Медные: {payment_copper}
Средств хватает: {can_enter}

=== Итог приключения ===

Новое имя героя: {new_name}
Оставшееся здоровье: {health}
Золотые: {gold}, Серебряные: {silver}, Медные: {copper}
Общий вес инвентаря: {total_weight} единиц''' )

