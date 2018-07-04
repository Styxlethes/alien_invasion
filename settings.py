class Settings():
    '''储存游戏所有设置的类'''

    def __init__(self):
        '''初始化游戏设置'''
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # 三个值为RGB的颜色，取值范围为0~255

        # 飞船设置
        self.ship_speed_factor = 1.5

        # 炮弹设置
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed=5
