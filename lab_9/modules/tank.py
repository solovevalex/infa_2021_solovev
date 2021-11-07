import pygame

class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() // 5, self.image.get_height() // 5))
        self.rect = self.image.get_rect(center=(x, y))
        self.left = self.image
        self.right = pygame.transform.flip(self.image, 1, 0)
        self.down = pygame.transform.rotate(self.image, 90)
        self.up = pygame.transform.rotate(self.image, -90)
        self.V = 10


    def image_tank(self, position):
        if position == 'up':
            self.image = self.up
        elif position == 'down':
            self.image = self.down
        elif position == 'left':
            self.image = self.left
        elif position == 'right':
            self.image = self.right

