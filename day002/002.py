"""Practice with building trees"""
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = [] #essential to make it into a list or something that can be added into
        self.parent = None  #Declare a parent to go with children

    def add_tree_children(self, new_node):
        new_node.parent = self
        self.children.append(new_node)

    def print_tree_ugly(self):
        """Recursion to print all nodes in the tree but with no idents"""

        print(self.data)
        
        if self.children:
            for child in self.children:
                child.print_tree()
    
    def get_level(self):
        """Using the parent property, start the counter to determine the level(starts from the lowest node and count the parent to top level"""
        level = 0
        paren = self.parent
        while paren:
            level+=1
            paren = paren.parent 

        return level


    def print_tree_right_way(self):
        at_level = " " * self.get_level() * 3
        check_root_level = at_level + "|__" if self.parent else ""    #Ternary operator to not print the |__ for the root
        
        print (check_root_level + self.data)

        if self.children:
            for child in self.children:
                child.print_tree_right_way() #recursion here
    

def build_tree():
    root = TreeNode("My favorite dessert") #my root for the tree
    
    pudding = TreeNode("Pudding")
    pudding.add_tree_children(TreeNode("Banana Pudding"))
    pudding.add_tree_children(TreeNode("Chocolate Pudding"))
    pudding.add_tree_children(TreeNode("Flan"))

    ice_cream = TreeNode("Ice Cream")
    ice_cream.add_tree_children(TreeNode("Strawberry"))
    ice_cream.add_tree_children(TreeNode("Mango"))

    cake = TreeNode("Cake")
    cake.add_tree_children(TreeNode("Bundt Cake"))
    cake.add_tree_children(TreeNode("Chocolate Cake"))

    root.add_tree_children(pudding)
    root.add_tree_children(ice_cream)
    root.add_tree_children(cake)

    return root


if __name__ == "__main__":
    test_tree = build_tree()

    test_tree.print_tree_right_way()




