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
        email = input()
        if not email == self.email:
            print('Ошибка: Такой почты нет в системе!')
            return

        password = input()
        if password == self.password:
            print('Пароль верный. Программа завершена.')
            return

        if not password.lower() == 'забыл пароль':
            print('Ошибка: Пароль неверный!')
            return
            
        secret_word = input()
        if not secret_word == self.secret_word:
            print('Ошибка: Кодовая фраза неверна!')
            return

        pass # Если кодовая фраза совпадает, пока поставьте заглушку pass

'''

Sample Input 4:

ivan@example.com
забыл пароль
Сидорова

Sample Output 4:

Ошибка: Кодовая фраза неверна!

Sample Input 3:

ivan@example.com
qwerty

Sample Output 3:

Ошибка: Пароль неверный!

Sample Input 2:

ivan@example.com
12345

Sample Output 2:

Пароль верный. Программа завершена.

Блин, опять забыл пароль! Часть 3

Sample Input 1:

ivanov@mail.ru

Sample Output 1:

Ошибка: Такой почты нет в системе!

'''

client = Client(
    name="Иван",
    surname="Иванов",
    birth_date="01.01.1990",
    email="ivan@example.com",
    address="Москва, ул. Пушкина, д. 1",
    password="12345",
    secret_word="Петрова"
)
