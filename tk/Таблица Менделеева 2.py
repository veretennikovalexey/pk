import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1200, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Таблица Менделеева — пример")

COLUMNS = 18
ROWS = 10
EXTRA_COLS = 1
EXTRA_ROWS = 1
MARGIN = 6

cell_w = (WIDTH - MARGIN * (COLUMNS + EXTRA_COLS + 1)) // (COLUMNS + EXTRA_COLS)
cell_h = (HEIGHT - MARGIN * (ROWS + EXTRA_ROWS + 1)) // (ROWS + EXTRA_ROWS)

TYPE_COLORS = {
    "alkali": (255, 200, 200),
    "alkaline": (255, 230, 180),
    "transition": (200, 220, 255),
    "post-transition": (220, 220, 220),
    "metalloid": (200, 255, 200),
    "nonmetal": (255, 255, 200),
    "halogen": (255, 200, 255),
    "noble": (200, 255, 255),
    "lanth": (240, 220, 255),
    "actin": (240, 200, 230),
    "unknown": (220, 220, 240),
}

elements = [
]

pos_map = {}
for z,s,p,g,t,o in elements:
    r = p - 1 + 1
    c = g - 1 + 1
    pos_map[(r,c)] = {"Z":z,"symbol":s,"type":t,"ox":o}

symbol_font = pygame.font.SysFont("verdana",22)
ox_font = pygame.font.SysFont("verdana",10)
label_font = pygame.font.SysFont("verdana",16)

roman = ["I","II","III","IV","V","VI","VII"]

clock = pygame.time.Clock()

def draw_cell(rect,data):
    pygame.draw.rect(screen,TYPE_COLORS[data["type"]],rect,4)
    pygame.draw.rect(screen,(150,150,150),rect,1,4)
    s = symbol_font.render(data["symbol"],True,(10,10,10))
    sr = s.get_rect(center=rect.center)
    screen.blit(s,sr)
    ox = ox_font.render(data["ox"],True,(10,10,10))
    screen.blit(ox,(sr.centerx-ox.get_width()//2,sr.bottom))
    z = ox_font.render(str(data["Z"]),True,(80,80,80))
    screen.blit(z,(rect.left+4,rect.top+2))

def draw_table():
    screen.fill((245,245,250))
    for r in range(ROWS + EXTRA_ROWS):
        for c in range(COLUMNS + EXTRA_COLS):
            x = MARGIN + c * (cell_w + MARGIN)
            y = MARGIN + r * (cell_h + MARGIN)
            rect = pygame.Rect(x,y,cell_w,cell_h)
            if r == 0 and c > 0:
                t = label_font.render(str(c),True,(0,0,0))
                screen.blit(t,(rect.centerx - t.get_width()//2,rect.centery - t.get_height()//2))
            elif c == 0 and 1 <= r <= 7:
                t = label_font.render(roman[r-1],True,(0,0,0))
                screen.blit(t,(rect.centerx - t.get_width()//2,rect.centery - t.get_height()//2))
            elif (r,c) in pos_map:
                draw_cell(rect,pos_map[(r,c)])
            else:
                pygame.draw.rect(screen,(240,240,240),rect,4)
                pygame.draw.rect(screen,(220,220,220),rect,1,4)

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
            running = False
    draw_table()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
