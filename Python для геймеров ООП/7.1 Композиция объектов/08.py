class SmokeAnimation:
    def __init__(self):
        print('Аллилуйя!')

    def play(self):
        print('Дым клубится вокруг гранаты...')     


class HolyHandGrenade:
    def __init__(self, delay):
        self.delay = delay
        self.smoke = SmokeAnimation()

    def explode(self):
        print(f'Святая граната тикает... {self.delay} сек.')            
        self.smoke.play()
        print('💥 БА-БАХ! Огромная воронка остаётся после взрыва!')