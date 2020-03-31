from union_find import UnionFind

class Percolation :

    # Creates n-by-n grid, with all sites initially blocked
    # 0 -> n*n-1    : nodes in he grid  (close)
    # n*n           : false top         (open)
    # n*n+1         : false bottom      (open)
    def __init__(self, n) :
        self.grid   = [False for i in range(n*n)] + [True, True]
        self.uf_arr = UnionFind(n*n+2)
        self.size   = n
        self.opened = 0


    # Returns the index from row and column
    def get_index(self, row, col) :
        return (row*self.size) + col

    # Checks if two sites are open and merges them
    def check_and_merge(self, i, j) :
        if self.grid[i] and self.grid[j] :
            self.uf_arr.union(i, j)
            return True
        return False

    # Opens the site (row, col) if it is not open already
    def open(self,row, col) :
        index   = self.get_index(row, col)
        if self.grid[index] :
            return
        self.opened += 1
        self.grid[index] = True
        # Handling rows
        if row == 0 :
            self.check_and_merge(index, self.size*self.size)
            self.check_and_merge(index, index+self.size)
        elif row == self.size-1 :
            self.check_and_merge(index, self.size*self.size+1)
            self.check_and_merge(index, index-self.size)
        else :
            self.check_and_merge(index, index-self.size)
            self.check_and_merge(index, index+self.size)
        # Handling columns
        if col == 0 :
            self.check_and_merge(index, index+1)
        elif col == self.size-1 :
            self.check_and_merge(index, index-1)
        else :
            self.check_and_merge(index, index-1)
            self.check_and_merge(index, index+1)


    # Is the site (row, col) open?
    def isOpen(self, row, col) :
        return self.grid[self.get_index(row, col)]

    # Is the site (row, col) full?
    def isFull(self, row, col) :
        return self.uf_arr.find(self.get_index(row, col), self.size*self.size) or self.uf_arr.find(self.get_index(row, col), self.size*self.size+1)

    # Returns the number of open sites
    def numberOfOpenSites(self) :
        return self.opened

    # Does the system percolate?
    def percolates(self) :
        return self.uf_arr.find(self.size*self.size, self.size*self.size+1)
