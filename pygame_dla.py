import pygame_menu
import pygame
import main
from main import DLA

pygame.init()
width = 1000
height = 800
screen = pygame.display.set_mode((width, height))
FPS = 60

pygame.mixer.init()
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.display.set_caption("Diffusion-limited aggregation")
clock = pygame.time.Clock()


class Model(DLA,  pygame.sprite.Sprite):
    def __init__(self, X, Y):
        super(Model, self).__init__(X, Y)
        pygame.sprite.Sprite.__init__(self)
        super(Model,self).generator(d_min=0, d_max=6)
        print(self.r)
        min = self.r
        super().circle()
        for i in range(self.Y):
            for j in range(self.X):
                if self.field[i][j] == 1:
                    self.particle = pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(j * 50, i * 50, 50, 50))

        self.particle.centerx = width / 2
        self.particle.bottom = height - 10
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
            self.speedy = 0
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
            self.speedy = 0
        if keystate[pygame.K_UP]:
            self.speedx = 0
            self.speedy = -8
        if keystate[pygame.K_DOWN]:
            self.speedx = 0
            self.speedy = +8

        self.particle.x += self.speedx
        self.particle.y += self.speedy

        if self.particle.right > width:
            self.particle.right = height
        if self.particle.left < 0:
            self.particle.left = 0
        if self.particle.y < 0:
            self.particle.y = 0
        if self.particle.y > height:
            self.particle.y = 0
def game():
    all_sprites = pygame.sprite.Group()
    first_model = Model(25, 25)
    first_model.generator(0,6)
    all_sprites.add(first_model)
    # Цикл игры
    running = True
    while running:
        # Держим цикл на правильной скорости
        clock.tick(FPS)
        # Ввод процесса (события)
        for event in pygame.event.get():
            # проверка для закрытия окна
            if event.type == pygame.QUIT:
                running = False

        # Обновление
        all_sprites.update()

        # Рендеринг
        screen.fill(BLACK)
        all_sprites.draw(screen)
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()
def menu():

    menu = pygame_menu.Menu('Welcome', 400, 400,
                            theme=pygame_menu.themes.THEME_BLUE)

    menu.add.button('Start', game())
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)

menu()
pygame.quit()