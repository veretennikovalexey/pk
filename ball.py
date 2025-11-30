import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 1500, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Физические шары")

clock = pygame.time.Clock()

gravity = 0
bounce = 0.8

def random_color():
    return (
        random.randint(50, 255),
        random.randint(50, 255),
        random.randint(50, 255)
    )

balls = []
for _ in range(5):
    radius = random.randint(1, 100)
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
        "m": radius,
        "color": random_color()
    })

def collide(b1, b2):
    dist = math.hypot(b1["x"] - b2["x"], b1["y"] - b2["y"])
    return dist < b1["r"] + b2["r"]

def resolve_collision(b1, b2):
    nx = b2["x"] - b1["x"]
    ny = b2["y"] - b1["y"]
    dist = math.hypot(nx, ny)

    if dist == 0:
        return

    nx /= dist
    ny /= dist

    v1 = b1["dx"] * nx + b1["dy"] * ny
    v2 = b2["dx"] * nx + b2["dy"] * ny

    if v1 < v2:
        return

    m1 = b1["m"]
    m2 = b2["m"]

    v1_new = (v1 * (m1 - m2) + 2 * m2 * v2) / (m1 + m2)
    v2_new = (v2 * (m2 - m1) + 2 * m1 * v1) / (m1 + m2)

    b1["dx"] += (v1_new - v1) * nx
    b1["dy"] += (v1_new - v1) * ny
    b2["dx"] += (v2_new - v2) * nx
    b2["dy"] += (v2_new - v2) * ny

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

        if event.type == pygame.MOUSEBUTTONDOWN:
            gravity = -gravity

    screen.fill((255, 255, 255))

    for b in balls:
        b["dy"] += gravity

        b["x"] += b["dx"]
        b["y"] += b["dy"]

        if b["x"] - b["r"] <= 0 or b["x"] + b["r"] >= WIDTH:
            b["dx"] = -b["dx"]

        if b["y"] + b["r"] >= HEIGHT:
            b["y"] = HEIGHT - b["r"]
            b["dy"] = -b["dy"] * bounce

        if b["y"] - b["r"] <= 0:
            b["y"] = b["r"]
            b["dy"] = -b["dy"] * bounce

    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            if collide(balls[i], balls[j]):
                resolve_collision(balls[i], balls[j])

    for b in balls:
        pygame.draw.circle(screen, b["color"], (int(b["x"]), int(b["y"])), b["r"])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
