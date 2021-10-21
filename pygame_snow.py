import sys
import pygame
from snow import Snow, PinholeCamera

if __name__ == "__main__":
    screen_size = (640, 480)
    screen = pygame.display.set_mode((640, 480))

    camera = PinholeCamera(50e-3, screen_size)
    snowflakes = Snow(10000, camera)

    while True:
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                sys.exit()

        screen.fill((0, 0, 0))

        snowflakes.step()

        x_all = snowflakes.project()

        for x in x_all.T:
            size = 1 / x[2]
            pygame.draw.circle(screen, (255, 255, 255), (x[0], x[1]), size)

        pygame.display.update()

