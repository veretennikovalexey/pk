class Client:
    def __init__(self, name, surname, birth_day, email, address, password, secret_word):
        self.__secret_word = secret_word
        self.__password = password
        self.birth_day = birth_day
        self.address = address
        self.surname = surname
        self.email = email
        self.name = name       

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

print(client.name, client.surname, client.email)    