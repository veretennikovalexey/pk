class Client:
    def __init__(self, name, surname, birth_date, email, address, password, secret_word):
        self.name = name       
        self.surname = surname
        self.birth_date = birth_date
        self.email = email
        self.address = address
        self.__password = password
        self.__secret_word = secret_word

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