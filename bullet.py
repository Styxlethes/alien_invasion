import pygame
from pygame.sprite import Sprite


class Bullets(Sprite):
    '''一个对飞船子弹进行管理的类'''

    def __init__(self, ai_settings, screen, ship):
        '''在飞船所在所在位置生成炮弹'''
        super().__init__()
        self.screen = screen

        # 在（0,0）处生成一个表示炮弹的矩形，在设置正确的位置
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height
        )
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 储存用小数表示的炮弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        '''向上移动炮弹'''
        # 更新表示炮弹速度的小数值
        self.y -= self.speed_factor
        # 更新表示炮弹位置的rect
        self.rect.y = self.y

    def draw_bullet(self):
        '''在屏幕上绘制炮弹'''
        pygame.draw.rect(self.screen, self.color, self.rect)
