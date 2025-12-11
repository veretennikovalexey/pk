class Person:
    setup = ['set_name', 'set_age', 'set_work', 'set_study']


id_1 = Person()
for attribute in id_1.setup:
    setattr(id_1,attribute,input())


# код ниже пожалуйста не удаляйте:
for value in id_1.setup:
    print(getattr(id_1, value))    