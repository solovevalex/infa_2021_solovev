import pygame


class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__inir__(self)
        self.image = pygame.image.load(filename).comvert_alpha()
        self.rect = pygame.image.get_rect(center=(x, y))
        self.Vy = 0

    def update(self, WIDTH, HEIGHT):
        """Переместить бомбу по прошествии единицы времени.

        Метод описывает перемещение бомбы за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации,
        """
        if self.rect.y > 20:
            self.rect.y += self.Vy
        else:
            pass
        g = -1
        self.Vy += g
