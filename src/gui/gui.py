import pygame

# local import
from src.gui.grid import Grid
from src.gui.dialog import ConfigurationDialog
from src.thread.thread import Threads
from src.algorithms.a_star import AStar
from src.algorithms.bfs import BFS
from src.algorithms.dfs import DFS


class GUI:

    """
    GUI interface for maze solver visualizer.
    """

    def __init__(self):
        # get screen size based on current screen size
        screen_height = pygame.display.Info()
        self.BLOCKSIZE = int(screen_height.current_h * (1 / 50))
        screen_height = int(screen_height.current_h // (4 / 3))
        screen_height = screen_height - (screen_height % self.BLOCKSIZE)
        # set main pygame screen surface size
        self.__screen_size = (screen_height, screen_height)
        self.__screen = pygame.display.set_mode(self.__screen_size)
        # change dispalay icon
        pygame.display.set_icon(pygame.image.load("./assets/icon.png"))
        pygame.display.set_caption("Maze solver visualizer")
        # init grid
        self.__grid = Grid(self.__screen_size, self.__screen, self.BLOCKSIZE)
        # init thread managment class
        self.__threads = Threads()
        # running state
        self.__running = True
        # control FPS (30)
        clock = pygame.time.Clock()
        clock.tick(30)
        # screen theme
        self.__theme = True
        # show / hide grid stroke
        self.__grid_stroke = True
        # init algorithms
        args = (self.__grid.grid, self.__grid._start, self.__grid._target)
        self.__algorithms = (AStar(*args), BFS(*args), DFS(*args))
        # init current position
        self.__current_pos = (0, 0)
        # init configuration dialog
        self.__dialog = ConfigurationDialog()

    def __refresh(self):
        """
        Redraw the screen and update it.
        """
        while self.__running:
            color = (0, 0, 0) if self.__theme else (255, 255, 255)
            # set background color to black
            self.__screen.fill(color)
            # redraw the grid
            self.__grid.draw(self.__theme, self.__grid_stroke)
            # update the screen
            pygame.display.update()

    def loop(self):
        """
        Main gui loop.
        """
        # mouse state
        mouse_drag = False
        # draw walls
        draw_bool = True
        # eraser
        iseraser = False
        # init the dialog
        # self.__threads.start(self.__dialog.start, ())
        # start refresh thread
        self.__threads.start(self.__refresh, (), 0)
        # run Pygame events loop
        while self.__running:
            # listen to events
            for e in pygame.event.get():
                # close window button event
                if e.type == pygame.QUIT:
                    # stop running thread
                    self.__algorithms[self.__dialog.value].run = False
                    self.__running = False
                    self.__threads.join_all()

                # drawing events
                elif e.type == pygame.MOUSEBUTTONDOWN:
                    # set mouse state to drag
                    mouse_drag = True
                    # get current position
                    self.__current_pos = self.__get_current_position()
                    # check if current position equals start point or target point
                    if (
                        self.__current_pos == self.__grid.start
                        or self.__current_pos == self.__grid.target
                    ):
                        # set start bool
                        start = self.__current_pos == self.__grid.start
                        # disable drawing walls
                        draw_bool = False
                elif e.type == pygame.MOUSEBUTTONUP:
                    # reset mouse drag state
                    mouse_drag = False
                    # enable drawing walls
                    draw_bool = True
                elif e.type == pygame.MOUSEMOTION and mouse_drag:
                    # check if drawing walls enabled
                    if draw_bool:
                        # draw wall
                        self.__draw_by_mouse(iseraser)
                    else:
                        # move start/target position
                        self.__move_start_target(start)

                elif e.type == pygame.KEYDOWN:
                    # change theme shortcut
                    if e.key == pygame.K_t:
                        self.__theme = not self.__theme
                    # show/hide grid stroke
                    elif e.key == pygame.K_s:
                        self.__grid_stroke = not self.__grid_stroke
                    # quite
                    elif e.key == pygame.K_q:
                        self.__running = False
                        self.__threads.join_all()
                    # eraser
                    elif e.key == pygame.K_e:
                        iseraser = not iseraser
                    # show dialog
                    elif e.key == pygame.K_RETURN:
                        if self.__algorithms[self.__dialog.value].run:
                            # stop running thread
                            self.__algorithms[self.__dialog.value].run = False
                            self.__threads.join_by_id(1)
                            iseraser = False
                        # reset only non-wall blocks on the grid
                        self.__grid.reset(False)
                        # show dialog
                        self.__dialog.show()
                        # check if the dialog not canceled
                        if self.__dialog.run:
                            # start choosen algorithm
                            self.__algorithms[self.__dialog.value].run = True
                            self.__threads.start(
                                self.__algorithms[
                                    self.__dialog.value
                                ].find_shortest_path,
                                (bool(self.__dialog.shows.get()),),
                                1,
                            )
                            self.__dialog.run = False
                    # reset only non-wall blocks on the grid
                    elif e.key == pygame.K_SPACE:
                        # stop running thread
                        self.__algorithms[self.__dialog.value].run = False
                        self.__threads.join_by_id(1)
                        # reset only non-wall blocks on the grid
                        self.__grid.reset(False)
                        iseraser = False
                    elif e.key == pygame.K_BACKSPACE or e.key == pygame.K_DELETE:
                        # reset the entire grid
                        self.__grid.reset(True)
                        iseraser = False

    def __move_start_target(self, start: bool):
        """
        Move start / target position.

        :param start: set True if start position 
        :type start: bool
        """
        # get current position
        pos = self.__get_current_position()
        # move...
        if start and pos != self.__grid.target:
            self.__grid.set_value(self.__grid.start, 0)
            self.__grid.start = pos
        elif pos != self.__grid.start:
            self.__grid.set_value(self.__grid.target, 0)
            self.__grid.target = pos
        # set block value to two
        self.__grid.set_value(pos, 2)

    def __draw_by_mouse(self, iseraser: bool):
        """
        Draw maze by the mouse.

        :param iseraser: enable/disable erasing
        """
        # get current position
        pos = self.__get_current_position()
        # block coloring start/target positions
        if not pos == self.__grid.start and not pos == self.__grid.target:
            v = 0 if iseraser else 1
            # set block value to v
            self.__grid.set_value(pos, v)

    def __get_current_position(self) -> tuple:
        """
        Get current square position (x, y).

        :returns: current position (x, y)
        :rtype: tuple
        """
        # get mouse click poistion
        p = pygame.mouse.get_pos()
        # calulate square (x, y) from mouse position
        return p[0] // self.BLOCKSIZE, p[1] // self.BLOCKSIZE
