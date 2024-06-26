import pygame, sys

# from pygame.sprite import Group

# pause = False
# for event in pygame.event.get():
#     if event.type == pygame.KEYDOWN:
#         # if event.key == pygame.K_ESCAPE:     
#         if event.key == pygame.K_ESCAPE:
#             if pause:
#                 pause =False
#             else:
#                 pause = True

running = True
class obj (pygame.sprite.Sprite):
    def __init__(self, pos_x , pos_y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('trash11.png')) #single move
        self.sprites.append(pygame.image.load('trash21.png'))
        self.sprites.append(pygame.image.load('trash31.png'))
        self.sprites.append(pygame.image.load('trash41.png'))
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        # self.image = pygame.Surface([20,20])
        # self.image.fill((255,255,255))

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x , pos_y]
    def update(self):
        self.current_sprite += 1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        key = pygame.key.get_pressed()
        if key[pygame.K_p]:
            self.pause()

    def pause(self):
        global running
        isPause = True
        while isPause:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        isPause = False
                if event.type == pygame.QUIT:
                    isPause = False
                    running = False

pygame.init()
clock = pygame.time.Clock()

screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("TEST")

moving_sprites = pygame.sprite.Group()
obj1 = obj(100,100)
moving_sprites.add(obj1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(1) #FPS