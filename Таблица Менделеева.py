# periodic_table.py
import pygame
import sys

pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 1200, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Таблица Менделеева — пример")

# Сетка: 18 колонок (группы), 10 строк (периоды + лантаноиды/актиниды)
COLUMNS = 18
ROWS = 10
MARGIN = 6
cell_w = (WIDTH - MARGIN * (COLUMNS + 1)) // COLUMNS
cell_h = (HEIGHT - MARGIN * (ROWS + 1)) // ROWS

# Цвета по типам элементов (R,G,B)
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

# Элементы: минимальный набор для примера.
# Каждый элемент: (Z, symbol, period, group, type_key, oxidation_string)
# period 1..7 обычные периоды; для лантаноидов и актинидов используем period 8 и 9 и помещаем их в отдельную строку.
elements = [
    (1,  "H", 1, 1,   "nonmetal", "+1 / -1"),
    (2,  "He",1, 18,  "noble", "0"),
    (3,  "Li",2, 1,   "alkali", "+1"),
    (4,  "Be",2, 2,   "alkaline", "+2"),
    (5,  "B", 2, 13,  "metalloid", "+3"),
    (6,  "C", 2, 14,  "nonmetal", "+4 / -4"),
    (7,  "N", 2, 15,  "nonmetal", "-3 / +5"),
    (8,  "O", 2, 16,  "nonmetal", "-2"),
    (9,  "F", 2, 17,  "halogen", "-1"),
    (10, "Ne",2, 18,  "noble", "0"),

    (11, "Na",3, 1,   "alkali", "+1"),
    (12, "Mg",3, 2,   "alkaline", "+2"),
    (13, "Al",3, 13,  "post-transition", "+3"),
    (14, "Si",3, 14,  "metalloid", "+4 / -4"),
    (15, "P", 3, 15,  "nonmetal", "-3 / +5"),
    (16, "S", 3, 16,  "nonmetal", "-2 / +6"),
    (17, "Cl",3, 17,  "halogen", "-1"),
    (18, "Ar",3, 18,  "noble", "0"),

    (19, "K", 4, 1,   "alkali", "+1"),
    (20, "Ca",4, 2,   "alkaline", "+2"),
    (21, "Sc",4, 3,   "transition", "+3"),
    (22, "Ti",4, 4,   "transition", "+4"),
    (23, "V", 4, 5,   "transition", "+5"),
    (24, "Cr",4, 6,   "transition", "+3 / +6"),
    (25, "Mn",4, 7,   "transition", "+2 / +7"),
    (26, "Fe",4, 8,   "transition", "+2 / +3"),
    (27, "Co",4, 9,   "transition", "+2 / +3"),
    (28, "Ni",4,10,   "transition", "+2"),
    (29, "Cu",4,11,   "transition", "+1 / +2"),
    (30, "Zn",4,12,   "transition", "+2"),
    (31, "Ga",4,13,   "post-transition", "+3"),
    (32, "Ge",4,14,   "metalloid", "+4"),
    (33, "As",4,15,   "metalloid", "-3 / +5"),
    (34, "Se",4,16,   "nonmetal", "-2 / +6"),
    (35, "Br",4,17,   "halogen", "-1"),
    (36, "Kr",4,18,   "noble", "0"),

    (37, "Rb",5,1,    "alkali", "+1"),
    (38, "Sr",5,2,    "alkaline", "+2"),
    (39, "Y", 5,3,    "transition", "+3"),
    (40, "Zr",5,4,    "transition", "+4"),
    (41, "Nb",5,5,    "transition", "+5"),
    (42, "Mo",5,6,    "transition", "+6"),
    (43, "Tc",5,7,    "transition", "+7"),
    (44, "Ru",5,8,    "transition", "+3 / +4"),
    (45, "Rh",5,9,    "transition", "+3"),
    (46, "Pd",5,10,   "transition", "+2"),
    (47, "Ag",5,11,   "transition", "+1"),
    (48, "Cd",5,12,   "transition", "+2"),
    (49, "In",5,13,   "post-transition", "+3"),
    (50, "Sn",5,14,   "post-transition", "+2 / +4"),
    (51, "Sb",5,15,   "metalloid", "-3 / +5"),
    (52, "Te",5,16,   "metalloid", "-2 / +6"),
    (53, "I", 5,17,   "halogen", "-1"),
    (54, "Xe",5,18,   "noble", "0"),

    # Блок 6 (частично)
    (55, "Cs",6,1,    "alkali", "+1"),
    (56, "Ba",6,2,    "alkaline", "+2"),
    (57, "La",8,3,    "lanth", "+3"),  # лантаноиды начинаются визуально ниже
    (58, "Ce",8,4,    "lanth", "+3 / +4"),
    (59, "Pr",8,5,    "lanth", "+3"),
    (60, "Nd",8,6,    "lanth", "+3"),
    (61, "Pm",8,7,    "lanth", "+3"),
    (62, "Sm",8,8,    "lanth", "+3"),
    (63, "Eu",8,9,    "lanth", "+2 / +3"),
    (64, "Gd",8,10,   "lanth", "+3"),
    (65, "Tb",8,11,   "lanth", "+3 / +4"),
    (66, "Dy",8,12,   "lanth", "+3"),
    (67, "Ho",8,13,   "lanth", "+3"),
    (68, "Er",8,14,   "lanth", "+3"),
    (69, "Tm",8,15,   "lanth", "+3"),
    (70, "Yb",8,16,   "lanth", "+2 / +3"),
    (71, "Lu",8,17,   "lanth", "+3"),

    (72, "Hf",6,4,    "transition", "+4"),
    (73, "Ta",6,5,    "transition", "+5"),
    (74, "W", 6,6,    "transition", "+6"),
    (75, "Re",6,7,    "transition", "+7"),
    (76, "Os",6,8,    "transition", "+4 / +8"),
    (77, "Ir",6,9,    "transition", "+3 / +4"),
    (78, "Pt",6,10,   "transition", "+2 / +4"),
    (79, "Au",6,11,   "transition", "+1 / +3"),
    (80, "Hg",6,12,   "transition", "+2"),
    (81, "Tl",6,13,   "post-transition", "+1 / +3"),
    (82, "Pb",6,14,   "post-transition", "+2 / +4"),
    (83, "Bi",6,15,   "post-transition", "+3 / +5"),
    (84, "Po",6,16,   "post-transition", "-2 / +4"),
    (85, "At",6,17,   "halogen", "-1"),
    (86, "Rn",6,18,   "noble", "0"),

    # Актиниды (в отдельной строке)
    (87, "Fr",7,1,    "alkali", "+1"),
    (88, "Ra",7,2,    "alkaline", "+2"),
    (89, "Ac",9,3,    "actin", "+3"),
    (90, "Th",9,4,    "actin", "+4"),
    (91, "Pa",9,5,    "actin", "+5"),
    (92, "U", 9,6,    "actin", "+6 / +4 / +5"),
    (93, "Np",9,7,    "actin", "+3 / +5"),
    (94, "Pu",9,8,    "actin", "+3 / +4"),
    (95, "Am",9,9,    "actin", "+3"),
    (96, "Cm",9,10,   "actin", "+3"),
    (97, "Bk",9,11,   "actin", "+3"),
    (98, "Cf",9,12,   "actin", "+3"),
    (99, "Es",9,13,   "actin", "+3"),
    (100,"Fm",9,14,   "actin", "+3"),
    (101,"Md",9,15,   "actin", "+2 / +3"),
    (102,"No",9,16,   "actin", "+2 / +3"),
    (103,"Lr",9,17,   "actin", "+3"),
    # Для сверхтяжёлых элементов можно добавить Z>103 при желании
]

# Преобразуем список в словарь по позиции (row, col) -> элемент
# Визуальная логика:
# period 1..7 отображаются в строках 0..6 (index)
# period 8 (lanth) помещаем в строку 7 (ниже основной таблицы)
# period 9 (actin) в строку 8
# оставим строку 9 пустой/резерв
pos_map = {}
for z, sym, period, group, typ, ox in elements:
    if period <= 7:
        row = period - 1
    elif period == 8:
        row = 7
    elif period == 9:
        row = 8
    else:
        row = 9
    col = group - 1  # группы 1..18 -> колонки 0..17
    pos_map[(row, col)] = {"Z": z, "symbol": sym, "type": typ, "ox": ox}

# Шрифты
base_font_size = min(cell_w, cell_h) // 2  # размер для символа
symbol_font = pygame.font.SysFont(None, base_font_size, bold=True)
ox_font = pygame.font.SysFont(None, max(10, base_font_size // 2))

# Цвет текста
TEXT_COLOR = (10, 10, 10)
Z_COLOR = (80, 80, 80)

clock = pygame.time.Clock()

def draw_cell(r, c, rect, data):
    # фон
    typ = data.get("type", "unknown")
    color = TYPE_COLORS.get(typ, TYPE_COLORS["unknown"])
    pygame.draw.rect(screen, color, rect, border_radius=4)
    pygame.draw.rect(screen, (150,150,150), rect, 1, border_radius=4)

    # символ (большой), по центру с небольшой сдвигом влево, чтобы правее поместилась степень окисления
    symbol = data["symbol"]
    sym_surf = symbol_font.render(symbol, True, TEXT_COLOR)
    sym_rect = sym_surf.get_rect()
    # располагать так: центр клетки, но чуть левее
    sym_rect.centery = rect.centery
    sym_rect.centerx = rect.left + rect.width * 0.45
    screen.blit(sym_surf, sym_rect)

    # степень окисления — справа от символа, в 2 раза меньший шрифт (ox_font)
    ox = data.get("ox", "")
    ox_surf = ox_font.render(ox, True, TEXT_COLOR)
    ox_rect = ox_surf.get_rect()
    # справа от символа, выровнять по центру вертикали
    ox_rect.centery = rect.centery
    ox_rect.left = sym_rect.right + 6
    # если выходит за правый край — сдвинуть влево
    if ox_rect.right > rect.right - 6:
        ox_rect.right = rect.right - 6
    screen.blit(ox_surf, ox_rect)

    # в верхнем левом углу показать порядковый номер (мелко)
    z_surf = ox_font.render(str(data["Z"]), True, Z_COLOR)
    screen.blit(z_surf, (rect.left + 4, rect.top + 2))


def draw_table():
    screen.fill((245, 245, 250))
    for row in range(ROWS):
        for col in range(COLUMNS):
            x = MARGIN + col * (cell_w + MARGIN)
            y = MARGIN + row * (cell_h + MARGIN)
            rect = pygame.Rect(x, y, cell_w, cell_h)
            key = (row, col)
            if key in pos_map:
                draw_cell(row, col, rect, pos_map[key])
            else:
                # пустая ячейка — лёгкий серый фон
                pygame.draw.rect(screen, (240,240,240), rect, border_radius=4)
                pygame.draw.rect(screen, (220,220,220), rect, 1, border_radius=4)

    # подписи для лантаноидов/актинидов (строка под таблицей)
    info_font = pygame.font.SysFont(None, 18)
    lan_txt = info_font.render("Lanthanides (rows shown separately): La – Lu", True, (50,50,50))
    act_txt = info_font.render("Actinides: Ac – Lr", True, (50,50,50))
    screen.blit(lan_txt, (MARGIN, HEIGHT - 36))
    screen.blit(act_txt, (MARGIN, HEIGHT - 18))


# Главный цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    draw_table()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
