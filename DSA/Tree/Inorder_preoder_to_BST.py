class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildTree(inorder, preorder, inorder_start, inorder_end):
    # Base case.
    if inorder_start > inorder_end:
        return None
    
    # Taking 0th index of preoder list as root.
    root = Node(preorder[buildTree.preIndex])
    # Then incrementing the preoder list index.
    buildTree.preIndex += 1

    # If current node doesn't have any children.
    if inorder_start == inorder_end:
        return root

    # Find the index of the root in inorder list.
    root_index = findPosition(inorder, inorder_start, inorder_end, root.data)

    # Construct left sub tree.
    root.left = buildTree(inorder, preorder, inorder_start, root_index-1)
    # Construct right sub tree.
    root.right = buildTree(inorder, preorder, root_index+1, inorder_end)

    return root


def findPosition(inOrder, start, end, element):
    for i in range(start, end+1):
        if inOrder[i] == element:
            return i
    return -1


def postorder_traversal(root):
    if root is None:
        return 
    else:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data, end=" ")


if __name__ == "__main__":
    inorder_list = ['D','B','E','A','F','C']
    preorder_list = ['A','B','D','E','C','F']
    # Static variable preIndex.
    buildTree.preIndex = 0
    root = buildTree(inorder_list, preorder_list, 0, len(inorder_list)-1)

    print(f"Final constructed tree: ")
    postorder_traversal(root)

