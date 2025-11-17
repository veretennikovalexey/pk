class Person:
    def __init__(self, name, last_name, age, sex, hobby, photos):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.hobby = hobby
        self.photos = photos

    def isprivate(self, field):
        private_map = {
            "имя": ("name", "__name", "Ваше имя скрыто!"),
            "фамилия": ("last_name", "__last_name", "Ваша фамилия скрыта!"),
            "возраст": ("age", "__age", "Ваш возраст больше никому не виден!"),
            "пол": ("sex", "__sex", "Ваш пол не опознан!"),
            "хобби": ("hobby", "__hobby", "Ваше хобби скрыто!"),
            "фото": ("photos", "__photos", "Ваши фотографии больше никто не увидит:)")
        }

        if field in private_map:
            public_attr, private_attr, message = private_map[field]
            setattr(self, private_attr, getattr(self, public_attr))
            delattr(self, public_attr)
            print(message)
        else:
            print("Такого поля не существует!")


data = input().split()
fields = input().lower().split()

my_person = Person( *data )

for field in fields:
    my_person.isprivate( field )
