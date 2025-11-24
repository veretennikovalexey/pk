import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Физические шары")

clock = pygame.time.Clock()


def random_color():
    return (
        random.randint(50, 255),
        random.randint(50, 255),
        random.randint(50, 255)
    )


# Создаём шары
balls = []
for _ in range(6):
    radius = random.randint(10, 50)
    x = random.randint(radius, WIDTH - radius)
    y = random.randint(radius, HEIGHT - radius)
    dx = random.choice([i / 2 for i in range(-10, 11) if i != 0])
    dy = random.choice([i / 2 for i in range(-10, 11) if i != 0])

    balls.append({
        "x": x,
        "y": y,
        "dx": dx,
        "dy": dy,
        "r": radius,
        "m": radius,  # масса = радиус
        "color": random_color()
    })


def collide(b1, b2):
    dist = math.hypot(b1["x"] - b2["x"], b1["y"] - b2["y"])
    return dist < b1["r"] + b2["r"]


def resolve_collision(b1, b2):
    # Вектор между центрами
    nx = b2["x"] - b1["x"]
    ny = b2["y"] - b1["y"]
    dist = math.hypot(nx, ny)

    if dist == 0:
        return

    # Нормализуем
    nx /= dist
    ny /= dist

    # Проекция скоростей на линию столкновения
    v1 = b1["dx"] * nx + b1["dy"] * ny
    v2 = b2["dx"] * nx + b2["dy"] * ny

    # Если уже разлетаются — ничего не делать
    if v1 < v2:
        return

    m1 = b1["m"]
    m2 = b2["m"]

    # Упругое столкновение 1D вдоль линии nx, ny
    v1_new = (v1 * (m1 - m2) + 2 * m2 * v2) / (m1 + m2)
    v2_new = (v2 * (m2 - m1) + 2 * m1 * v1) / (m1 + m2)

    # Обновляем скорости вдоль линии
    b1["dx"] += (v1_new - v1) * nx
    b1["dy"] += (v1_new - v1) * ny
    b2["dx"] += (v2_new - v2) * nx
    b2["dy"] += (v2_new - v2) * ny

    # Раздвигаем шары, чтобы они не пересекались
    overlap = b1["r"] + b2["r"] - dist
    if overlap > 0:
        b1["x"] -= nx * overlap / 2
        b1["y"] -= ny * overlap / 2
        b2["x"] += nx * overlap / 2
        b2["y"] += ny * overlap / 2


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    screen.fill((255, 255, 255))

    # Движение + столкновения со стенами
    for b in balls:
        b["x"] += b["dx"]
        b["y"] += b["dy"]

        if b["x"] - b["r"] <= 0 or b["x"] + b["r"] >= WIDTH:
            b["dx"] = -b["dx"]

        if b["y"] - b["r"] <= 0 or b["y"] + b["r"] >= HEIGHT:
            b["dy"] = -b["dy"]

    # Столкновения пар шаров
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            if collide(balls[i], balls[j]):
                resolve_collision(balls[i], balls[j])

    # Рисуем
    for b in balls:
        pygame.draw.circle(screen, b["color"], (int(b["x"]), int(b["y"])), b["r"])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
