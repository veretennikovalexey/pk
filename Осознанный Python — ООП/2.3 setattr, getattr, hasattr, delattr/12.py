# delattr(object, name)

class Person:
    pass

id_1 = Person()

setattr(id_1, "name", "Vasya")
print(hasattr(id_1, "name"))  # True

delattr(id_1, "name")
print(hasattr(id_1, "name"))  # False