class Node:

    def __init__(self, board):
        self.data = board
        self.children = []
        self.parent = None

    def print_tree(self):
        self.data.print_board()
        print()
        for child in self.children:
            print()
            child.print_tree()