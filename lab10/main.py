from movies_binary_tree import Tree, Node


def main():
    # Creating binary tree
    bt = Tree()

    # Creating some nodes
    n1 = Node(3, "Interstellar", 2014, 3, "science fiction", "Paramount Pictures")
    n2 = Node(4, "Forrest Gump", 1994, 2, "tragicomedy", "Paramount Pictures")
    n3 = Node(0, "The Lord of Rings: The Fellowship of the Ring", 2001, 3, "adventure", "New Line Cinema")
    n4 = Node(8, "Shutter island", 2010, 2, "thriller", "Paramount Pictures")
    n5 = Node(2, "The Lord of Rings: The Two Towers", 2002, 3, "adventure", "New Line Cinema")

    # Adding nodes
    bt.add(3, n1)
    bt.add(4, n2)
    bt.add(0, n3)
    bt.add(8, n4)
    bt.add(2, n5)

    print("------------------------")  # Printing line for better reading the output

    bt.print_tree()

    print("------------------------")

    # Printing the output of find function
    print(bt.find(3))
    print(bt.find(10))

    print("------------------------")

    # Deleting nodes with the same movie studio
    print(bt.delete_nodes_with_same_studio(n1, 3, "Paramount Pictures"))

    # Deleting exact node
    print(bt.delete_node(n4, 8))
    bt.print_tree()

    print("------------------------")

    bt.print_nodes_with_same_genre("adventure")

    print("------------------------")

    # Deleting bt
    bt.delete_tree()

    # Checking binary tree
    bt.print_tree()


if __name__ == '__main__':
    main()
