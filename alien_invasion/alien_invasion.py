import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import ScoreBoard
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))  #窗口大小1200*800像素
    pygame.display.set_caption("Alien Invasion")  #设置窗口名称
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings)  #创建一个用于存储游戏统计信息的实例
    sb = ScoreBoard(ai_settings, screen, stats)  #创建记分牌
    ship = Ship(ai_settings, screen)  #创建一艘飞船
    bullets = Group()  #创建一个用于存储子弹的编组
    aliens = Group()  #创建一个用于存储外星人的编组
    gf.create_fleet(ai_settings, screen, ship, aliens)  #创建外星人群

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)  #响应键鼠事件
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets)  #更新子弹位置
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens,
                             bullets)  #更新外星人位置
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                         play_button)  #更新屏幕


run_game()