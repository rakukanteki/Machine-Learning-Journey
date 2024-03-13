class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None
    
    def add_child(self,data):
        data.parent = self
        self.children.append(data)
    
    def get_level(self):
        # Counting the number of ancestors.
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, choice):
        if choice == 'name':
            value = self.name
        elif choice == 'both':
            value = self.name + " (" + self.designation + " )"
        else:
            value = self.designation

        spaces = " "*self.get_level()*2
        prefix = spaces + "|__ " if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(choice)
    

def buildCompanyTree():
    root = TreeNode("Radwan", "CEO")

    infra = TreeNode("Tajim", "Infrasturture Head")
    infra.add_child(TreeNode("Anon", "Cloud Manager"))
    infra.add_child(TreeNode("Rahul", "App Manager"))
    appHead = TreeNode("Dibakar", "Application Head")
    cto = TreeNode("Aniruddha", "CTO")
    hr = TreeNode("Rifath","HR Head")
    hr.add_child(TreeNode("Sazid", "Recruitment Manager"))
    hr.add_child(TreeNode("Maksud", "Policy Manager"))

    cto.add_child(infra)
    cto.add_child(appHead)

    root.add_child(cto)
    root.add_child(hr)

    return root


if __name__ == "__main__":
    root = buildCompanyTree()
    root.print_tree("name")
    root.print_tree("designation")
    root.print_tree("both")