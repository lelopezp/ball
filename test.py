import pygame


def main():
    pygame.init()
    surface = pygame.display.set_mode((400, 800))

    color = 0
    clock = pygame.time.Clock()

    x = 200
    y = 50
    v = 15

    run = True
    while run:
        clock.tick(20)

        surface.fill(pygame.Color(color, color, color))
        pygame.draw.circle(surface, pygame.Color(255, 255, 255), (x, y), 12)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            x += v
        if keys[pygame.K_LEFT]:
            x -= v

        if x > 400:
            x = 1
        if x < 0:
            x = 399

        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()