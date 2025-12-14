list_person = ['hobby', 'work', 'study']

class Person:
    hobby = 'dance'
    work = 'design'
    study = 'college'


id_1 = Person()
for attr in list_person:
    print( getattr(id_1, attr) )

