import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__inir__(self)
        self.image = pygame.image.load(filename).comvert_alpha()
        self.rect = pygame.image.get_rect(center=(x, y))
        self.Vx = 0
        self.Vy = 0

    def update(self, WIDTH, HEIGHT):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна"""
        if self.rect.x < WIDTH - 20:
            self.rect.x += self.Vx
        elif self.rect.x > WIDTH - 20:
            self.Vx *= -1
        elif self.rect.x > 20:
            self.rect.x += self.Vx
        elif self.rect.x < 20:
            self.Vx *= -1

        if self.rect.y < HEIGHT - 20:
            self.rect.y += self.Vy
        elif self.rect.y > HEIGHT - 20:
            self.Vy *= -1
        elif self.rect.y > 20:
            self.rect.y += self.Vy
        elif self.rect.y < 20:
            self.Vy *= -1
        g = -1
        self.Vy += g
