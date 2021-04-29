import pygame
import sys
from random import randint

# Constants
SCREEN_SIZE = WIDTH, HEIGHT = (1280, 720)


# Initialization
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Epidemic Simulator 1.0")
fps = pygame-time.Clock()
pause = False

# Create people
main_people_list = [Person(randint(50, WIDTH-50), randint(50, HEIGHT-50)) for i in range(10)]

# Main program
while True:
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame-quit()
            sys.exit()
        if event.type == pygame.KEYDOWEN:
              if event.key == pygame.K_SPACE:
                    pause = not pause
  if not pause:
      pass     
