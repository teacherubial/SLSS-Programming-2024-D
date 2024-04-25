# Introduction to Pygame
#    - boilerplate is useful to set up our environments
#    - the Sprite class has some really cool things in it

import pygame


class Dvdlogo(pygame.sprite.Sprite):
    """Represents DVD logo sprite"""

    def __init__(self):
        super().__init__()

        # image -> visual representation
        self.image = pygame.image.load("./Images/dvd-logo.png")

        # rect  -> hitbox representation
        # get_rect() -> Rect
        #     [x, y, width, height]
        #     [0, 0, <width of image>, <height of image>]
        self.rect = self.image.get_rect()

        # Velocity of the Dvd Logo
        self.vel_x = 3
        self.vel_y = 3


def start():
    """Environment Setup and Game Loop"""

    pygame.init()

    # --CONSTANTS--
    # COLOURS
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    EMERALD = (21, 219, 147)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GRAY = (128, 128, 128)

    WIDTH = 1280  # Pixels
    HEIGHT = 720
    SCREEN_SIZE = (WIDTH, HEIGHT)

    # --VARIABLES--
    screen = pygame.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pygame.time.Clock()

    pygame.display.set_caption("DVD Logo Screensaver")

    # Make a DVD Logo object
    dvdlogo = Dvdlogo()

    # Move the dvd logo to the middle
    dvdlogo.rect.centerx = WIDTH // 2
    dvdlogo.rect.centery = HEIGHT // 2

    # Create a group of sprites
    all_sprites = pygame.sprite.Group()

    # Add the DVD Logo object to the group of sprites
    all_sprites.add(dvdlogo)

    # --MAIN LOOP--
    while not done:
        # --- Event Listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # --- Update the world state
        # Update the location of the dvdlogo
        #     dvdlogo.rect.x + dvdlogo.vel_x
        #     dvdlogo.rect.y + dvdlogo.vel_y
        dvdlogo.rect.x = dvdlogo.rect.x + dvdlogo.vel_x
        dvdlogo.rect.y += dvdlogo.vel_y

        print(dvdlogo.rect.x, dvdlogo.rect.y)

        # --- Draw items
        screen.fill(BLACK)

        # Draw all the sprites on the screen
        all_sprites.draw(screen)

        # Update the screen with anything new
        pygame.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()
