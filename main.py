import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('Setup End')

print('Loop start')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # close window
            quit()  # end in pygame
