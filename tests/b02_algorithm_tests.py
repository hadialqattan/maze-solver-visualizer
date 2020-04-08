from unittest import TestCase
from unittest.mock import MagicMock, patch
from sys import modules

# mock dialog (tkinter)
modules["tkinter"] = MagicMock()
modules["ConfigurationDialog"] = MagicMock()

# local import
from src.algorithms.base import BaseAlgorithm
from src.algorithms.a_star import AStar
from src.algorithms.bfs import BFS
from src.algorithms.dfs import DFS


class AlgorithmTests(TestCase):

    """
    Algorithms unit tests.
    """

    def __init__(self, *args, **kwargs):
        super(AlgorithmTests, self).__init__(*args, **kwargs)

    def test_01_BaseAlgorithm(self):
        """
        Test BaseAlgorithm (Parent class of all algorithms classes).
        """
        # init 20*20 grid
        grid = [[0 for i in range(20)] for j in range(20)]
        # init base class
        base = BaseAlgorithm(grid, (1, 1), (19, 19))
        # set wall
        for i in range(10):
            # tests set value
            base.set_value((i, 10), 1)
            assert grid[i][10] == 1
        # get neighbors
        assert base.get_neighbors((1, 1)) == [
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 0),
            (1, 2),
            (2, 0),
            (2, 1),
            (2, 2),
        ]
        # get behind the walls
        assert base.get_neighbors((4, 9)) == [(3, 8), (3, 9), (4, 8), (5, 8), (5, 9)]
        # test casting
        assert type(base.start) == type(base.target) == tuple

    @patch("ConfigurationDialog.show_report")
    def test_02_AStar(self, mock):
        """
        Test AStar (A*).
        """
        # mock report.show_report
        mock.return_value = None
        # init 20*20 grid
        grid = [[0 for i in range(20)] for j in range(20)]
        # init base class
        astar = AStar(grid, (1, 1), (19, 19))
        astar.run = True
        # set wall
        for i in range(10):
            # tests set value
            astar.set_value((i, 10), 1)
        # get the solution (there's a solution)
        assert astar.find_shortest_path(False) == [(i, i) for i in range(2, 19)]
        # split the grid
        for i in range(20):
            # tests set value
            astar.set_value((i, 10), 1)
        # get the solution (no solution)
        assert astar.find_shortest_path(False) == None

    @patch("ConfigurationDialog.show_report")
    def test_03_BFS(self, mock):
        """
        Test BFS (Breadth-first search).
        """
        # mock report.show_report
        mock.return_value = None
        # init 20*20 grid
        grid = [[0 for i in range(20)] for j in range(20)]
        # init base class
        bfs = BFS(grid, (1, 1), (19, 19))
        bfs.run = True
        # set wall
        for i in range(10):
            # tests set value
            bfs.set_value((i, 10), 1)
        # get the solution (there's a solution)
        assert bfs.find_shortest_path(False) == [(i, i) for i in range(2, 19)]
        # split the grid
        for i in range(20):
            # tests set value
            bfs.set_value((i, 10), 1)
        # get the solution (no solution)
        assert bfs.find_shortest_path(False) == None

    @patch("ConfigurationDialog.show_report")
    def test_04_DFS(self, mock):
        """
        Test DFS (Depth-first search).
        """
        # mock report.show_report
        mock.return_value = None
        # init 20*20 grid
        grid = [[0 for i in range(20)] for j in range(20)]
        # init base class
        dfs = DFS(grid, (1, 1), (19, 19))
        dfs.run = True
        # set wall
        for i in range(10):
            # tests set value
            dfs.set_value((i, 10), 1)
        # get the solution (there's a solution)
        assert dfs.find_shortest_path(False) == [(i, i) for i in range(2, 19)]
        # split the grid
        for i in range(20):
            # tests set value
            dfs.set_value((i, 10), 1)
        # get the solution (no solution)
        assert dfs.find_shortest_path(False) == None
