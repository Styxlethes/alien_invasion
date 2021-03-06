class Settings():
    '''储存游戏所有设置的类'''

    def __init__(self):
        '''初始化游戏设置'''
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # 三个值为RGB的颜色，取值范围为0~255

        # 飞船设置
        self.ship_limit = 3

        # 炮弹设置
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 500

        # alien设置
        self.fleet_drop_speed = 10

        # 以怎样的速度加快游戏节奏
        self.speedup_scale = 1.1
        # alien点数提高的速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''初始化随游戏进行的二变化的设置'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction为1表示右移，-1表示左移
        self.fleet_direction = 1
        # 计分
        self.alien_points = 50

    def increase_speed(self):
        '''提高速度和alien点数的设置'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points*self.score_scale)
        print(self.alien_points)
