import pygame
import circle_class


def main() -> None:

    # stuff about the window
    pygame.init()
    window_width = 400
    window_height = 800
    surface = pygame.display.set_mode((window_width, window_height))
    background_color_r = 0
    background_color_g = 0
    background_color_b = 0
    clock = pygame.time.Clock()

    # stuff about the circle
    circle = circle_class.Circle(200, 50, 12, 1)

    # run loop
    run = True
    while run:

        # how often window updates
        clock.tick(300)

        # draw background and circle
        surface.fill(pygame.Color(background_color_r, background_color_g, background_color_b))
        pygame.draw.circle(surface, pygame.Color(255, 255, 255), (circle.x(), circle.y()), circle.radius())

        # check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # key controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and circle.x() < window_width - circle.radius():
            circle.go_right()
        if keys[pygame.K_LEFT] and circle.x() > circle.radius():
            circle.go_left()

        # update window
        pygame.display.flip()

    # quit game
    pygame.quit()


if __name__ == "__main__":
    main()
