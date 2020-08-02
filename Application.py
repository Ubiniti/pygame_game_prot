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

    def on_key_up(self, key: int, mod: int):
        pass

    def on_key_down(self, key: int, mod: int):
        pass

    def on_key_pressed(self, keys: List[bool]):
        pass

    def on_quit(self):
        sys.exit()

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


class Drawable:
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
    def __init__(self, font: Font):
        self.position = (0, 0)
        self.font = font
        drawable = font.render("", True, WHITE, BLACK)
        Drawable.__init__(self, drawable)

    def set_text(self, text: str):
        self.drawable = self.font.render(text, True, WHITE, BLACK)
        self.rect = self.drawable.get_rect()
        self.rect.center = self.position

    def set_position(self, pos: Vector2F):
        x, y = pos
        self.position = int(x), int(y)
        self.rect.center = self.position
