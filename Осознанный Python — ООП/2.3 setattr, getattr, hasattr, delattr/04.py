class Person:
    '''setattr()'''
    pass


id_1 = Person()
setattr(id_1, "name", "Vasya")
setattr(id_1, "name", "Masha")
name = getattr(id_1, "name")
print(name)
