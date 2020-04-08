

class BaseAlgorithm:

    """
    Base algorithms class.

    :param grid: maze grid.
    :type grid: list
    :param start: start position (x, y)
    :type start: list
    :param target: target position (x, y)
    :type target: list
    """

    def __init__(self, grid: list, start: list, target: list):
        self.grid = grid
        self.grid_len = len(self.grid)
        self.run = False
        self.__start = start
        self.__target = target

    @property
    def start(self) -> tuple: 
        """
        start property getter.

        :returns: start position
        :rtype: tuple
        """
        return tuple(self.__start)
    
    @property
    def target(self) -> tuple: 
        """
        target property getter.

        :returns: target position
        :rtype: tuple
        """
        return tuple(self.__target)

    def find_shortest_path(self, show: bool):
        """
        Find shortest path (algorithm name).

        :param show: if True, the algorithm will run with delay
        :type show: bool
        """
        raise NotImplementedError

    def get_neighbors(self, statepos: tuple) -> list:
        """
        Get state neighbors.

        :param statepos: state position to get neighbors (x, y)
        :type state: tuple
        :returns: list of all state neighbors [(x, y)]
        :rtype: list

        Actions map : 

            # up neighbors
            (-1, -1), (-1, 0), (-1, +1)
            # middle neighbors
            (0, -1), (current), (0, +1)
            # down neighbors
            (+1, -1), (+1, 0), (+1, +1)

        """
        # calculate neighbors
        subs = (
            # up neighbors
            (-1, -1),
            (-1, 0),
            (-1, +1),
            # middle neighbors
            (0, -1),
            (0, +1),
            # down neighbors
            (+1, -1),
            (+1, 0),
            (+1, +1),
        )
        # get neighbors
        neighbors = []
        for x, y in subs: 
            # calculate neghbor position
            nx, ny = statepos[0] + x, statepos[1] + y 
            # check if the neghbor in grid length range
            if (-1 < nx < self.grid_len 
                and -1 < ny < self.grid_len 
                and self.grid[nx][ny] != 1): 
                # append the neighbor
                neighbors.append((nx, ny))
        return neighbors

    def set_value(self, pos: tuple, value: int):
        """
        Set block value by position. 

        :param pos: block position (x, y)
        :type pos: tuple
        :param value: block value
        :type value: int
        """
        self.grid[pos[0]][pos[1]] = value
