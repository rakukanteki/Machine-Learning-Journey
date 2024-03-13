class TreeNode:
    def __init__(self, country):
        self.country = country
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self,level):
        if self.get_level() > level:
            return
        spaces = " "*self.get_level()*3
        prefix = spaces + "|__ " if self.parent else ""
        print(prefix + self.country)
        if self.children:
            for child in self.children:
                child.print_tree(level)


def buildCountryTree():
    Globe = TreeNode("Global")

    # Bangladesh
    raj = TreeNode("Rajshahi")
    raj.add_child(TreeNode("Natore"))
    raj.add_child(TreeNode("Pabna"))

    dhaka = TreeNode("Dhaka")
    dhaka.add_child(TreeNode("Madaripur"))
    dhaka.add_child(TreeNode("Munshiganj"))

    bd = TreeNode("Bangladesh")
    bd.add_child(raj)
    bd.add_child(dhaka)

    # USA
    NJ = TreeNode("New Jersey")
    NJ.add_child(TreeNode("Princeton"))
    NJ.add_child(TreeNode("Torento"))

    Cali = TreeNode("California")
    Cali.add_child(TreeNode("San Francisco"))
    Cali.add_child(TreeNode("Mountain View"))
    Cali.add_child(TreeNode("Palo Alto"))

    usa = TreeNode("USA")
    usa.add_child(NJ)
    usa.add_child(Cali)

    Globe.add_child(bd)
    Globe.add_child(usa)
    
    return Globe


if __name__ == "__main__":
    root = buildCountryTree()
    root.print_tree(2)