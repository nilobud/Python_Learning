import pygame
import random

pygame.init()

screenWidth = 500
screenHeight = 500
done = False

display = pygame.display.set_mode((screenWidth, screenHeight))

clock = pygame.time.Clock()

bg = pygame.image.load('background.png')
speed = 0

boat = pygame.image.load('boat.png')
waveImage = pygame.image.load('wave.png')

wavesList = []

for i in range(6):
  x = random.randrange(0, screenWidth)
  y = random.randrange(183, screenHeight)
  wavesList.append([x,y])

while not done:
  display.blit(bg, (0, 0))
  
  pos = list(pygame.mouse.get_pos())

  if pos[1] < 183:
    pos[1] = 183

  display.blit(boat, (pos[0]-25, pos[1]-25))

  for i in range(len(wavesList)):
    wave = display.blit(waveImage, wavesList[i])

    wavesList[i][0] -= 1 + speed

    if wavesList[i][0] < -68:
      x = screenWidth+5
      y = random.randrange(183, screenHeight)
      wavesList[i][0] = x
      wavesList[i][1] = y
    
    collide = wave.collidepoint(pos)

    if collide == True:
      print('OH NO! your ship has sunk!')
      done = True

  speed += 0.009
  clock.tick(30)
  pygame.display.update()
  pygame.event.get()