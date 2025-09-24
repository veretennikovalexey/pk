text = input()
# text = "Привет, как дела?!"
sum = len( text ) * 60
print(f'''\
{ sum // 100 } р. { sum % 100 } коп.''')

# print(f'{sum = }')

'''
10 р. 80 коп.
'''