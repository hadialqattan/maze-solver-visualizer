import pygame 


class Grid: 

    """
    maze solver GUI grid implementation.

    :param size: screen size (width, height)
    :type size: tuple
    :param screen: pygame screen
    :type screen: pygame.Surface
    :param BLOCKSIZE: grid block size
    :type BLOCKSIZE: int
    """

    def __init__(self, size: tuple, screen: pygame.Surface, BLOCKSIZE: int):
        self.__size = size
        self.__screen = screen 
        self.BLOCKSIZE = BLOCKSIZE
        # get row/column square count
        n = self.__size[0] // self.BLOCKSIZE
        # init the grid (empty grid)
        self.grid = [
            [0 for i in range(n)] for j in range(n)
        ]
        self.n = len(self.grid)

    def draw(self, theme: bool, grid_stroke: bool): 
        """
        Draw the grid.

        :param theme: screen theme
        :type there: bool
        :param grid_stroke: show/hide grid stroke
        :type grid_stroke: bool
        """
        # set colors based on the theme
        if theme:
            fill = (255, 255, 255)
            stroke = (200, 200, 200)
            target = (51, 204, 51)
        else: 
            fill = (55, 55, 55)
            stroke = (0, 0, 0)
            target = (51, 51, 204)
        # iterate over all rows
        for x in range(self.n): 
            # iterate over all columns
            for y in range(self.n): 
                # create rect
                rect = pygame.Rect(x*self.BLOCKSIZE, y*self.BLOCKSIZE, self.BLOCKSIZE, self.BLOCKSIZE)
                if self.grid[x][y] == 1: 
                    # draw rect (fill)
                    pygame.draw.rect(self.__screen, fill, rect)
                elif self.grid[x][y] == 2: 
                    # draw rect (start-end)
                    pygame.draw.rect(self.__screen, target, rect)
                if grid_stroke:
                    # draw rect (stroke)
                    pygame.draw.rect(self.__screen, stroke, rect, 1)
    
    def set_value(self, pos: tuple, value: int):
        """
        Set block value by position. 

        :param pos: block position (x, y)
        :type pos: tuple
        :param value: block value
        :type value: int
        """
        self.grid[pos[0]][pos[1]] = value
