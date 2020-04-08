from unittest import TestCase

# local import
from src.datastructures.datastructure import Node, ASNode, Stack, Queue, OpenList


class DatastructureTests(TestCase):

    """
    Datastructures unit tests.
    """

    def __init__(self, *args, **kwargs):
        super(DatastructureTests, self).__init__(*args, **kwargs)

    def test_01_Node(self):
        """
        Test Node.
        """
        # init nodes
        root_node = Node((0, 0), None)
        node = Node((1, 1), root_node)
        # get state
        assert root_node.state == (0, 0)
        # get parent
        assert node.parent == root_node
        # get parent state
        assert node.parent.state == (0, 0)

    def test_02_ASNode(self):
        """
        Test ASNode (A* Node).
        """
        # init nodes
        root_node = Node((0, 0), None)
        # set values
        root_node.g = 10
        root_node.h = 5
        root_node.f = root_node.g + root_node.h
        node = Node((1, 1), root_node)
        node.g = node.parent.g + 10
        node.h = 3
        node.f = node.g + node.h
        # check values
        assert root_node.g == 10
        assert root_node.h == 5
        assert root_node.f == 15
        assert node.g == 20
        assert node.h == 3
        assert node.f == 23

    def test_03_Stack(self):
        """
        Test Stack.
        """
        # init
        stack = Stack()
        # check isempty
        assert stack.isempty() == True
        # add elements
        n1 = Node((0, 0), None)
        n2 = Node((1, 1), n1)
        n3 = Node((2, 2), n2)
        stack.add(n1)
        stack.add(n2)
        stack.add(n3)
        # check isempty
        assert stack.isempty() == False
        # check isexist
        assert stack.isexist((0, 0)) == True
        # remove last in
        assert stack.remove() == n3

    def test_04_Queue(self):
        """
        Test Queue.
        """
        # init
        queue = Queue()
        # check isempty
        assert queue.isempty() == True
        # add elements
        n1 = Node((0, 0), None)
        n2 = Node((1, 1), n1)
        n3 = Node((2, 2), n2)
        queue.add(n1)
        queue.add(n2)
        queue.add(n3)
        # check isempty
        assert queue.isempty() == False
        # check isexist
        assert queue.isexist((0, 0)) == True
        # remove first in
        assert queue.remove() == n1

    def test_05_OpenList(self):
        """
        Test OpenList.
        """
        # init open list
        open_list = OpenList()
        # check isempty
        assert open_list.isempty() == True
        # add nodes
        n1 = ASNode((0, 0), None)
        n1.g = 1
        n1.h = 2
        n1.f = n1.g + n1.h
        n2 = ASNode((1, 1), n1)
        n2.g = n1.g + 3
        n2.h = 4
        n2.f = n2.g + n2.h
        n3 = ASNode((2, 2), n2)
        n3.g = n2.g + 5
        n3.h = 6
        n3.f = n3.g + n3.h
        open_list.add(n1)
        open_list.add(n2)
        open_list.add(n3)
        # check isempty
        assert open_list.isempty() == False
        # check isexist
        assert open_list.isexist((0, 0), 10) == True
        # get lowest cost
        assert open_list.lowest_cost(n3) == (n1, 0)
        # get list front
        assert open_list.front() == n1
        # remove by index
        open_list.remove(1)
        assert len(open_list.list) == 2
