import pygame
import random
import sys
from collections import deque

GRID_W, GRID_H = 10, 10
CELL = 50
BOMBS_COUNT = 10
WIDTH, HEIGHT = GRID_W * CELL, GRID_H * CELL
FPS = 30

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
DARK_GRAY = (160, 160, 160)
BLACK = (0, 0, 0)
GREEN = (0, 180, 0)
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
pygame.display.set_caption("Мини-сапёр 10x10")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, CELL // 2)

grid = [[0 for _ in range(GRID_W)] for __ in range(GRID_H)]
revealed = [[False for _ in range(GRID_W)] for __ in range(GRID_H)]
flagged = [[False for _ in range(GRID_W)] for __ in range(GRID_H)]
lost = False
won = False


def place_bombs():
    coords = [(x, y) for x in range(GRID_W) for y in range(GRID_H)]
    bombs = random.sample(coords, BOMBS_COUNT)
    for x, y in bombs:
        grid[y][x] = -1
    for y in range(GRID_H):
        for x in range(GRID_W):
            if grid[y][x] == -1:
                continue
            c = 0
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < GRID_W and 0 <= ny < GRID_H and grid[ny][nx] == -1:
                        c += 1
            grid[y][x] = c


def draw_bomb(surface, cx, cy):
    cx_pix = cx * CELL + CELL // 2
    cy_pix = cy * CELL + CELL // 2
    radius = CELL // 3
    pygame.draw.circle(surface, BLACK, (cx_pix, cy_pix), radius)
    tail_len = 6
    for i in range(8):
        angle = (2 * 3.14159265 / 8) * i
        v = pygame.math.Vector2(1, 0).rotate_rad(angle)
        sx = cx_pix + int((radius - 1) * v.x)
        sy = cy_pix + int((radius - 1) * v.y)
        ex = cx_pix + int((radius + tail_len) * v.x)
        ey = cy_pix + int((radius + tail_len) * v.y)
        pygame.draw.line(surface, BLACK, (sx, sy), (ex, ey), 2)


def draw_flag(surface, cx, cy):
    x0 = cx * CELL
    y0 = cy * CELL
    cxm = x0 + CELL // 2
    y_base = y0 + CELL // 2 + 8

    pygame.draw.line(surface, BLACK, (cxm, y_base - 15), (cxm, y_base), 3)

    tip = (cxm, y_base - 15)
    left = (cxm - 12, y_base - 8)
    right = (cxm + 3, y_base - 12)
    pygame.draw.polygon(surface, GREEN, [tip, left, right])


def reveal_tile(x, y):
    global lost, won
    if revealed[y][x] or flagged[y][x] or lost or won:
        return

    revealed[y][x] = True

    if grid[y][x] == -1:
        lost = True
        return

    if grid[y][x] == 0:
        q = deque()
        q.append((x, y))
        while q:
            cx, cy = q.popleft()
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < GRID_W and 0 <= ny < GRID_H:
                        if not revealed[ny][nx] and not flagged[ny][nx]:
                            revealed[ny][nx] = True
                            if grid[ny][nx] == 0:
                                q.append((nx, ny))

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
            r = pygame.Rect(x * CELL, y * CELL, CELL, CELL)

            if revealed[y][x]:
                pygame.draw.rect(screen, DARK_GRAY, r)
            else:
                pygame.draw.rect(screen, WHITE, r)

            pygame.draw.rect(screen, BLACK, r, 1)

            if revealed[y][x]:
                if grid[y][x] == -1:
                    draw_bomb(screen, x, y)
                elif grid[y][x] > 0:
                    t = font.render(str(grid[y][x]), True, NUMBER_COLORS[grid[y][x]])
                    screen.blit(t, t.get_rect(center=r.center))
            else:
                if flagged[y][x]:
                    draw_flag(screen, x, y)

    if lost:
        for y in range(GRID_H):
            for x in range(GRID_W):
                if grid[y][x] == -1:
                    draw_bomb(screen, x, y)
        t = font.render("Ты проиграл — Esc", True, RED)
        screen.blit(t, (10, HEIGHT - 30))

    if won:
        t = font.render("Победа! — Esc", True, GREEN)
        screen.blit(t, (10, HEIGHT - 30))


def get_cell(pos):
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
            elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                running = False
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                cell = get_cell(ev.pos)
                if not cell:
                    continue
                x, y = cell

                if ev.button == 1:  
                    if not flagged[y][x]:
                        reveal_tile(x, y)

                if ev.button == 3:  
                    if not revealed[y][x] and not lost and not won:
                        flagged[y][x] = not flagged[y][x]

        draw()
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
