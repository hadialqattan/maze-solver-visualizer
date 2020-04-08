from time import sleep

# local import
from src.algorithms.base import BaseAlgorithm
from src.datastructures.datastructure import Queue, Node
from src.gui.dialog import ConfigurationDialog as report


class BFS(BaseAlgorithm):

    """
    Breadth First Search algorithm implementation.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def find_shortest_path(self, show: bool) -> list:
        """
        Find shortest path (BFS).

        :param show: if True, the algorithm will run with delay
        :type show: bool
        :returns: sulution list (positions) OR None if there's no solution
        :rtype: list
        """
        # create init node
        start_node = Node(state=self.start, parent=None)
        # init frontier (QUEUE)
        frontier = Queue()
        frontier.add(start_node)
        # init explored nodes set
        explored = set()

        # start BFS
        while not frontier.isempty() and self.run:

            # dequeue node from frontier
            node = frontier.remove()

            # mark as explored
            self.set_value(node.state, 3)
            # show sleep
            if show:
                sleep(0.03)

            # check if the node state equals target
            if node.state == self.target:
                # recolor start and target
                self.set_value(self.target, 5)
                self.set_value(self.start, 5)
                # init solution list
                solution = []
                # skip target node
                node = node.parent
                # backtrack to get the solution list
                while node.parent is not None:
                    # store solution tuple (movie_id, actor_id)
                    solution.append(node.state)
                    # mark solution path
                    self.set_value(node.state, 4)
                    # show sleep
                    if show:
                        sleep(0.03)
                    # move to the next parent
                    node = node.parent
                # reverse the solution
                solution.reverse()
                # distance report
                report.show_report(len(solution))
                # return the solution
                return solution

            # mark as explored
            explored.add(node)

            # search for neighbors
            for neighbor in self.get_neighbors(node.state):
                # check if the neighbor not in frontier and not explored
                if not frontier.isexist(neighbor) and neighbor not in [
                    i.state for i in explored
                ]:
                    # add the node to the frontier
                    frontier.add(Node(state=neighbor, parent=node))

        # no solution
        # distance report
        if frontier.isempty():
            report.show_report(0)
        return None
