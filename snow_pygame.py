import sys
import pygame
from snow import Snow, PinholeCamera

if __name__ == "__main__":
    screen_size = [1024, 768]
    screen = pygame.display.set_mode(screen_size)

    camera = PinholeCamera(50e-3, screen_size)
    snowflakes = Snow(1500, camera)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                sys.exit()

        screen.fill((0, 0, 0))

        snowflakes.step()

        x_all = snowflakes.project()

        for x in x_all.T:
            size = -15 / x[2]
            pygame.draw.circle(screen, (255, 255, 255), (x[0], x[1]), size)

        pygame.display.update()

        # Run a fixed frame rate
        clock.tick(30)

