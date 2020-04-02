import  random
import  pygame, sys
from    time            import sleep
from    pygame.locals   import *
from    percolation     import Percolation

from config import WINDOW_LENGTH, COVERED_SITE_LENGTH, COVERED_PADDING_LENGTH
from config import COLOR_OPEN, COLOR_CLOSED, COLOR_FILLED
from config import SLEEP_TIME

# Returns the (row,col) tuple for given index and size of grid
def get_row_col(i, n) :
    return (i//n, i%n)

# Percolation sim order and chaos
size = int(input("Enter size of percolation grid: "))
if size == 1 :
    print('100% duh!')
    exit()
percolation = Percolation(size)
random_order = [i for i in range(size*size)]
random.shuffle(random_order)

# Display initialization
pygame.init()
window_size = (WINDOW_LENGTH, WINDOW_LENGTH)
DISPLAYSURF = pygame.display.set_mode(window_size)
pygame.display.set_caption('Percolation')

# Simulation configurations
site_size       = COVERED_SITE_LENGTH/size
padding         = COVERED_PADDING_LENGTH/size
occupied_space  = ((site_size*size)+((size-1)*padding))
gapx            = (window_size[0] - occupied_space)/2
gapy            = (window_size[1] - occupied_space)/2
sites           = [None for i in range(size*size)]

iteration = -1
last_loop = False
while True:
    # main game loop
    if percolation.percolates() :
        opened = percolation.numberOfOpenSites()
        print('opened sites:', opened)
        print('percetage opened:', opened*100/size/size,'%')
        last_loop = True

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if iteration >= 0 :
        next_open   = get_row_col(random_order[iteration], size)
        percolation.open(next_open[0], next_open[1])

    for index in range(size*size) :
        (row,col) = get_row_col(index, size)
        color = COLOR_OPEN
        if sites[index] is None :
            x = gapx+col*(site_size+padding)
            y = gapx+row*(site_size+padding)
            sites[index] = pygame.Rect(x, y, site_size, site_size)
        if not percolation.isOpen(row, col) :
            color = COLOR_CLOSED
        elif percolation.isFull(row, col) :
            color = COLOR_FILLED
        pygame.draw.rect(DISPLAYSURF, color, sites[index])


    iteration += 1
    sleep(SLEEP_TIME)
    if last_loop :
        break
    if not last_loop :
        pygame.display.update()

input("\nPress return to exit!")
