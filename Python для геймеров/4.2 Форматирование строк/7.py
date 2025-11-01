player = input()
level = int( input() )
score = int( input() )
location = input()
items = input()
health = input()

print( 'Сохранение игрового прогресса в формате JSON:' )
print( '{' )
print( f'\t"player": "{player}",' )
print( f'\t"level": {level},' )
print( f'\t"score": {score},' )
print( f'\t"location": "{location}",' )
print( f'\t"items": "{items}",' )
print( f'\t"health": "{health}"' )
print( '}' )


'''
Сохранение игрового прогресса в формате JSON:
{
	"player": "<имя игрока>",
	"level": <уровень>,
	"score": <очки>,
	"location": "<местоположение>",
	"items": "<предмет1>, <предмет2>, ...",
	"health": "<текущее здоровье> из <максимальное здоровье>"
}
'''
