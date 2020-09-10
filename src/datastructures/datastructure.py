from collections import deque


class Node:

    """
    Node implementation for(BFS-DFS).

    :param state: node state (x, y)
    :type state: tuple
    :param parent: Node instance
    :type parent: Node
    """

    def __init__(self, state: tuple, parent):
        self.state = state
        self.parent = parent


class ASNode(Node):

    """
    A* Node implementation for(A*)

    child :: (Node)
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.g = 0
        self.h = 0
        self.f = 0


class Stack:

    """
    Stack implementation.
    """

    def __init__(self):
        self.list = deque([])

    def add(self, node: Node):
        """
        Add new element into list.

        :param node: Node object to add
        :type node: Node
        """
        self.list.append(node)

    def remove(self) -> Node:
        """
        Remove and return element from list.

        :returns: last in element
        :rtype: Node
        """
        return self.list.pop()

    def isempty(self) -> bool:
        """
        Is the list empty?

        :returns: True if the list is empty otherwise False
        :rtype: bool
        """
        return len(self.list) == 0

    def isexist(self, state: int) -> bool:
        """
        Is the state exist on the list?

        :param state: state to check
        :type state: int
        :returns: True if exist otherwise False
        :rtype: bool
        """
        return any(node.state == state for node in self.list)


class Queue(Stack):

    """
    Queue implementation.

    child :: (Stack)
    """

    def remove(self) -> Node:
        """
        Remove and return element from list.

        :returns: last in element
        :rtype: Node
        """
        return self.list.popleft()


class OpenList:

    """
    A* open list implementation.
    """

    def __init__(self):
        self.list = []

    def lowest_cost(self, node: ASNode) -> tuple:
        """
        Get the lowest cost node.

        :param node: current node to compare
        :type node: ASNode
        :returns: lowst node, current index
        """
        currentindex = 0
        # iterate over open list elements
        for index, lnode in enumerate(self.list):
            # get lower cost node
            if lnode.f < node.f:
                node = lnode
                currentindex = index
        return node, currentindex

    def add(self, node: ASNode):
        """
        Add new element into list.

        :param node: Node object to add
        :type node: Node
        """
        self.list.append(node)

    def front(self) -> ASNode:
        """
        Return list front element.

        :returns: front node element
        :rtype: ASNode
        """
        return self.list[0]

    def remove(self, index: int):
        """
        Remove element from list.

        :param index: index to remove
        :type index: int
        """
        self.list.pop(index)

    def isempty(self) -> bool:
        """
        Is the list empty?

        :returns: True if the list is empty otherwise False
        :rtype: bool
        """
        return len(self.list) == 0

    def isexist(self, state: int, g: int) -> bool:
        """
        Is the state exist on the list?

        :param state: state to check
        :type state: int
        :param g: g value
        :type g: int
        :returns: True if exist otherwise False
        :rtype: bool
        """
        return any(node.state == state for node in self.list if g > node.g)
