import pygame


def main():
    pygame.init()
    surface = pygame.display.set_mode((400, 800))

    color = 0
    clock = pygame.time.Clock()

    circle_x = 200
    circle_y = 50

    run = True
    while run:
        clock.tick(20)

        surface.fill(pygame.Color(color, color, color))
        pygame.draw.circle(surface, pygame.Color(255, 255, 255), (circle_x, circle_y), 12)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            circle_x += 15
        if keys[pygame.K_LEFT]:
            circle_x -= 15

        if circle_x > 400:
            circle_x = 0
        elif circle_x < 0:
            circle_x = 400

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()