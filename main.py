from MyGame import MyGame

app = MyGame()
app.run()

# import sys
# from Application import Window, Image, Sprite, TextLabel, ImageSprite, Font
#
# size = width, height = 1200, 900
# window = Window(size)
#
# fps_counter_position = (width-150, 50)
# speed = [2.0, 2.0]
#
# # screen = pygame.display.set_mode(size)
#
# # ball = pygame.image.load("asset/ball.gif")
# # ballrect = ball.get_rect()
#
# ball_image = Image("asset/ball.gif")
# ball_sprite = ImageSprite(ball_image)
#
# roboto_font = Font("asset/Roboto-Regular.ttf")
# fps_counter_label = TextLabel(roboto_font)
#
# fps_counter_label.set_text("Hello")
# fps_counter_label.set_position(fps_counter_position)
#
# # font = pygame.font.Font("asset/Roboto-Regular.ttf", 16)
# # fpsTextSprite = TextSprite(font)
# # fpsTextSprite.set_text("dsadasdsa")
# # fpsTextSprite.set_position(fps_counter_position)
#
#
# # fps_text = font.render("FPS COUNTER", True, white, black)
# # fps_rect = fps_text.get_rect()
# # fps_rect.center = (width-150, 50)
#
# # clock = pygame.time.Clock()
# counter = 0
#
# player_x = 100.0
# player_y = 100.0
# x_moving_speed = 1.0
# y_moving_speed = 1.0
#
# fps = 0
#
# # def getFpsCounter(counter):
# #     text = font.render(str(counter), True, white, black)
# #     rect = text.get_rect()
# #     rect.center = (width-150, 50)
# #     return text, rect
#
# while True:
#     # for event in pygame.event.get():
#     #     if event.type == pygame.QUIT: sys.exit()
#
#     # keys = pygame.key.get_pressed()
#     #
#     # if  keys[pygame.K_w]:
#     #     player_y -= y_moving_speed
#     # if keys[pygame.K_s]:
#     #     player_y -= y_moving_speed
#     # if  keys[pygame.K_a]:
#     #     player_x -= x_moving_speed
#     # if  keys[pygame.K_d]:
#     #     player_x -= y_moving_speed
#
#     # spriteRect = ballSprite.move((speed[0], speed[1]))
#     # if spriteRect.left < 0 or spriteRect.right > width:
#     #     speed[0] = -speed[0]
#     # if spriteRect.top < 0 or spriteRect.bottom > height:
#     #     speed[1] = -speed[1]
#
#     # clock.tick()
#     # counter += 1
#     # if counter % 100 == 0:
#     #     fps = clock.get_fps()
#     #
#     # fpsTextSprite.set_text(str(round(fps)))
#
#     window.clear()
#     window.draw(ball_image)
#     window.draw(fps_counter_label)
#     # window.draw(fpsTextSprite)
#     Window.display()
