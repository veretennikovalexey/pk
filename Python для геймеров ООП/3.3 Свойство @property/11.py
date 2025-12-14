class Client:
    def __init__(self, name, surname, birth_date, email, address, password, secret_word):
        self.name = name       
        self.surname = surname
        self.birth_date = birth_date
        self.email = email
        self.address = address
        self.__password = password
        self.__secret_word = secret_word

    @property
    def password(self):
        '''Возвращает текущий пароль'''
        return self.__password

    @password.setter
    def password(self, value):
        '''Позволяет изменить пароль'''
        self.__password = value

    @property     
    def secret_word(self):
        '''Возвращает кодовую фразу (без возможности изменения)'''
        return self.__secret_word            

    def change_password(self):
        pass    

client = Client(
    name="Иван",
    surname="Иванов",
    birth_date="01.01.1990",
    email="ivan@example.com",
    address="Москва, ул. Пушкина, д. 1",
    password="12345",
    secret_word="Петрова"
)

print(client.password)
client.password = "54321"
print(client.password)
print(client.secret_word) 