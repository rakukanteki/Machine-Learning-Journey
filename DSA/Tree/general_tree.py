class TreeNode:
    # Constructor.
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self  # self is a parent of child.
        self.children.append(child)

    def get_level(self):
        # Counting the number of ancestors.
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level


    def print_tree(self):
        spaces = " "*self.get_level()*2
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("ASUS TUF F15"))
    laptop.add_child(TreeNode("Lenovo"))
    laptop.add_child(TreeNode("ASUS ROG"))

    cellphone = TreeNode("Cell Phones")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Xiaomi"))
    cellphone.add_child(TreeNode("Samsung"))

    tv =  TreeNode("TV")
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("SONY"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    # print(tv.get_level())
    return root


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
    # print(root.get_level())