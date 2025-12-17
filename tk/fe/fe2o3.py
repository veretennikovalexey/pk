import pygame
import math

pygame.init()

# окно
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fe₂O₃ — молекула")

clock = pygame.time.Clock()
CENTER = (WIDTH // 2, HEIGHT // 2)

# цвета
BLACK = (10, 10, 15)
IRON = (200, 120, 60)
OXYGEN = (220, 50, 50)
BOND = (180, 180, 200)
ELECTRON = (120, 200, 255)
WHITE = (240, 240, 240)

# атомы (позиции)
Fe_left  = (CENTER[0] - 120, CENTER[1])
Fe_right = (CENTER[0] + 120, CENTER[1])

O_top    = (CENTER[0], CENTER[1] - 140)
O_bl     = (CENTER[0] - 80, CENTER[1] + 120)
O_br     = (CENTER[0] + 80, CENTER[1] + 120)

atoms_O = [O_top, O_bl, O_br]

# свободные электроны
electron_count = 6
orbit_radius = 220
angle = 0
rotation_speed = math.radians(3)  # медленно

font = pygame.font.SysFont("Arial", 28)

running = True
while running:
    dt = clock.get_time() / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # связи
    for O in atoms_O:
        pygame.draw.line(screen, BOND, Fe_left, O, 2)
        pygame.draw.line(screen, BOND, Fe_right, O, 2)

    # атомы
    pygame.draw.circle(screen, IRON, Fe_left, 30)
    pygame.draw.circle(screen, IRON, Fe_right, 30)

    for O in atoms_O:
        pygame.draw.circle(screen, OXYGEN, O, 22)

    # подписи
    screen.blit(font.render("Fe", True, WHITE), (Fe_left[0]-18, Fe_left[1]-12))
    screen.blit(font.render("Fe", True, WHITE), (Fe_right[0]-18, Fe_right[1]-12))

    for O in atoms_O:
        screen.blit(font.render("O", True, WHITE), (O[0]-8, O[1]-12))

    # вращающиеся электроны
    angle += rotation_speed * dt
    for i in range(electron_count):
        theta = angle + i * (2 * math.pi / electron_count)
        x = CENTER[0] + orbit_radius * math.cos(theta)
        y = CENTER[1] + orbit_radius * math.sin(theta)
        pygame.draw.circle(screen, ELECTRON, (int(x), int(y)), 6)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
