from typing import List
from Application import Application, Window, ImageSprite, Image, Key, DrawableInterface, TextLabel, Font, Clock

RIGHT = 1
LEFT = -1


config = {
    'image': {
        'player': 'asset/ball.gif'
    },
    'font': {
        'roboto': 'asset/Roboto-Regular.ttf'
    },
    'player': {
        'running_speed': 1.0
    },
    'interface': {
        'fps_counter_position': (200, 200)
    }
}


class MyGame(Application):
    def __init__(self):
        Application.__init__(self, (800, 600))
        self.player = Player()
        self.fps_label = FpsLabel()
        self.fps_label.set_position(
            tuple(config['interface']['fps_counter_position'])
        )

    def on_key_pressed(self, keys: List[bool]):
        if keys[Key.K_a]:
            self.player.run(LEFT)
        if keys[Key.K_d]:
            self.player.run(RIGHT)

    def on_update(self, detla_time: float):
        self.fps_label.update(self.clock)

    def on_draw(self, window: 'Window'):
        self.player.draw(window)
        self.fps_label.draw(window)


class Player(DrawableInterface):
    def __init__(self):
        self.sprite = ImageSprite(
            Image(config['image']['player'])
        )
        self.running_speed = float(config['player']['running_speed'])

    def run(self, direction: int):
        self.sprite.move((float(direction) * self.running_speed, 0.0))

    def draw(self, window: Window):
        self.sprite.draw(window)


class FpsLabel(TextLabel):
    def __init__(self):
        self.font = Font(config['font']['roboto'])
        TextLabel.__init__(self, self.font)
        self.set_alignment(self.ALIGN_RIGHT | self.VERTICAL_ALIGN_MIDDLE)

    def update(self, clock: Clock):
        self.set_text(str(round(clock.get_fps())))

