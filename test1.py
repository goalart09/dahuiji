import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from allen import Alien
from game_stats import GameStats
def run_game():

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Allen Invasion")

    # 创建一个用于存储游戏统计信息的实例
    status =GameStats(ai_settings)

#创建一艘飞船
    ship = Ship(ai_settings,screen)
#创建一个用于存储子弹的编组
    bullets = Group()
# 创建一个外星人
    aliens = Group()
#创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
#开始游戏循环
    while True:

        gf.check_events(ai_settings,screen,ship,bullets)
        if status.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,status,screen,ship,aliens,bullets)
        gf.update_screen(ai_settings ,screen,ship,aliens,bullets)
        #screen_rect = screen.get_rect()
       # print(screen_rect)

# # 每次循环时都重绘屏幕
#         screen.fill(ai_settings.bg_color)
#         ship.blitme()
# # 让最近绘制的屏幕可见
#         pygame.display.flip()
run_game()


