
#Main program
#imports knight tour class fro knight_tour
#imports pygame to use with the GUI. pygame includes graphics and sound libraries
#imports sys to get system specific access

from knight_tour import KnightTour
import pygame 
import sys


#background of the window function
def draw_background():
    screen.fill(blackTileColor)
    for i in range(board_size[0]):
        for j in range(board_size[1]):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, whiteTileColor, (tileSize * j, tileSize * i, tileSize, tileSize), 0)
            pygame.draw.circle(screen, knightTileColor,
                               (tileSize * j + tileSize // 2, tileSize * i + tileSize // 2), tileSize // 4, 0)


#function for the kinghts path 
def draw_line(start, end):
    pygame.draw.line(screen, lineColor,
                     (tileSize * start[1] + tileSize // 2, tileSize * start[0] + tileSize // 2),
                     (tileSize * end[1] + tileSize // 2, tileSize * end[0] + tileSize // 2), 10)

#board size and window size
board_size = (6, 6)
screenSizeX = 800
screenSizeY = 800


if screenSizeX // board_size[1] >= screenSizeY // board_size[0]:
    tileSize = screenSizeY // board_size[0]
else:
    tileSize = screenSizeX // board_size[1]

#loads knights tour using pygame graphics and sound libraries
knight_tour = KnightTour(board_size=board_size)
pygame.init()
screen = pygame.display.set_mode((tileSize * board_size[1], tileSize * board_size[0]))
clock = pygame.time.Clock()
fps = 1

#Colors of the tiles and lines
whiteTileColor = (245, 245, 245)
blackTileColor = (100, 100, 100)
visitedTileColor = (153, 51, 51)
knightTileColor = (255, 102, 102)
lineColor = (255, 102, 102)

#executes the background function
draw_background()

skip = True
runUpdate = True
even = False
time = 0
while True:
    iterations = 0
    knight_tour.initialize_neurons()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    runUpdate = False

                if event.key == pygame.K_q:
                    fps += 1
                if event.key == pygame.K_a:
                    fps -= 1
                    if fps == 0:
                        fps = 1
        if runUpdate:
            num_of_active, num_of_changes = knight_tour.update_neurons()
            draw_background()
            for vertex_set in knight_tour.get_active_neurons_vertices():
                vertex1, vertex2 = vertex_set
                draw_line(vertex1, vertex2)

            if num_of_changes == 0:
                break

            if knight_tour.check_degree():
                even = True
                break
            iterations += 1
            if iterations == 20:
                break
    time += 1
    if even:
        print('all vertices have degree=2')
        if knight_tour.check_connected_components():
            print('solution found!!')
            knight_tour.get_solution()
            runUpdate = False
        else:
            even = False

        pygame.display.set_caption("Knight\'s Tour " + str(fps) + "fps")
        pygame.display.update()
        msElapsed = clock.tick(fps)
