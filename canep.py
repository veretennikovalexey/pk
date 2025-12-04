# minesweeper.py
import pygame
import random
import sys
from collections import deque

# Настройки
GRID_W, GRID_H = 10, 10
CELL = 50                # размер клетки в пикселях
BOMBS_COUNT = 10
WIDTH, HEIGHT = GRID_W * CELL, GRID_H * CELL
FPS = 30

# Цвета (RGB)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
DARK_GRAY = (160, 160, 160)
BLACK = (0, 0, 0)
GREEN = (0, 150, 0)
RED = (200, 0, 0)
NUMBER_COLORS = {
    1: (25, 25, 200),
    2: (25, 150, 25),
    3: (200, 25, 25),
    4: (20, 100, 200),
    5: (150, 20, 20),
    6: (20, 150, 150),
    7: (100, 20, 100),
    8: (80, 80, 80),
}

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Мини-сапер 10x10")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, CELL // 2)

# Игровые структуры
# grid: 0..8 - количество бомб вокруг; -1 - бомба
grid = [[0 for _ in range(GRID_W)] for __ in range(GRID_H)]
revealed = [[False for _ in range(GRID_W)] for __ in range(GRID_H)]
lost = False
won = False

def place_bombs():
    coords = [(x, y) for x in range(GRID_W) for y in range(GRID_H)]
    bombs = random.sample(coords, BOMBS_COUNT)
    for bx, by in bombs:
        grid[by][bx] = -1
    # заполним числа
    for y in range(GRID_H):
        for x in range(GRID_W):
            if grid[y][x] == -1:
                continue
            count = 0
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    nx, ny = x + dx, y + dy
                    if dx == 0 and dy == 0:
                        continue
                    if 0 <= nx < GRID_W and 0 <= ny < GRID_H and grid[ny][nx] == -1:
                        count += 1
            grid[y][x] = count

def draw_bomb(surface, cell_x, cell_y):
    # Рисуем полностью закрашенную чёрную окружность и 8 хвостов (очень коротких), чтобы не выходили за клетку
    cx = cell_x * CELL + CELL // 2
    cy = cell_y * CELL + CELL // 2
    # радиус круга
    radius = CELL // 3
    pygame.draw.circle(surface, BLACK, (cx, cy), radius)
    # хвосты — 8 маленьких линий от окружности наружу, длина в пару пикселей
    tail_len = 6  # пара пикселей
    for i in range(8):
        angle = (2 * 3.14159265 / 8) * i
        sx = cx + int((radius - 1) * pygame.math.Vector2(1, 0).rotate_rad(angle).x)
        sy = cy + int((radius - 1) * pygame.math.Vector2(1, 0).rotate_rad(angle).y)
        ex = cx + int((radius + tail_len) * pygame.math.Vector2(1, 0).rotate_rad(angle).x)
        ey = cy + int((radius + tail_len) * pygame.math.Vector2(1, 0).rotate_rad(angle).y)
        pygame.draw.line(surface, BLACK, (sx, sy), (ex, ey), 2)

def reveal_tile(x, y):
    global lost, won
    if revealed[y][x] or lost or won:
        return
    revealed[y][x] = True
    if grid[y][x] == -1:
        lost = True
        return
    # Если у клетки 0 соседних бомб — рекурсивно (через очередь) открываем соседей
    if grid[y][x] == 0:
        q = deque()
        q.append((x, y))
        while q:
            cx, cy = q.popleft()
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < GRID_W and 0 <= ny < GRID_H and not revealed[ny][nx]:
                        revealed[ny][nx] = True
                        if grid[ny][nx] == 0:
                            q.append((nx, ny))
    # Проверка победы: все не-бомбы открыты
    all_open = True
    for yy in range(GRID_H):
        for xx in range(GRID_W):
            if grid[yy][xx] != -1 and not revealed[yy][xx]:
                all_open = False
                break
        if not all_open:
            break
    if all_open:
        won = True

def draw():
    screen.fill(GRAY)
    for y in range(GRID_H):
        for x in range(GRID_W):
            rect = pygame.Rect(x * CELL, y * CELL, CELL, CELL)
            # фон клетки
            if revealed[y][x]:
                pygame.draw.rect(screen, DARK_GRAY, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)
            # рамка
            pygame.draw.rect(screen, BLACK, rect, 1)

            if revealed[y][x]:
                if grid[y][x] == -1:
                    # бомба
                    draw_bomb(screen, x, y)
                elif grid[y][x] > 0:
                    num = grid[y][x]
                    txt = font.render(str(num), True, NUMBER_COLORS.get(num, BLACK))
                    txt_rect = txt.get_rect(center=rect.center)
                    screen.blit(txt, txt_rect)
                # если 0 — просто тёмная клетка уже нарисована
            else:
                # не открыта
                pass

    # Если проигрыш — показать все бомбы (включая НЕ открытые)
    if lost:
        for y in range(GRID_H):
            for x in range(GRID_W):
                if grid[y][x] == -1 and not revealed[y][x]:
                    draw_bomb(screen, x, y)
        # подпись
        lose_txt = font.render("Ты проиграл! Нажми Esc или закрой окно.", True, RED)
        screen.blit(lose_txt, (10, HEIGHT - 30))
    if won:
        win_txt = font.render("Победа! Нажми Esc или закрой окно.", True, GREEN)
        screen.blit(win_txt, (10, HEIGHT - 30))

def get_cell_from_pos(pos):
    mx, my = pos
    x = mx // CELL
    y = my // CELL
    if 0 <= x < GRID_W and 0 <= y < GRID_H:
        return x, y
    return None

def main():
    place_bombs()
    running = True
    while running:
        clock.tick(FPS)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    running = False
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                if ev.button == 1 and not lost and not won:  # левый клик
                    cell = get_cell_from_pos(ev.pos)
                    if cell:
                        x, y = cell
                        if not revealed[y][x]:
                            reveal_tile(x, y)

        draw()
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
