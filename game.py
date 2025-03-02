import pygame
import random
pygame.init()

# Screen
screen = pygame.display.set_mode((700, 800))
pygame.display.set_caption('Flappy Bird')

# Functions
Font = pygame.font.SysFont(None, 55)
def draw_text(text, font, colour, x, y):
    img = font.render(text, True, colour)
    screen.blit(img, (x, y))

# Loading images
BG = pygame.image.load('bg.png').convert_alpha()
BG = pygame.transform.scale(BG, (700, 700))
Ground = pygame.image.load('ground.png').convert_alpha()
Ground = pygame.transform.scale(Ground, (735, 100))

# Variables
Fps = 60
clock = pygame.time.Clock()
ground_scroll = 0
scroll_speed = 4
gravity = 0.3
bird_vel = 0
bird_x = 40
bird_y = 30
jump = -8
pipe_gap = 150
pipe_x = 600
pipe_y = 290
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency
Score = 0

# Define ground rectangle
ground_rect = pygame.Rect(0, 700, 700, 100)


# Classes
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Pipe.png")
        self.rect = self.image.get_rect()
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y + int(pipe_gap / 2)]
        if position == -1:
            self.rect.topleft = [x, y + int(pipe_gap / 2)]

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('bird1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
        self.velocity = 0

    def update(self):
        self.velocity += gravity
        self.rect.y += self.velocity
        if self.rect.top < 0 or self.rect.colliderect(ground_rect):
            import Fail

    def jump(self):
        self.velocity = jump

Bird_class = Bird(40, 60)
Bird_group = pygame.sprite.Group()
Bird_group.add(Bird_class)
pipe_group = pygame.sprite.Group()

# While loop
run = True
while run:
    time_now = pygame.time.get_ticks()
    if time_now - last_pipe > pipe_frequency:
        Score += 1
        pipe_height = random.randint(-100, 100)
        btm_pipe = Pipe(700, (570 / 2) + pipe_height, -1)
        top_pipe = Pipe(700, (290 / 2) + pipe_height, 1)
        pipe_group.add(btm_pipe)
        pipe_group.add(top_pipe)
        last_pipe = time_now

    # Drawing elements
    screen.blit(BG, (0, 0))
    screen.blit(Ground, (ground_scroll, 700))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) >= 35:
        ground_scroll = 0
    pipe_group.draw(screen)
    pipe_group.update()
    Bird_group.draw(screen)
    Bird_group.update()
    draw_text(str(Score), Font, (255, 255, 255), 100,100)
    if pygame.sprite.groupcollide(Bird_group, pipe_group, False, False):
        import Fail
    pygame.display.update()

    # Settings Fps
    clock.tick(Fps)

    # For loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            Bird_class.jump()

pygame.quit()