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

        passone = 'b'
        passtwo = 'd'

        while not passone == passtwo:
            passone = input()
            passtwo = input()
            if not passone == passtwo:
                print('Пароли не совпадают! Введите ещё раз!')

        print('Отлично! Ваш пароль сохранён!')
        self.password = passone

name = input()
surname = input()
birth_date = input()
email = input()
address = input()
password = input()
secret_word = input()

client = Client(name, surname, birth_date, email, address, password, secret_word)  
client.change_password()      