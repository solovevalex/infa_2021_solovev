import pygame
from random import uniform,randint

class Target(pygame.sprite.Sprite):
    def __init__(self, x, y, Vx, Vy, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        # масштабирую
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() // 10, self.image.get_height() // 10))
        self.rect = self.image.get_rect(center=(x, y))
        self.Vx = Vx
        self.Vy = Vy

    def update(self, WIDTH, HEIGHT):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна"""
        if self.rect.x < WIDTH - 40:
            self.rect.x += self.Vx
        if self.rect.x >= WIDTH - 40:
            self.Vx = -self.Vx
        if self.rect.x >= 40:
            self.rect.x += self.Vx
        if self.rect.x < 40:
            self.Vx = -self.Vx

        if self.rect.y <= HEIGHT - 40:
            self.rect.y += self.Vy
        if self.rect.y > HEIGHT - 40:
            self.Vy = -self.Vy
        if self.rect.y >= 40:
            self.rect.y += self.Vy
        if self.rect.y < 40:
            self.Vy = -self.Vy

    def new_speed(self):
        # задается новая скорость в пикселах за кадр перерисовки
        if self.Vx >= 0:
            self.Vx = randint(0, 10)
        elif self.Vx <= 0:
            self.Vx = -randint(0, 10)
        if self.Vy >= 0:
            self.Vy = randint(0, 10)
        elif self.Vy <= 0:
            self.Vy = -randint(0, 10)
        self.Vy = randint(0, 10)
    def target_control(self, width,height):
        # функция не позволяет целям залетать, куда не надо
        if self.rect.centery > height:
            self.rect.centery = height
        if self.rect.centery < 0:
            self.rect.centery = 0
        if self.rect.centerx > width:
            self.rect.centerx = width
        if self.rect.centerx < 0:
            self.rect.centerx = 0
