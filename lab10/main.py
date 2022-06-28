from movies_binary_tree import Tree, Node


def main():
    bt = Tree()

    root = Node(5)  # Root(default node)
    root.left = Node(3, "Interstellar", 2014, 3, "science fiction", "Paramount Pictures")
    root.right = Node(6, "Forrest Gump", 1994, 2, "tragicomedy", "Paramount Pictures")

    root.left.left = Node(2, "The Lord of Rings: The Fellowship of the Ring", 2001, 3, "adventure", "New Line Cinema")
    root.left.right = Node(4, "Shutter island", 2010, 2, "thriller", "Paramount Pictures")

    root.left.right.right = Node(7, "The Lord of Rings: The Two Towers", 2002, 3, "adventure", "New Line Cinema")

    print("Added nodes:")
    bt.add(5, root)
    bt.add(3, root.left)
    bt.add(6, root.right)
    bt.add(2, root.left.left)
    bt.add(4, root.left.right)
    bt.add(7, root.left.right.right)

    print("------------------------")

    # Printing bt
    bt.print_tree()

    print("------------------------")

    print("Founded nodes:")
    print(bt.find(3))
    print(bt.find(10))

    print("------------------------")

    # Printing bt
    print("Original bt:")
    bt.preorder(root)

    # Deleting specified node
    result = bt.delete_node(root, 2)  # Method returning root

    print("After deleting specified node:")
    bt.preorder(result)

    print("------------------------")

    # Using the same root 'result'
    result = bt.delete_nodes_with_same_studio(root, root.left.right.right, "New Line Cinema")

    print("After deleting movies with the same studio:")
    bt.preorder(result)

    print("------------------------")

    print("Movies with the same genre:")
    bt.print_nodes_with_same_genre(result, "tragicomedy")

    print("------------------------")

    # Deleting bt
    bt.delete_tree()

    print("Bt after deletion:")
    bt.print_tree()


if __name__ == '__main__':
    main()
