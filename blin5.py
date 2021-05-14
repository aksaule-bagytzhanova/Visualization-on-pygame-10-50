import pygame, sys
from colour import Color

x=150
y=410

x1 = 250
y1 = 180
def bouncing_rect():
    global x_speed, y_speed, other_speed
    
    other_rect.y += other_speed
    if other_rect.top <= 190 or other_rect.bottom >= 500:
        other_speed *= -1

def bouncing_rect1():
    global x_speed, y_speed, other_speed
    
    other_rect1.y -= other_speed
    if other_rect1.top <= 190 or other_rect1.bottom >= 500:
        other_speed *= -1


    pygame.draw.rect(screen, (255,255,255), other_rect)
    pygame.draw.rect(screen, (255,255,255), other_rect1)

pygame.init()
clock = pygame.time.Clock()
screen_width,screen_height = 500, 500
screen = pygame.display.set_mode((screen_width,screen_height))

other_rect = pygame.Rect(170,350,50,50)
other_rect1 = pygame.Rect(270,300,50,50)
other_speed = 1



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((16711935))
    
    
    
    pygame.draw.aalines(screen, (255,255,255), False,
                    [[200, 150], [200, 500]])
    pygame.draw.aalines(screen, (255,255,255), False,
                    [[300, 150], [300, 500]])
    
    pygame.draw.rect(screen, (16711935), (0,0,400,150))
    pygame.draw.rect(screen, (255,255,255), (190,80,120,10))
    pygame.draw.aalines(screen, (255,255,255), False,
                    [[250, 80], [250, 170]])
    pygame.draw.rect(screen, (255,255,255), other_rect)
    pygame.draw.rect(screen, (255,255,255), other_rect1)
    pygame.draw.circle(screen, (255,255,255), 
                   (250,150), 50)   
    
    bouncing_rect()   
    bouncing_rect1()
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
