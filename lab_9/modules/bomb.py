import pygame


class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        # масштабирую:
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() // 10, self.image.get_height() // 10))
        self.rect = self.image.get_rect(center=(x, y))
        self.Vy = 0

    def update(self, WIDTH, HEIGHT):
        """Переместить бомбу по прошествии единицы времени.

        Метод описывает перемещение бомбы за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации,
        """
        if self.rect.y > 20:
            self.rect.y += self.Vy
        else:
            self.kill()
        g = 1
        self.Vy += g

