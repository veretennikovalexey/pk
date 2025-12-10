class Person:
    '''Вася развивает соцсеть'''
    name = "Vasya"


id_1 = Person()
id_1.name = "Lena"
Person.name = "Masha"
print(Person.name)
print(id_1.name)


