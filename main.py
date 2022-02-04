import pygame, sys

class Car(pygame.sprite.Sprite):
    def __init__(self, w, h):
        super().__init__()
        # duplicate the image to avoid losing resolution
        # when rotating it (pygame issues)
        self.original_image = pygame.image.load('Audi.png')
        self.image = self.original_image
        self.rect = self.image.get_rect(center = (640, 360))

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(120)
