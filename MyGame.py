from typing import List
from Application import Application, Window, ImageSprite, Image, Key, DrawableInterface, TextLabel, Font, Clock, \
    Animation, AnimationSprite
from config import config

RIGHT = 1
LEFT = -1

resource_container = {}

class MyGame(Application):
    def __init__(self):
        Application.__init__(self, (800, 600))
        self.player = Player()
        # self.fps_label = FpsLabel()
        # self.fps_label.set_position(
        #     tuple(config['interface']['fps_counter_position'])
        # )

    def on_resource_load(self):
        self.__load_animation(Player.RESOURCE_ANIMATION_IDLE, config.image.animations.player.idle)
        self.__load_animation(Player.RESOURCE_ANIMATION_RUN, config.image.animations.player.run)
        self.player.on_resource_load()

    def on_key_pressed(self, keys: List[bool]):
        self.player.on_key_pressed(keys)

    def on_key_up(self, key: int, mod: int):
        self.player.on_key_up(key, mod)

    def on_key_down(self, key: int, mod: int):
        self.player.on_key_down(key, mod)

    def on_update(self, detla_time: float):
        # self.fps_label.update(self.clock)
        # self.chuck_animation_sprite.update()
        self.player.update()

    def on_draw(self, window: 'Window'):
        self.player.draw(window)
        # self.fps_label.draw(window)
        # self.chuck_animation_sprite.draw(window)

    def __load_animation(self, key: str, paths: List[str]):
        resource_container[key] = Animation.create_from_paths(
            paths,
            config.animation.interval
        )


class Player(DrawableInterface):
    RESOURCE_ANIMATION_IDLE = 'animation_player_idle'
    RESOURCE_ANIMATION_RUN = 'animation_player_run'

    ANIMATION_IDLE = 'idle'
    ANIMATION_RUN = 'run'

    STATE_IDLE = 'idle'
    STATE_RUN = 'run'

    def __init__(self):
        self.running_speed = float(config.player.running_speed)
        self.animations = {}
        self.state = self.STATE_IDLE
        self.position = (100, 200)
        self.direction = RIGHT

    def on_resource_load(self):
        self.animations[self.ANIMATION_IDLE] = resource_container.get(self.RESOURCE_ANIMATION_IDLE)
        self.animations[self.ANIMATION_RUN] = resource_container.get(self.RESOURCE_ANIMATION_RUN)

    def on_key_pressed(self, keys: List[bool]):
        if keys[Key.K_a]:
            self.run(LEFT)
        if keys[Key.K_d]:
            self.run(RIGHT)

    def on_key_up(self, key: int, mod: int):
        if key in [Key.K_a, Key.K_d]:
            self.state = self.STATE_IDLE

    def on_key_down(self, key: int, mod: int):
        if key in [Key.K_a, Key.K_d]:
            self.state = self.STATE_RUN

    def run(self, direction: int):
        self.direction = direction
        x, y = self.position
        self.position = (x + float(direction) * self.running_speed, y)

    def draw(self, window: Window):
        flipped = True if self.direction == LEFT else False
        self.__get_animation().drawOnPosition(window, self.position, flipped)

    def update(self):
        # print(self.state)
        self.__get_animation().update()

    def __get_animation(self) -> Animation:
        return self.animations.get(self.state)


class FpsLabel(TextLabel):
    def __init__(self):
        self.font = Font(config['font']['roboto'])
        TextLabel.__init__(self, self.font)
        self.set_alignment(self.ALIGN_RIGHT | self.VERTICAL_ALIGN_MIDDLE)

    def update(self, clock: Clock):
        self.set_text(str(round(clock.get_fps())))
