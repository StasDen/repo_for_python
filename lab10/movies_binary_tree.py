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

        # Key
        self.value = value

        # Children
        self.right = None
        self.left = None

    # Representing our node obj
    def __str__(self) -> str:
        return (f"'{self.name}' was released in {self.release_year}. Duration: {self.duration_in_hours} hours."
                f" It's {self.genre} from '{self.studio}'")


# Binary tree
class Tree:

    # Initializing our tree
    def __init__(self) -> None:
        self.root = None  # Necessary root

    # Adding nodes to bt
    def add(self, value: int, node: Node) -> None:
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(value, self.root)

        print(f"{node} - node has been added")

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

    # Finding tree node
    def find(self, value: int) -> int | None:

        # Finding elements in our bt if only bt root exists
        if self.root is not None:
            if (found_value := self._find(value, self.root)) is not None:  # Returning value only if node is not None
                return found_value.value
            else:
                return None
        else:
            return None

    def _find(self, value: int, node: Node) -> Node:
        if value == node.value:

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

    # Printing bt
    def print_tree(self) -> None:
        print("Binary tree:")

        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node: Node) -> None:

        # Rendering binary tree
        if node is not None:
            self._print_tree(node.left)
            print(node.value)
            self._print_tree(node.right)

    # Deleting node
    def delete_node(self, root: Node, key: int) -> Node | None:
        if not root:
            return None

        # If key less than value - deleting left node
        if root.value > key:
            root.left = self.delete_node(root.left, key)

        # If key is bigger than value - deleting right node
        elif root.value < key:
            root.right = self.delete_node(root.right, key)

        # If key = node value
        else:

            # Checking node for right/left child
            if not root.right:
                return root.left
            if not root.left:
                return root.right

            # If both children exist
            temp_val = root.right
            min_val = temp_val.value
            while temp_val.left:
                temp_val = temp_val.left
                min_val = temp_val.value

            # Deleting min right node
            root.right = self.delete_node(root.right, root.value)

        return root

    # Printing all the nodes(bt)
    def pre_order(self, node: Node) -> None:
        if not node:
            return None

        # If node exists
        print(node.value)

        # Doing so for right/left children
        self.pre_order(node.left)
        self.pre_order(node.right)

    # Deleting movies(nodes) with the same studio using 'delete_node' method
    def delete_nodes_with_same_studio(self, root: Node, node_ex: Node, studio: str) -> Node | None:
        if not root:
            return None

        if node_ex.studio == studio:
            self.delete_node(root, node_ex.value)
        else:
            print("There aren't movies with the same studio")

        # Using recursion
        self.delete_nodes_with_same_studio(root.right, node_ex, studio)
        self.delete_nodes_with_same_studio(root.left, node_ex, studio)

        return root

    # Printing movies with the same genre
    def print_nodes_with_same_genre(self, root: Node, genre: str) -> None:
        if not root:
            return None

        if root.genre == genre:
            print(root.value)

        # Doing so for right/left children
        self.print_nodes_with_same_genre(root.left, genre)
        self.print_nodes_with_same_genre(root.right, genre)
