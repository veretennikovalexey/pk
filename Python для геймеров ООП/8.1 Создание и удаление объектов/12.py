class GameSettings:
    ''' Настройки игры '''
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.volume = 100
        self.difficulty = "Normal"
        self.resolution = "1920x1080"        