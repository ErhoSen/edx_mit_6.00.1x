class Member(object):
    def __init__(self, founder):
        """ 
        founder: string
        Initializes a member. 
        Name is the string of name of this node,
        parent is None, and no children
        """        
        self.name = founder
        self.parent = None         
        self.children = []    

    def __str__(self):
        return self.name    

    def add_parent(self, mother):
        """
        mother: Member
        Sets the parent of this node to the `mother` Member node
        """
        self.parent = mother   

    def get_parent(self):
        """
        Returns the parent Member node of this Member
        """
        return self.parent 

    def is_parent(self, mother):
        """
        mother: Member
        Returns: Boolean, whether or not `mother` is the 
        parent of this Member
        """
        return self.parent == mother  

    def add_child(self, child):
        """
        child: Member
        Adds another child Member node to this Member
        """
        self.children.append(child)   

    def is_child(self, child):
        """
        child: Member
        Returns: Boolean, whether or not `child` is a
        child of this Member
        """
        return child in self.children 


class Family(object):
    def __init__(self, founder):
        self.names_to_nodes = {}
        self.root = Member(founder)    
        self.names_to_nodes[founder] = self.root   

    def set_children(self, mother, list_of_children):
        mom_node = self.names_to_nodes[mother]
        for c in list_of_children:
            c_member = Member(c)
            self.names_to_nodes[c] = c_member
            c_member.add_parent(mom_node)
            mom_node.add_child(c_member)         
    
    def is_parent(self, mother, kid):
        mom_node = self.names_to_nodes[mother]
        child_node = self.names_to_nodes[kid]
        return child_node.is_parent(mom_node)   

    def is_child(self, kid, mother):
        mom_node = self.names_to_nodes[mother]
        child_node = self.names_to_nodes[kid]
        return mom_node.is_child(child_node)

    def cousin(self, a, b, cousin_type = 0, degree_removed = 0):
        node_a = self.names_to_nodes[a]
        node_b = self.names_to_nodes[b]
        if node_a == node_b:
            return (-1, 0)

        def get_parent(child_node):
            ### RETURN PARENT NODE FOR child_node
            if child_node == self.root:
                return None
            stack = [self.root]
            temp = stack.pop()
            while True:
                if self.is_child(child_node.name, temp.name):
                    return temp
                else:
                    stack += temp.children
                    temp = stack.pop()

        def find_depth(node, depth = -2):
            if node == None:
                return depth
            else:
                return find_depth(get_parent(node), depth+1)

        return (min(find_depth(node_a), find_depth(node_b)), abs(find_depth(node_a) - find_depth(node_b)))



f = Family("a")
f.set_children("a", ["b", "c"])
f.set_children("b", ["d", "e"])
f.set_children("c", ["f", "g"])

f.set_children("d", ["h", "i"])
f.set_children("e", ["j", "k"])
f.set_children("f", ["l", "m"])
f.set_children("g", ["n", "o", "p", "q"])

words = ["zeroth", "first", "second", "third", "fourth", "fifth", "non"]

## These are your test cases. 

## The first test case should print out:
## 'b' is a zeroth cousin 0 removed from 'c'


t, r = f.cousin("f", "c")
print "'f' is a", words[t], "cousin", r, "removed from 'c'"
