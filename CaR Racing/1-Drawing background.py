import pygame
pygame.init()

w_width = 500 
w_height = 500
window = pygame.display.set_mode((w_width, w_height))
pygame.display.set_caption("Car race")

# game variables
clock = pygame.time.Clock()

# drawing on the window surface
def DrawInGameLoop():
    clock.tick(60)
    window.fill("gray")
    pygame.display.flip()

# load and play music
pygame.mixer.music.load("sounds/music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.6)

# game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    DrawInGameLoop()

pygame.quit()

