class User:
    def __init__(self, last_name, name, date_of_birth):
        self.__last_name = last_name    
        self.__name = name    
        self.__date_of_birth = date_of_birth    

last_name, name, date_of_birth = input().split()
user = User( last_name, name, date_of_birth )

# from datetime import datetime
# <Фамилия> <Имя> <Дата_рождения>
# date_of_birth = datetime.strptime(date_of_birth, "%d.%m.%Y").date()