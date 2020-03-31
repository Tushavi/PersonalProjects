# TODO: Improve performance, see lines 30 and 34
#       In union method, attach the node requested directly as well, apart from its root
class UnionFind :

    # constructor and initialiser of the object, id-ing all nodes to themselves
    def __init__(self, num_nodes) :
        self.ids        = [x for x in range(num_nodes)]
        self.num_nodes  = num_nodes
        self.sizes      = [1]*num_nodes

    # returns the root of a node
    def root(self, node) :
        x = node
        if self.ids[node] == node :
            return x
        sizex = self.sizes[node]
        while x != self.ids[x] :
            x = self.ids[x]
            self.sizes[x] -= sizex
        self.ids[node] = x
        self.sizes[x] += sizex
        return x

    def union(self, a, b) :
        root_a = self.root(a)
        root_b = self.root(b)
        if root_a == root_b :
            return
        if self.sizes[root_a] >= self.sizes[root_b] :
            self.ids[root_b] = self.ids[root_a]
            # self.ids[b] = self.ids[root_a]
            self.sizes[root_a] += self.sizes[root_b]
        else :
            self.ids[root_a] = self.ids[root_b]
            # self.ids[a] = self.ids[root_b]
            self.sizes[root_b] += self.sizes[root_a]

    # Checks if 2 nodes are connected or not
    # Just compare the roots of the 2 nodes
    def find(self, a, b) :
        if self.root(a) == self.root(b) :
            return True
        else :
            return False
