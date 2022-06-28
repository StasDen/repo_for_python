from movies_binary_tree import Tree, Node


def main():
    bt = Tree()

    root = Node(5)  # Root
    root.left = Node(3, "Interstellar", 2014, 3, "science fiction", "Paramount Pictures")
    root.right = Node(4, "Forrest Gump", 1994, 2, "tragicomedy", "Paramount Pictures")
    root.left.left = Node(0, "The Lord of Rings: The Fellowship of the Ring", 2001, 3, "adventure", "New Line Cinema")
    root.left.right = Node(8, "Shutter island", 2010, 2, "thriller", "Paramount Pictures")
    root.left.right.left = Node(2, "The Lord of Rings: The Two Towers", 2002, 3, "adventure", "New Line Cinema")

    bt.add(5, root)
    bt.add(3, root.left)
    bt.add(4, root.right)
    bt.add(0, root.left.left)
    bt.add(8, root.left.right)
    bt.add(2, root.left.right.left)

    print("------------------------")

    bt.print_tree()

    print("------------------------")

    print(bt.find(3))
    print(bt.find(10))

    print("------------------------")

    # Printing bt
    print("Original node:")
    bt.pre_order(root)

    # Deleting specified node
    result = bt.delete_node(root, 3)

    # Checking bt
    print("After deleting:")
    bt.pre_order(result)

    print("------------------------")

    result = bt.delete_nodes_with_same_studio(root, root.left.right, "Paramount Pictures")

    print("After deleting movies with the same studio:")
    bt.pre_order(result)

    print("------------------------")

    print("Movies with the same genre:")
    bt.print_nodes_with_same_genre(result, "adventure")

    print("------------------------")

    # Deleting bt
    bt.delete_tree()

    # Checking binary tree
    bt.print_tree()


if __name__ == '__main__':
    main()
