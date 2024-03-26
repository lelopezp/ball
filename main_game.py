import pygame


def run() -> None:
    pygame.init()

    surface = pygame.display.set_mode((800, 700))

    pygame.quit()


if __name__ == "__main__":
    print("hello world")
    run()

