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
        self.n = self.__size[0] // self.BLOCKSIZE
        # init the grid (empty grid)
        self.grid = [
            [0 for i in range(self.n)] for j in range(self.n)
        ]
        # set start / target 
        self.__start = [1, 1]
        self.__target = [self.n-2, self.n-2]
        self.grid[1][1] = 2
        self.grid[self.n-2][self.n-2] = 2

    @property
    def _start(self) -> list: 
        """
        start property getter.

        :returns: start position
        :rtype: list
        """
        return self.__start

    @property
    def start(self) -> tuple: 
        """
        start property getter.

        :returns: start position
        :rtype: tuple
        """
        return tuple(self.__start)

    @start.setter
    def start(self, position: tuple): 
        """
        start property setter.

        :param position: new start position 
        :type position: tuple
        """
        self.__start[0] = position[0]
        self.__start[1] = position[1]

    @property
    def _target(self) -> list: 
        """
        target property getter.

        :returns: target position
        :rtype: list
        """
        return self.__target

    @property
    def target(self) -> tuple: 
        """
        target property getter.

        :returns: target position
        :rtype: tuple
        """
        return tuple(self.__target)
    
    @target.setter 
    def target(self, position: tuple): 
        """
        target property setter

        :param position: new start position
        :rtype position: tuple
        """
        self.__target[0] = position[0]
        self.__target[1] = position[1]

    def reset(self, _all: bool): 
        """
        Reset the grid.

        :param _all: set all to reset the entire grid
        :type _all: bool
        """
        if _all: 
            # reset the grid (empty grid)
            for x in range(self.n): 
                for y in range(self.n): 
                    self.grid[x][y] = 0
        else: 
            # reset only non-wall block
            for x in range(self.n): 
                for y in range(self.n):
                    if self.grid[x][y] != 1: 
                        self.grid[x][y] = 0
        # relocate start and target
        self.set_value(self.start, 2)
        self.set_value(self.target, 2)

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
        else: 
            fill = (55, 55, 55)
            stroke = (0, 0, 0)
        # iterate over all rows
        for x in range(self.n): 
            # iterate over all columns
            for y in range(self.n): 
                # create rect
                rect = pygame.Rect(x*self.BLOCKSIZE, y*self.BLOCKSIZE, self.BLOCKSIZE, self.BLOCKSIZE)
                if grid_stroke:
                    # draw rect (stroke)
                    pygame.draw.rect(self.__screen, stroke, rect, 1)
                if self.grid[x][y] == 1: 
                    # draw rect (fill)(wall)
                    pygame.draw.rect(self.__screen, fill, rect)
                elif self.grid[x][y] == 2:
                    # draw rect (fill)(start-target)
                    pygame.draw.rect(self.__screen, (51, 51, 204), rect)
                elif self.grid[x][y] == 3: 
                    # draw rect (fill)(explored & frontiered)
                    pygame.draw.rect(self.__screen, (51, 204, 51), rect)
                elif self.grid[x][y] == 4: 
                    # shortest path member
                    pygame.draw.rect(self.__screen, (51, 51, 204), rect)
                elif self.grid[x][y] == 5:
                    # found target
                    pygame.draw.rect(self.__screen, (204, 51, 51), rect)
    
    def set_value(self, pos: tuple, value: int):
        """
        Set block value by position. 

        :param pos: block position (x, y)
        :type pos: tuple
        :param value: block value
        :type value: int
        """
        self.grid[pos[0]][pos[1]] = value
