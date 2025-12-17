import pygame
import math

pygame.init()

# экран
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fe атом и валентные электроны")

clock = pygame.time.Clock()

# параметры
center = (WIDTH // 2, HEIGHT // 2)
radius = 150  # радиус орбиты электронов
electron_count = 8
rotation_speed = math.radians(6)  # 6 градусов в секунду = 1 круг за 60 секунд

angle = 0  # текущий угол

# цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # фон
    screen.fill(BLACK)

    # текст Fe в центре
    font = pygame.font.SysFont("Arial", 80)
    text = font.render("Fe", True, WHITE)
    text_rect = text.get_rect(center=center)
    screen.blit(text, text_rect)

    # обновляем угол вращения
    dt = clock.get_time() / 1000  # delta time в секундах
    angle += rotation_speed * dt

    # рисуем электроны
    for i in range(electron_count):
        # вычисляем позицию
        theta = angle + i * (2 * math.pi / electron_count)
        x = center[0] + radius * math.cos(theta)
        y = center[1] + radius * math.sin(theta)

        # рисуем круг
        pygame.draw.circle(screen, BLUE, (int(x), int(y)), 10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
