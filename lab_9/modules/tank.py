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
        WIDTH = 800
        HEIGHT = 600
        # эта функция задает положение изображения танка на экране в зависимости от того, куда он собирается ехать
        if position == 'up':
            self.image = self.up
            self.rect.y -= self.V
            if self.rect.y < 0:
                self.rect.y = 0
        elif position == 'down':
            self.image = self.down
            self.rect.y += self.V
            if self.rect.y > HEIGHT - self.rect.width:
                self.rect.y = HEIGHT - self.rect.width
        elif position == 'left':
            self.image = self.left
            self.rect.x -= self.V
            if self.rect.x < 0:
                self.rect.x = 0
        elif position == 'right':
            self.image = self.right
            self.rect.x += self.V
            if self.rect.x > WIDTH - self.rect.width:
                self.rect.x = WIDTH - self.rect.width

    def position(self):
        """Возвращает последнюю позицию танка: вверх, вниз, вправо, влево"""
        if self.image == self.right:
            return 'right'
        if self.image == self.left:
            return 'left'
        if self.image == self.down:
            return 'down'
        if self.image == self.up:
            return 'up'


