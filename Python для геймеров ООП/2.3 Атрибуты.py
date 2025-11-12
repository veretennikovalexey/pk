class Hero:
    def __init__(self, name, hp, dmg):
        self.name, self.hp, self.dmg = name, hp, dmg
        print(f'Герой {name}\n❤️: {hp}\n⚔️: {dmg}')

        
def parse(_):
    name, hp, dmg = _.split()
    return [name, int(hp), int(dmg)]    


def strike(striker, blocker):
    print( f'{striker.name} наносит удар!' )
    blocker.hp -= striker.dmg
    print( f'У {blocker.name} осталось ❤️ {blocker.hp}' )
    if blocker.hp <= 0:
        print( f'Победил {striker.name}' ) 
        return True
    return False
    
striker, blocker = Hero( *parse( input() ) ), Hero( *parse( input() ) )

while True:
    if strike(striker, blocker):
        break
    striker, blocker = blocker, striker