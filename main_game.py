import pygame
import random
import circle_class


def main() -> None:

    # stuff about the window
    pygame.init()
    window_width = 400
    window_height = 500
    surface = pygame.display.set_mode((window_width, window_height))
    background_color_r = 0
    background_color_g = 0
    background_color_b = 0
    clock = pygame.time.Clock()

    speed = 1

    # stuff about the circle
    circle = circle_class.Circle(200, 50, 12, speed)

    # dictionary to store line openings
    d_o = dict()
    d_o[0] = random.randint(0, window_width - 50)
    d_o[1] = random.randint(0, window_width - 50)
    d_o[2] = random.randint(0, window_width - 50)
    d_o[3] = random.randint(0, window_width - 50)
    d_o[4] = random.randint(0, window_width - 50)
    d_o[5] = random.randint(0, window_width - 50)
    d_o[6] = random.randint(0, window_width - 50)
    d_o[7] = random.randint(0, window_width - 50)
    d_o[8] = random.randint(0, window_width - 50)
    d_o[9] = random.randint(0, window_width - 50)
    d_o[10] = random.randint(0, window_width - 50)
    d_o[11] = random.randint(0, window_width - 50)

    # dictionary to store y positions
    d_y = dict()
    d_y[0] = 200
    d_y[1] = 250
    d_y[2] = 300
    d_y[3] = 350
    d_y[4] = 400
    d_y[5] = 450
    d_y[6] = 500
    d_y[7] = 550
    d_y[8] = 600
    d_y[9] = 650
    d_y[10] = 700
    d_y[11] = 750

    tracker = 0

    # run loop
    run = True
    while run:

        # how often window updates
        clock.tick(50)

        # draw background and circle
        surface.fill(pygame.Color(background_color_r, background_color_g, background_color_b))
        pygame.draw.circle(surface, pygame.Color(255, 255, 255), (circle.x(), circle.y()), circle.radius())

        # draw lines
        for (o_key, o), (y_key, y) in zip(d_o.items(), d_y.items()):
            pygame.draw.line(surface, pygame.Color(255, 255, 255), (0, y), (o, y), 10)
            pygame.draw.line(surface, pygame.Color(255, 255, 255), (o+30, y), (window_width, y), 10)

        # move lines up
        for num in range(12):
            d_y[num] -= speed

        # if the grid dot below the ball is not a wall, call circles fall function
        if circle.y() < window_height - circle.radius():
            if surface.get_at((circle.x() + circle.radius(), circle.y() + circle.radius())) == pygame.Color(255, 255, 255):
                circle.stuck()
            else:
                circle.fall()

        # after line passes top of screen, generate new line below
        if d_y[tracker] <= 0:
            d_y[tracker] = 600
            if tracker < 11:
                tracker += 1
            else:
                tracker = 0

        # if ball touches top of screen, game ends
        if circle.y() - circle.radius() <= 0:
            run = False

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
