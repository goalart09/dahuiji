class Settings():

    def __init__(self):
     """初始化游戏设置"""
    # 屏幕设置
     self.screen_width = 1000
     self.screen_height = 600
     self.bg_color = (225,225,225)

     # 飞船的设置
     self.ship_speed_factor = 1
     self.ship_limit = 3

     #子弹的设置
     self.bullet_speed_factor = 1
     self.bullet_width = 3
     self.bullet_height = 15
     self.bullet_color = 60,10,60
     self.bullets_allowed = 3

     #外星人设置
     self.alien_speed_factor = 0.5
     self.fleet_drop_speed =3
     # fleet_direction为1标识向右移，为-1表示向左移
     self.fleet_direction =1