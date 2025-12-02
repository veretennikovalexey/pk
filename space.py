import pygame
import random
import math
import sys

pygame.init()

info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Расширенная Галактика")

clock = pygame.time.Clock()

# -----------------------------
# ЗВЁЗДЫ (разные размеры + мерцание)
# -----------------------------
STAR_COUNT = 350
stars = []
for _ in range(STAR_COUNT):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    size = random.randint(1, 3)
    phase = random.uniform(0, math.pi * 2)
    speed = random.uniform(0.5, 1.5)
    stars.append([x, y, size, phase, speed])

# -----------------------------
# СОЛНЦЕ
# -----------------------------
sun_pos = (WIDTH // 2, HEIGHT // 2)
SUN_RADIUS = 60
SUN_COLOR = (255, 220, 40)

# -----------------------------
# ПЛАНЕТЫ (эллипсы!)
# orbit_x — горизонтальный радиус
# orbit_y — вертикальный радиус (меньше)
# -----------------------------
planets = [
    ("Mercury", 100, 60, 6, 2.0, (200, 200, 200)),
    ("Venus",   150, 90, 10, 1.6, (255, 200, 80)),
    ("Earth",   200, 120, 12, 1.0, (80, 150, 255)),
    ("Mars",    250, 150, 10, 0.8, (255, 120, 80)),
    ("Jupiter", 340, 210, 26, 0.45, (230, 180, 140)),
    ("Saturn",  420, 260, 22, 0.35, (240, 210, 150)),
    ("Uranus",  500, 300, 16, 0.25, (170, 230, 255)),
    ("Neptune", 580, 340, 15, 0.20, (90, 140, 255)),
    ("Pluto",   650, 380,  6, 0.15, (200, 180, 160))
]

planet_states = []
for p in planets:
    planet_states.append({
        "name": p[0],
        "ox": p[1],
        "oy": p[2],
        "radius": p[3],
        "speed": p[4],
        "color": p[5],
        "angle": random.random() * math.pi * 2
    })

# -----------------------------
# НЛО
# -----------------------------
ufo_x = -200
ufo_y = HEIGHT // 3
ufo_speed = 180
ufo_timer = 0
next_ufo_time = random.randint(5, 12)

# -----------------------------
# Кометы
# -----------------------------
comets = []
COMET_SPAWN_TIME = 4
comet_timer = 0

def spawn_comet():
    y = random.randint(0, HEIGHT // 2)
    speed = random.uniform(220, 300)
    tail = []
    return {"x": -100, "y": y, "speed": speed, "tail": tail}

# -----------------------------
# Функция мягкого освещения планеты
# -----------------------------
def draw_planet_with_light(x, y, radius, base_color):
    for r in range(radius, 0, -1):
        t = r / radius
        lit = (
            min(255, int(base_color[0] + 80 * (1 - t))),
            min(255, int(base_color[1] + 80 * (1 - t))),
            min(255, int(base_color[2] + 80 * (1 - t)))
        )
        pygame.draw.circle(screen, lit, (int(x), int(y)), r)

# -----------------------------
# Основной цикл
# -----------------------------
running = True
while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_ESCAPE, pygame.K_q):
                running = False

    # -----------------------------
    # ЗВЁЗДЫ
    # -----------------------------
    screen.fill((0, 0, 0))
    for s in stars:
        x, y, size, phase, speed = s
        phase += speed * dt
        s[3] = phase
        brightness = 150 + int((math.sin(phase) + 1) * 50)
        pygame.draw.circle(screen, (brightness, brightness, brightness), (x, y), size)

    # -----------------------------
    # СОЛНЦЕ
    # -----------------------------
    pygame.draw.circle(screen, SUN_COLOR, sun_pos, SUN_RADIUS)

    # -----------------------------
    # ПЛАНЕТЫ на эллиптических орбитах
    # -----------------------------
    for p in planet_states:
        p["angle"] += p["speed"] * dt

        x = sun_pos[0] + p["ox"] * math.cos(p["angle"])
        y = sun_pos[1] + p["oy"] * math.sin(p["angle"])

        if p["name"] == "Saturn":
            pygame.draw.ellipse(
                screen, (180, 160, 120),
                (x - p["radius"] * 1.6, y - p["radius"] * 0.6, p["radius"] * 3.2, p["radius"] * 1.2),
                3
            )

        draw_planet_with_light(x, y, p["radius"], p["color"])

    # -----------------------------
    # КОМЕТЫ
    # -----------------------------
    comet_timer += dt
    if comet_timer >= COMET_SPAWN_TIME:
        comet_timer = 0
        comets.append(spawn_comet())

    for c in comets:
        c["x"] += c["speed"] * dt
        c["y"] += math.sin(c["x"] * 0.01) * 1.5
        c["tail"].append((c["x"], c["y"]))

        if len(c["tail"]) > 40:
            c["tail"].pop(0)

        for i, (tx, ty) in enumerate(c["tail"]):
            alpha = i * 6
            color = (255, 255 - alpha, 255 - alpha)
            pygame.draw.circle(screen, color, (int(tx), int(ty)), 3)

    comets = [c for c in comets if c["x"] < WIDTH + 200]

    # -----------------------------
    # НЛО
    # -----------------------------
    ufo_timer += dt
    if ufo_timer >= next_ufo_time:
        ufo_x = -200
        ufo_y = random.randint(50, HEIGHT - 50)
        ufo_timer = 0
        next_ufo_time = random.randint(5, 12)

    if ufo_x < WIDTH + 200:
        ufo_x += ufo_speed * dt
        ufo_y += math.sin(pygame.time.get_ticks() * 0.002) * 0.7
        pygame.draw.ellipse(screen, (120, 255, 120),
                            (ufo_x, ufo_y, 60, 25))

    pygame.display.flip()

pygame.quit()
sys.exit()
