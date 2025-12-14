class StreamMode:
    '''Стримерский режим'''
    def __init__(self, telegram, discord, server):
        self.telegram = telegram
        self.discord = discord
        self.server = server

    def hide(self, field_name):

        if field_name == "telegram":
            print("Уведомления Telegram скрыты")
        elif field_name == "discord":
            print("Уведомления Discord скрыты")
        elif field_name == "server":
            print("Название сервера скрыто")
        else:
            print("Такого поля не существует!")
            return

        value = getattr(self, field_name)
        setattr(self, "__" + field_name, value)
        delattr(self, field_name)


telegram, discord, server = input().split()
settings = StreamMode(telegram, discord, server)

fields = input().lower().split()

for field in fields:
    settings.hide(field)