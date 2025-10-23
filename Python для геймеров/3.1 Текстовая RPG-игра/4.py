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

'''
Sample Input:

1037
Sample Output:

=== Лут ===

Вес до обмена: 26547.2
Золото: 3, Серебро: 1, Медь: 1
Вес после обмена: 135.31
'''