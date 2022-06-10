# Node
class Node:

    # Initializing our node
    def __init__(self, value: int, name: str = "film", release_year: int = 2010, duration_in_hours: int = 1,
                 genre: str = "epic", studio: str = "Universal Pictures") -> None:
        self.name = name
        self.release_year = release_year
        self.duration_in_hours = duration_in_hours
        self.genre = genre
        self.studio = studio

        # Value
        self.value = value

        # Children
        self.right = None
        self.left = None

    # Representing our node obj
    def __str__(self) -> str:
        return (f"'{self.name}' was released in {self.release_year}. Duration: {self.duration_in_hours} hours."
                f" It's {self.genre} from {self.studio}")


# Binary tree
class Tree:

    # Initializing our tree
    def __init__(self) -> None:
        self.root = None  # Necessary root

    # Adding nodes to bt(logic)
    def add(self, value: int, node: Node) -> None:
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(value, self.root)

        print(f"{node} - node has been added")

    # Adding nodes to bt(realization)
    def _add(self, value: int, node: Node) -> None:

        # Left node here
        if value < node.value:
            if node.left is not None:
                self._add(value, node.left)  # Using recursion
            else:
                node.left = Node(value)  # If there isn't left node - creating it

        # Right node
        else:
            if node.right is not None:
                self._add(value, node.right)
            else:
                node.right = Node(value)

    # Finding tree node(logic)
    def find(self, value: int):
        if self.root is not None:  # Finding elements in our bt if only bt root exists
            self._find(value, self.root)
        else:
            return None

    # Finding tree node(realization)
    def _find(self, value: int, node: Node) -> Node:
        if value == node.value:
            print(f"{node} - found node")

            return node

        # Left node
        elif value < node.value and node.left is not None:
            return self._find(value, node.left)  # Recursion

        # Right node
        elif value > node.value and node.right is not None:
            return self._find(value, node.right)

    # Deleting tree
    def delete_tree(self) -> None:
        self.root = None  # Garbage collector will do this for us

    # Printing bt(logic)
    def print_tree(self) -> None:
        print("Binary tree")

        if self.root is not None:
            self._print_tree(self.root)

    # Printing bt(realization)
    def _print_tree(self, node: Node) -> None:

        # Rendering binary tree
        if node is not None:
            self._print_tree(node.left)
            print(node.value)
            self._print_tree(node.right)

    # Deleting node
    @staticmethod
    def successor(node: Node) -> int:  # Successor of node
        node = node.right

        while node.left:
            node = node.left

        return node.value

    @staticmethod
    def predecessor(node: Node) -> int:  # Predecessor of node
        node = node.left

        while node.right:
            node = node.right

        return node.value

    # Main deleting func(using 'successor' and 'predecessor' functions here)
    def delete_node(self, node: Node, key: int) -> None | str:
        if not node:
            return None

        # Deleting right node
        if key > node.value:
            node.right = self.delete_node(node.right, key)  # Using recursion

        # Deleting left node
        elif key < node.value:
            node.left = self.delete_node(node.left, key)

        else:

            # If our node is a leaf
            if not node.left or node.right:
                node = None

            # If our node has right child
            elif node.right:

                node.value = self.successor(node)  # Changing our tree
                node.right = self.delete_node(node.right, node.value)

            # If our node has left child
            else:
                node.value = self.predecessor(node)
                node.left = self.delete_node(node.left, node.value)

        return f"{node} - node has been deleted"

    # Deleting nodes(movies) with the same studio
    def delete_nodes_with_same_studio(self, node: Node, key: int, studio: str) -> None | str:
        if studio == node.studio:  # Checking if node's studios are the same

            # Then using our 'delete_node()' method
            if not node:
                return None

            # Deleting right node
            if key > node.value:
                node.right = self.delete_node(node.right, key)  # Using recursion

            # Deleting left node
            elif key < node.value:
                node.left = self.delete_node(node.left, key)

            else:

                # If our node is a leaf
                if not node.left or node.right:
                    node = None

                # If our node has right child
                elif node.right:

                    node.value = self.successor(node)  # Changing our tree
                    node.right = self.delete_node(node.right, node.value)

                # If our node has left child
                else:
                    node.value = self.predecessor(node)
                    node.left = self.delete_node(node.left, node.value)

        # If there aren't any appropriate nodes - printing info about it
        else:
            print("There aren't movies with the same studio")

        return f"{node} - node with the same movie studio has been deleted"

    # Printing movies with the same genre
    def print_nodes_with_same_genre(self, genre: str) -> None:
        pass
