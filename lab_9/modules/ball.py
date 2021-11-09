import pygame


# необходимые параметры для определения нижеопределяемого класса
def start_speed_x(position, V):
    """задает направление начальной скорости шарика (снаряда пушки) по х"""
    if position == 'up':
        return 0
    elif position == 'down':
        return 0
    elif position == 'right':
        return V
    elif position == 'left':
        return -V


def start_speed_y(position, V):
    """задает направление начальной скорости шарика (снаряда пушки) по y"""
    if position == 'up':
        return -V
    elif position == 'down':
        return V
    elif position == 'right':
        return 0
    elif position == 'left':
        return 0


class Ball(pygame.sprite.Sprite):
    """Это шарик - снаряд, который вудетает из пушки-танка"""

    def __init__(self, x, y, Vx, Vy, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        # нужно отмаштабировать шарики
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() // 20, self.image.get_height() // 20))
        self.rect = self.image.get_rect(center=(x, y))
        self.Vx = Vx
        self.Vy = Vy
        self.life = 0

    def update(self, *args):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна"""
        if self.rect.x < args[0] - 20:
            self.rect.x += self.Vx
        if self.rect.x > args[0] - 20:
            self.Vx *= -1
        if self.rect.x > 20:
            self.rect.x += self.Vx
        if self.rect.x < 20:
            self.Vx *= -1

        if self.rect.y < args[1] - 20:
            self.rect.y += self.Vy
        if self.rect.y > args[1] - 20:
            self.Vy *= -1
        if self.rect.y > 20:
            self.rect.y += self.Vy
        if self.rect.y < 20:
            self.Vy *= -1
        g = 1
        self.Vy += g

    def kill(self):
        time_life = 300
        if self.life == time_life:
            self.kill()
        else:
            self.life += 1
