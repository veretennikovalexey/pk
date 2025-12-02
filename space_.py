import pygame
import random
import math
import sys

pygame.init()
# Получаем размер экрана
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Солнечная система — демонстрация")

clock = pygame.time.Clock()

# Звёзды
STAR_COUNT = 300
stars = [(random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)) for _ in range(STAR_COUNT)]

# Солнце (в точном центре)
sun_pos = (WIDTH // 2, HEIGHT // 2)
SUN_RADIUS = 60

# Орбита Земли (чётко круговая)
earth_orbit_radius = min(WIDTH, HEIGHT) * 0.28  # радиус орбиты Земли
EARTH_RADIUS = 18
earth_angle = 0.0
earth_angular_speed = 0.8  # радианы в секунду

# Луна вокруг Земли
moon_orbit_radius = 48
MOON_RADIUS = 6
moon_angle = 0.0
moon_angular_speed = 3.0  # быстрее Земли

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 210, 0)
BLUE = (95, 170, 255)

running = True
while running:
    dt = clock.tick(60) / 1000.0  # секунды, ограничение 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Выход по Escape или по нажатию клавиши Q
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                running = False

    # Обновление углов — это даёт круговые орбиты
    earth_angle += earth_angular_speed * dt
    moon_angle += moon_angular_speed * dt

    # Позиция Земли по круговой орбите вокруг Солнца
    earth_x = sun_pos[0] + earth_orbit_radius * math.cos(earth_angle)
    earth_y = sun_pos[1] + earth_orbit_radius * math.sin(earth_angle)

    # Позиция Луны по круговой орбите вокруг Земли
    moon_x = earth_x + moon_orbit_radius * math.cos(moon_angle)
    moon_y = earth_y + moon_orbit_radius * math.sin(moon_angle)

    # Рисуем сцену
    screen.fill(BLACK)

    # Звёзды
    for sx, sy in stars:
        screen.set_at((sx, sy), WHITE)  # просто белая точка

    # Солнце (точно в центре)
    pygame.draw.circle(screen, YELLOW, sun_pos, SUN_RADIUS)

    # Орбита Земли (опционально рисовать контур орбиты — можно закомментировать)
    # pygame.draw.circle(screen, (40,40,40), sun_pos, int(earth_orbit_radius), 1)

    # Земля
    pygame.draw.circle(screen, BLUE, (int(earth_x), int(earth_y)), EARTH_RADIUS)

    # Луна
    pygame.draw.circle(screen, WHITE, (int(moon_x), int(moon_y)), MOON_RADIUS)

    pygame.display.flip()

pygame.quit()
sys.exit()
