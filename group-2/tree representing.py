class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self, level=0):
        result = "  " * level + self.data + "\n"
        for child in self.children:
            result += child.__str__(level + 1)
        return result

def construct_tree(book_structure):
    root = TreeNode("Book")
    for chapter, sections in book_structure.items():
        chapter_node = TreeNode("Chapter " + str(chapter))
        root.add_child(chapter_node)
        for section, subsections in sections.items():
            section_node = TreeNode("Section " + str(section))
            chapter_node.add_child(section_node)
            for subsection in subsections:
                subsection_node = TreeNode("Subsection " + str(subsection))
                section_node.add_child(subsection_node)
    return root

def print_nodes(root):
    print(root)

# Example book structure
book_structure = {
    1: {1: [1, 2], 2: [1, 2]},
    2: {1: [1, 2], 2: [1, 2]},
    3: {1: [1, 2], 2: [1, 2]},
}

# Construct the tree
root_node = construct_tree(book_structure)

# Print the nodes
print_nodes(root_node)

