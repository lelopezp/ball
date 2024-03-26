import pygame


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
    circle_x = 200
    circle_y = 50
    circle_r = 12
    circle_v = 1

    # run loop
    run = True
    while run:

        # how often window updates
        clock.tick(300)

        # draw background and circle
        surface.fill(pygame.Color(background_color_r, background_color_g, background_color_b))
        pygame.draw.circle(surface, pygame.Color(255, 255, 255), (circle_x, circle_y), circle_r)

        # check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # key controls 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and circle_x < window_width - circle_r:
            circle_x += circle_v
        if keys[pygame.K_LEFT] and circle_x > circle_r:
            circle_x -= circle_v

        # update window
        pygame.display.flip()

    # quit game
    pygame.quit()


if __name__ == "__main__":
    main()
