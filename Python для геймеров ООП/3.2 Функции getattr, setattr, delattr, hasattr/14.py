class Controls:
    '''Настройки горячих клавиш'''
    def __init__(self):
        self.mic_on = "F4"
        self.mute_sound = "F5"
        self.push_to_talk = "V"
        self.deafen = "F6"

    def set_key(self, action, key):
        if hasattr(self, action):
            setattr(self, action, key)

    def get_key(self, action):
        return getattr(self, action, "нет такого действия")            