import pygame

from pygame.sprite import Group
from settings import Settings
from game_status import GameStatus
from score_board import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化游戏并建立一个屏幕对象
    pygame.init()  # 初始化pygame
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption('Alien Invasion')

    # 创建play按钮
    play_button = Button(ai_settings, screen, 'Play')

    # 创建一艘飞船,一个储存炮弹的编组以及一个alienship编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # 创建alien群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建一个用于储存游戏统计信息的实例,并创建计分板
    stats = GameStatus(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 开始游戏的主循环
    while True:

        gf.check_events(ai_settings, screen, stats, sb, play_button,
                        ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb,
                              ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship,
                             aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb,
                         ship, aliens, bullets, play_button)


if __name__ == '__main__':
    run_game()
