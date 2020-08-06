from typing import Tuple


class Config:
    class Image:
        class Animations:
            class Player:
                climbing = list
                collect = list
                defeated = list
                fire = list
                hurt = list
                idle = list
                jump_fire = list
                jump_toss = list
                run = list

            player = Player()

        animations = Animations()

    class Animation:
        interval = int

    class Player:
        running_speed = float

    class Interface:
        fps_counter_position = Tuple[float, float]

    image = Image()
    animation = Animation()
    fonts = {}
    player = Player()

    def __init__(self):
        pass


config = Config()

config.animation.interval = 90

config.fonts = {
    'roboto': 'asset/Roboto-Regular.ttf'
}

config.player.running_speed = 1.0

config.image.animations.player.climbing = [
                    'asset/chuck/bro5_climbing0001.png',
                    'asset/chuck/bro5_climbing0002.png',
                    'asset/chuck/bro5_climbing0003.png',
                    'asset/chuck/bro5_climbing0004.png',
                    'asset/chuck/bro5_climbing0005.png',
                    'asset/chuck/bro5_climbing0006.png',
                    'asset/chuck/bro5_climbing0007.png',
                    'asset/chuck/bro5_climbing0008.png',
                    'asset/chuck/bro5_climbing0009.png',
                    'asset/chuck/bro5_climbing0010.png',
                    'asset/chuck/bro5_climbing0011.png',
                ]

config.image.animations.player.collect = [
                    'asset/chuck/bro5_collect0001.png',
                    'asset/chuck/bro5_collect0002.png',
                    'asset/chuck/bro5_collect0003.png',
                    'asset/chuck/bro5_collect0004.png',
                    'asset/chuck/bro5_collect0005.png',
                    'asset/chuck/bro5_collect0006.png',
                    'asset/chuck/bro5_collect0007.png',
                ]

config.image.animations.player.defeated = [
                    'asset/chuck/bro5_defeated0001.png',
                    'asset/chuck/bro5_defeated0002.png',
                    'asset/chuck/bro5_defeated0003.png',
                    'asset/chuck/bro5_defeated0004.png',
                    'asset/chuck/bro5_defeated0005.png',
                    'asset/chuck/bro5_defeated0006.png',
                    'asset/chuck/bro5_defeated0007.png',
                ]

config.image.animations.player.fire = [
                    'asset/chuck/bro5_fire0001.png',
                    'asset/chuck/bro5_fire0002.png',
                    'asset/chuck/bro5_fire0003.png',
                    'asset/chuck/bro5_fire0004.png',
                    'asset/chuck/bro5_fire0005.png',
                ]

config.image.animations.player.hurt = [
                    'asset/chuck/bro5_hurt0001.png',
                    'asset/chuck/bro5_hurt0002.png',
                    'asset/chuck/bro5_hurt0003.png',
                    'asset/chuck/bro5_hurt0004.png',
                    'asset/chuck/bro5_hurt0005.png',
                    'asset/chuck/bro5_hurt0006.png',
                ]

config.image.animations.player.idle = [
                    'asset/chuck/bro5_idle0001.png',
                    'asset/chuck/bro5_idle0002.png',
                    'asset/chuck/bro5_idle0003.png',
                    'asset/chuck/bro5_idle0004.png',
                    'asset/chuck/bro5_idle0005.png',
                    'asset/chuck/bro5_idle0006.png',
                    'asset/chuck/bro5_idle0007.png',
                    'asset/chuck/bro5_idle0008.png',
                ]

config.image.animations.player.jump_fire = [
                    'asset/chuck/bro5_jump_fire0001.png',
                    'asset/chuck/bro5_jump_fire0002.png',
                    'asset/chuck/bro5_jump_fire0003.png',
                    'asset/chuck/bro5_jump_fire0004.png',
                    'asset/chuck/bro5_jump_fire0005.png',
                ]

config.image.animations.player.jump_toss = [
                    'asset/chuck/bro5_jump_toss0001.png',
                    'asset/chuck/bro5_jump_toss0002.png',
                    'asset/chuck/bro5_jump_toss0003.png',
                    'asset/chuck/bro5_jump_toss0004.png',
                    'asset/chuck/bro5_jump_toss0005.png',
                    'asset/chuck/bro5_jump_toss0006.png',
                    'asset/chuck/bro5_jump_toss0007.png',
                    'asset/chuck/bro5_jump_toss0008.png',
                    'asset/chuck/bro5_jump_toss0009.png',
                    'asset/chuck/bro5_jump_toss0010.png',
                    'asset/chuck/bro5_jump_toss0011.png',
                ]

config.image.animations.player.run = [
                    'asset/chuck/bro5_run0001.png',
                    'asset/chuck/bro5_run0002.png',
                    'asset/chuck/bro5_run0003.png',
                    'asset/chuck/bro5_run0004.png',
                    'asset/chuck/bro5_run0005.png',
                    'asset/chuck/bro5_run0006.png',
                    'asset/chuck/bro5_run0007.png',
                ]
