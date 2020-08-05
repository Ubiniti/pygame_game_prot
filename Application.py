import sys
from typing import Tuple, List
import pygame
import constants_keys as Key
pygame.init()

Vector2F = Tuple[float, float]

BLACK = 0, 0, 0
WHITE = 200, 200, 200
DEFAULT_FONT_SIZE = 16


class Application:
    def __init__(self, window_size):
        self.window = Window(window_size)
        self.__keys_pressed = []
        self.clock = Clock()

    def on_key_up(self, key: int, mod: int):
        pass

    def on_key_down(self, key: int, mod: int):
        pass

    def on_key_pressed(self, keys: List[bool]):
        pass

    def on_quit(self):
        sys.exit()

    def on_update(self, detla_time: float):
        pass

    def on_draw(self, window: 'Window'):
        pass

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: self.on_quit()
                if event.type == pygame.KEYUP: self.on_key_up(event.key, event.mod)
                if event.type == pygame.KEYDOWN: self.on_key_down(event.key, event.mod)

            self.__keys_pressed = pygame.key.get_pressed()
            self.on_key_pressed(self.__keys_pressed)

            self.clock.tick()
            self.on_update(self.clock.get_delta_time())

            self.window.clear()
            self.on_draw(self.window)
            self.window.display()

class Window:
    def __init__(self, size):
        self.screen = pygame.display.set_mode(size)

    def clear(self, color = (0, 0, 0)):
        self.screen.fill(color)

    @staticmethod
    def display():
        pygame.display.flip()

    def draw(self, drawable: 'Drawable'):
        drawable.draw(self)


class Clock:
    def __init__(self):
        self.__pygame_clock = pygame.time.Clock()
        self.__delta_time = 0.0

    def tick(self) -> float:
        self.__delta_time = self.__pygame_clock.tick()
        return self.__delta_time

    def get_delta_time(self) -> float:
        return self.__delta_time

    def get_fps(self):
        return self.__pygame_clock.get_fps()


class DrawableInterface:
    def draw(self, window: Window):
        pass


class Drawable(DrawableInterface):
    def __init__(self, drawable):
        self.rect = drawable.get_rect()
        self.drawable = drawable

    def draw(self, window: Window):
        window.screen.blit(self.drawable, self.rect)


class Image(Drawable):
    def __init__(self, path: str):
        self.image = pygame.image.load(path)
        Drawable.__init__(self, self.image)


class Sprite(Drawable):
    def __init__(self, pygame_drawable):
        self.drawable = pygame_drawable
        Drawable.__init__(self, pygame_drawable)

    def move(self, vector: Vector2F):
        self.rect = self.rect.move(vector)


class ImageSprite(Sprite):
    def __init__(self, image: Image):
        Sprite.__init__(self, image.image)


class Font:
    def __init__(self, path: str):
        self.pygame_font = pygame.font.Font(path, DEFAULT_FONT_SIZE)

    def render(self, text: str, antialias: bool, color, background):
        return self.pygame_font.render(text, antialias, color, background)


class TextLabel(Drawable):
    ALIGN_LEFT = 0b1000
    ALIGN_CENTER = 0b1100
    ALIGN_RIGHT = 0b0100
    VERTICAL_ALIGN_TOP = 0b0010
    VERTICAL_ALIGN_MIDDLE = 0b0011
    VERTICAL_ALIGN_BOTTOM = 0b0001

    def __init__(self, font: Font):
        self.position = (0, 0)
        self.font = font
        drawable = font.render("", True, WHITE, BLACK)
        Drawable.__init__(self, drawable)
        self.alignment = self.ALIGN_LEFT | self.VERTICAL_ALIGN_MIDDLE

    def set_text(self, text: str):
        self.drawable = self.font.render(text, True, WHITE, BLACK)
        self.rect = self.drawable.get_rect()
        self.rect.bottomleft = self.position

    def set_position(self, pos: Vector2F):
        x, y = pos
        self.position = int(x), int(y)
        self.rect.center = self.position

    def set_alignment(self, alignment_flags):
        self.alignment = alignment_flags

    def __set_rect_position(self, position: Vector2F):
        if self.alignment == self.ALIGN_LEFT | self.VERTICAL_ALIGN_BOTTOM:
            self.rect.bottomleft = position
        elif self.alignment == self.ALIGN_LEFT | self.VERTICAL_ALIGN_MIDDLE:
            self.rect.midleft = position
        elif self.alignment == self.ALIGN_LEFT | self.VERTICAL_ALIGN_TOP:
            self.rect.topleft = position
        elif self.alignment == self.ALIGN_RIGHT | self.VERTICAL_ALIGN_BOTTOM:
            self.rect.bottomleft = position
        elif self.alignment == self.ALIGN_RIGHT | self.VERTICAL_ALIGN_MIDDLE:
            self.rect.midleft = position
        elif self.alignment == self.ALIGN_RIGHT | self.VERTICAL_ALIGN_TOP:
            self.rect.topleft = position
        elif self.alignment == self.ALIGN_CENTER | self.VERTICAL_ALIGN_MIDDLE:
            self.rect.center = position
        else:
            raise Exception('TextLabel alignment value is not allowed')