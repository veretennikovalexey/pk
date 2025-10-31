print('=== Создание героя ===\n')
hero_name = input()  # Герой имя (строка)
print('Имя: ' + hero_name)
hero_class = input() # Герой класс (строка)
print('Класс: ' + hero_class)
hero_health = int(input())   # Герой здоровье (целое число)
hero_armor  = int(input())   # Герой броня    (целое число)
hero_damage = float(input()) # Герой базовый урон (дробное число)
print(f'Здоровье: {hero_health}, Броня: {hero_armor}, Урон: {hero_damage}')

print('\n=== Магическое противостояние ===\n')
guard_health = int(input())       # Стражник здоровье (целое число)
guard_armor  = int(input())       # Стражник броня    (целое число)
base_guard_attack= float(input()) # Стражник базовый урон (дробное число)

magic_damage = round( hero_damage * 1.5 - guard_armor, 1 )
print(f'{hero_name} использовал магическую атаку и нанёс стражнику {magic_damage} урона!')
guard_health -= magic_damage
print(f'Здоровье стражника теперь: {guard_health}')
guard_attack = round( base_guard_attack * 1.2 - hero_armor, 1 )
print(f'Стражник атаковал героя и нанёс {guard_armor} урона!')
hero_health -= guard_attack
print(f'Здоровье героя теперь: {hero_health}')

print('\n=== Лут ===\n')
copper_coins = int(input()) # Монеты медные (натуральное число)


def wei(gold, silver, cooper): # вес монет
    COOPER_WEIGHT = 25.6
    SILVER_WEIGHT = 16.40
    GOLD_WEIGHT = 31.103
    total_weight = round(gold * GOLD_WEIGHT +
                         silver * SILVER_WEIGHT +
                         cooper * COOPER_WEIGHT, 2)    
    return total_weight


print(f'Вес до обмена: {wei(0,0,copper_coins)}')

gold_coins = copper_coins // 336
copper_coins %= 336
silver_coins = copper_coins // 28
copper_coins %= 28

print(f'Золото: {gold_coins}, Серебро: {silver_coins}, Медь: {copper_coins}')
print(f'Вес после обмена: {wei(gold_coins,silver_coins,copper_coins)}')

print('\n=== Я свободен! ===\n')

x1 = float(input()) # Герой 
y1 = float(input()) # Герой
x2 = float(input()) # Поселение
y2 = float(input()) # Поселение
distance = ( (x2-x1) ** 2 + (y2-y1) ** 2 ) ** 0.5
distance = round( distance, 2 )
print(f'Расстояние между мной ({x1}; {y1}) и ближайшим поселением ({x2}; {y2}) составляет {distance} точек')

print('\n=== Травушки-муравушки ===\n')
grass1_amnt = int(input()) # Трава 1 количество
grass1_cost = int(input()) # Трава 1 цена
grass2_amnt = int(input()) # Трава 2 количество 
grass2_cost = int(input()) # Трава 2 цена 
grass3_amnt = int(input()) # Трава 3 количество  
grass3_cost = int(input()) # Трава 3 цена 

profit = [ grass1_amnt * grass1_cost, 
           grass2_amnt * grass2_cost,
           grass3_amnt * grass3_cost ]

print(f'Ожидаемая прибыль: { max(profit) } медяков')

print('\n=== Дай грош – не отгребёшь ===\n')

payment_gold   = int(input()) # Плата за вход в город золото 
payment_silver = int(input()) # Плата за вход в город серебро 
payment_copper = int(input()) # Плата за вход в город медь
print(f'Требуемая сумма: Золотые: {payment_gold}, Серебряные: {payment_silver}, Медные: {payment_copper}')

can_enter = gold_coins >= payment_gold and silver_coins >= payment_silver and copper_coins >= payment_copper
print(f'Средств хватает: {can_enter}')

print('\n=== Итог приключения ===\n')
hero_name = input() # Герой новое имя (строка)  
print('Новое имя героя: ' + hero_name)
print(f'Оставшееся здоровье: {hero_health}')

gold_coins -= payment_gold
silver_coins -= payment_silver
copper_coins -= payment_copper
copper_coins += max(profit) # продали травы 150 монет
gold_coins += copper_coins // 336
copper_coins %= 336
silver_coins += copper_coins // 28
copper_coins %= 28

print(f'Золотые: {gold_coins}, Серебряные: {silver_coins}, Медные: {copper_coins}')
print(f'Общий вес инвентаря: {wei(gold_coins,silver_coins,copper_coins)} единиц')