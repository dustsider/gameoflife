import pygame, sys
from grid import Grid
from simulation import Simulation

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE = 750, 750, 25
FPS = 12

#Colors
GREY = (29, 29, 28)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

clock = pygame.time.Clock()
#variables
simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)


#simulation loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row = pos[1] // CELL_SIZE
            column = pos[0] // CELL_SIZE
            simulation.toggle_cell(row, column)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                simulation.start()
                pygame.display.set_caption("Game of Life is running")
            elif event.key == pygame.K_d:
                FPS +=2
            elif event.key == pygame.K_a:
                if FPS > 5: 
                    FPS-=2
                if FPS < 1:
                    FPS = 1
            elif event.key == pygame.K_r:
                simulation.create_random_state()
            elif event.key == pygame.K_c:
                simulation.clear()
            elif event.key == pygame.K_SPACE:
                simulation.stop()
                pygame.display.set_caption("Game of Life has stopped")
            
    #update simulation
    simulation.update()
    
    #draw window/grid
    window.fill(GREY)
    simulation.draw(window)
    pygame.display.update()
    clock.tick(FPS)