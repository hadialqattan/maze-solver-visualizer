from time import sleep

# local import
from src.algorithms.base import BaseAlgorithm
from src.datastructures.datastructure import OpenList, ASNode
from src.gui.dialog import ConfigurationDialog as report


class AStar(BaseAlgorithm):

    """
    A* algorithm implementation.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def find_shortest_path(self, show: bool) -> list:
        """
        Find shortest path (A*).

        :param show: if True, the algorithm will run with delay
        :type show: bool
        :returns: sulution list (positions) OR None if there's no solution
        :rtype: list
        """
        # create init node
        start_node = ASNode(state=self.start, parent=None)
        start_node.g = start_node.h = start_node.f = 0
        # init open list
        open_list = OpenList()
        open_list.add(start_node)
        # init closed list
        closed_list = set()

        # start A* searching
        while not open_list.isempty() and self.run: 
            
            # get the current node
            current_node = open_list.front()
            current_index = 0

            # show sleep
            if show: 
                sleep(0.03)

            # iterate over open list elements
            current_node, current_index = open_list.lowest_cost(current_node)
        
            # pop current from open list, add to closed list
            open_list.remove(current_index)
            closed_list.add(current_node)

            # found the goal
            if current_node.state == self.target: 
                # recolor start and target
                self.set_value(self.target, 5)
                self.set_value(self.start, 5)
                # init solution list
                solution = []
                # skip target node
                current_node = current_node.parent
                # backtrack to get the solution list
                while current_node.parent is not None:
                    # store solution tuple (movie_id, actor_id)
                    solution.append(current_node.state)
                    # mark solution path
                    self.set_value(current_node.state, 4)
                    # show sleep
                    if show:
                        sleep(0.05)
                    # move to the next parent
                    current_node = current_node.parent
                # reverse the solution
                solution.reverse()
                # distance report
                report.show_report(len(solution))
                # return the solution
                return solution

            # search for neighors
            for neighbor in self.get_neighbors(current_node.state): 
                # skip neighbor in the closed list
                if neighbor in [i.state for i in closed_list]: 
                    continue
                # create new node
                node = ASNode(state=neighbor, parent=current_node)
                # calculate f, g, h values
                node.g = current_node.g + 1
                node.h = ((neighbor[0] - self.target[0])**2) + ((neighbor[1] - self.target[1])**2)
                node.f = node.g + node.h 
                # check if the node already in the open list
                if open_list.isexist(node.state, node.g): 
                    continue
                # mark as explored
                self.set_value(node.state, 3)
                # add the node to the open list
                open_list.add(node)

        # no solution
        # distance report
        if open_list.isempty():
            report.show_report(0)
        return None
