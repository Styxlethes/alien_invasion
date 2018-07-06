import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard():
    '''显示得分信息的类'''

    def __init__(self, ai_settings, screen, stats):
        '''初始化显示得分信息涉及的属性'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示得分信息使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 准备包括最高得分当前得分的图像
        self.prep_score()
        self.prep_hight_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        '''将得分转变为图像'''
        rounded_score = round(self.stats.score, -1)
        score_str = '{:,}'.format(rounded_score)
        self.score_image = self.font.render('score:'+score_str, True, self.text_color,
                                            self.ai_settings.bg_color)

        # 将得分放在屏幕的右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right-20
        self.score_rect.top = 20

    def prep_hight_score(self):
        '''将最高得分转换为图像'''
        rounded_hight_score = round(self.stats.hight_score, -1)
        hight_score_str = '{:,}'.format(rounded_hight_score)
        self.hight_score_image = self.font.render('hightest score:'+hight_score_str, True,
                                                  self.text_color, self.ai_settings.bg_color)

        # 将最高得分放在屏幕顶部中央
        self.hight_score_rect = self.hight_score_image.get_rect()
        self.hight_score_rect.centerx = self.screen_rect.centerx
        self.hight_score_rect.top = self.score_rect.top

    def prep_level(self):
        '''将等级转化为图像'''
        self.level_image = self.font.render('level:'+str(self.stats.level), True,
                                            self.text_color, self.ai_settings.bg_color)

        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom+10

    def prep_ships(self):
        '''显示剩余多少艘飞船'''
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10+ship_number*ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        '''在屏幕上显示得分'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.hight_score_image, self.hight_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # 绘制飞船
        self.ships.draw(self.screen)
