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
        self.background_color = WHITE

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

    def on_resource_load(self):
        pass

    def run(self):
        self.on_resource_load()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.on_quit()
                if event.type == pygame.KEYUP:
                    self.on_key_up(event.key, event.mod)
                if event.type == pygame.KEYDOWN:
                    self.on_key_down(event.key, event.mod)

            self.__keys_pressed = pygame.key.get_pressed()
            self.on_key_pressed(self.__keys_pressed)

            self.clock.tick()
            self.on_update(self.clock.get_delta_time())

            self.window.clear(self.background_color)
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

    def draw(self, drawable: 'DrawableInterface'):
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

    @staticmethod
    def get_time_from_init():
        return pygame.time.get_ticks()


class DrawableInterface:
    def draw(self, window: Window):
        pass

    def move(self, vector: Vector2F):
        pass

    def set_position(self, vector: Vector2F):
        pass


class Image:
    def __init__(self, path: str):
        self._pygame_image = pygame.image.load(path)
        self._pygame_rect = self._pygame_image.get_rect()
        self._pygame_image_xmirror = pygame.transform.flip(self._pygame_image, True, False)

    def drawOnPosition(self, window: Window, position: Vector2F, x_flipped=False):
        rect = self._pygame_image.get_rect()
        rect.bottomleft = position
        if not x_flipped:
            window.screen.blit(self._pygame_image, rect)
        else:
            window.screen.blit(self._pygame_image_xmirror, rect)


class ImageSprite(DrawableInterface):
    def __init__(self, image: Image, position=(0.0, 0.0)):
        self.image = image
        self.position = position
        self.set_position(self.position)
        self.flipped = False

    def draw(self, window: Window):
        self.image.drawOnPosition(window, self.position, self.flipped)

    def move(self, vector: Vector2F):
        self.position += vector

    def set_position(self, vector: Vector2F):
        self.position = vector


class Font:
    def __init__(self, path: str):
        self.__pygame_font = pygame.font.Font(path, DEFAULT_FONT_SIZE)

    def render(self, text: str, antialias: bool, color, background):
        return self.__pygame_font.render(text, antialias, color, background)


class Animation:
    def __init__(self, images: List[Image], update_interval=0):
        self.frames = images
        self.update_interval = update_interval
        self.frame_number = 0
        self.last_update_time = Clock.get_time_from_init()

    @staticmethod
    def create_from_paths(paths: List[str], update_interval):
        return Animation(list(map(lambda path: Image(path), paths)), update_interval)

    def update(self):
        current_time = Clock.get_time_from_init()
        last_time = self.last_update_time
        if current_time - last_time > self.update_interval:
            self.frame_number += 1
            if self.frame_number == len(self.frames):
                self.frame_number = 0
            self.last_update_time = current_time

    def drawOnPosition(self, window: Window, position: Vector2F, flipped=False):
        self.frames[self.frame_number].drawOnPosition(window, position, flipped)

    def reset(self):
        self.frame_number = 0


class AnimationSprite(DrawableInterface):
    def __init__(self, animation: Animation, position=(0.0, 0.0)):
        self.animation = animation
        self.position = position
        self.flipped = False
        self.set_position(position)

    def draw(self, window: Window):
        self.animation.drawOnPosition(window, self.position, self.flipped)

    def move(self, vector: Vector2F):
        self.position += vector

    def set_position(self, vector: Vector2F):
        self.position = vector

    def update(self):
        self.animation.update()


class TextLabel(DrawableInterface):
    ALIGN_LEFT = 0b1000
    ALIGN_CENTER = 0b1100
    ALIGN_RIGHT = 0b0100
    VERTICAL_ALIGN_TOP = 0b0010
    VERTICAL_ALIGN_MIDDLE = 0b0011
    VERTICAL_ALIGN_BOTTOM = 0b0001

    def __init__(self, font: Font):
        self.position = (0, 0)
        self.font = font
        self.__pygame_drawable = font.render("", True, WHITE, BLACK)
        self.__pygame_rect = self.__pygame_drawable.get_rect()
        self.alignment = self.ALIGN_LEFT | self.VERTICAL_ALIGN_MIDDLE

    def set_text(self, text: str):
        self.__pygame_drawable = self.font.render(text, True, WHITE, BLACK)
        self.__pygame_rect = self.__pygame_drawable.get_rect()
        self.__pygame_rect.bottomleft = self.position

    def set_position(self, pos: Vector2F):
        x, y = pos
        self.position = int(x), int(y)
        self.__pygame_rect.bottomleft = self.position

    def set_alignment(self, alignment_flags):
        self.alignment = alignment_flags

    def __set_rect_position(self, position: Vector2F):
        if self.alignment == self.ALIGN_LEFT | self.VERTICAL_ALIGN_BOTTOM:
            self.__pygame_rect.bottomleft = position
        elif self.alignment == self.ALIGN_LEFT | self.VERTICAL_ALIGN_MIDDLE:
            self.__pygame_rect.midleft = position
        elif self.alignment == self.ALIGN_LEFT | self.VERTICAL_ALIGN_TOP:
            self.__pygame_rect.topleft = position
        elif self.alignment == self.ALIGN_RIGHT | self.VERTICAL_ALIGN_BOTTOM:
            self.__pygame_rect.bottomleft = position
        elif self.alignment == self.ALIGN_RIGHT | self.VERTICAL_ALIGN_MIDDLE:
            self.__pygame_rect.midleft = position
        elif self.alignment == self.ALIGN_RIGHT | self.VERTICAL_ALIGN_TOP:
            self.__pygame_rect.topleft = position
        elif self.alignment == self.ALIGN_CENTER | self.VERTICAL_ALIGN_MIDDLE:
            self.__pygame_rect.center = position
        else:
            raise Exception('TextLabel alignment value is not allowed')

    def draw(self, window: Window):
        window.screen.blit(self.font, self.__pygame_rect)

    def move(self, vector: Vector2F):
        self.__pygame_rect.move(vector)
