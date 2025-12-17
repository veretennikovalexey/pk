class Person:
    Vasya = ''
    Masha = ''
    Lena = ''
    Leonid = ''


names = ['Klementina', 'Roza', 'Balu', 'Lena', 'Leonid']  

for name in names:
    if hasattr(Person, name):
        delattr(Person, name)

print( len(Person.__dict__) )