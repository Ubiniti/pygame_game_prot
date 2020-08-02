from typing import List
from Application import Application, Window, ImageSprite, Image, Key


class MyGame(Application):
    def __init__(self):
        Application.__init__(self, (800, 600))
        ball_image = Image("asset/ball.gif")
        self.ball_sprite = ImageSprite(ball_image)

    def on_key_pressed(self, keys: List[bool]):
        if keys[Key.K_a]:
            self.ball_sprite.move((-1.0, 0.0))
        if keys[Key.K_d]:
            self.ball_sprite.move((1.0, 0.0))

    def on_draw(self, window: 'Window'):
        window.draw(self.ball_sprite)
