class Node:
    def __init__(self, parent = None):
        self.parent = parent

        self.number = None
        self.left = None
        self.right = None


    def setnumber(self, number):
        self.number = number


class Tree:
    def __init__(self, height):
        self.height = height
        self.root = Node()
        self.counter = 1
        self.found = []
        bottomnodes = [self.root]


        while height > 1:
            height -= 1
            nodes = []

            for node in bottomnodes:
                node.left = Node(node)
                node.right = Node(node)

                nodes.append(node.left)
                nodes.append(node.right)

            bottomnodes = nodes

        self.__assign()


    def __assign(self, root = False):
        if root == False: root = self.root
        
        if root != None:
            self.__assign(root.left)
            self.__assign(root.right)

            root.setnumber(self.counter)
            self.counter += 1


    def find(self, number, root = False):
        if root == False: root = self.root

        if root != None:
            self.find(number, root.left)
            self.find(number, root.right)

            if root.number == number:
                if root.parent != None: self.found.append(root.parent.number)
                else: self.found.append(-1)


def solution(h, q):
    tree = Tree(h)
    for converter in q: tree.find(converter)
    return tree.found
