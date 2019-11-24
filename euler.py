from collections import deque
import heapq
import itertools

class Graph:
    def __init__(self, nodes=None, edges=None):
        """Initialize a graph object.
        Args:
            nodes:  Iterator of nodes. Each node is an object.
            edges:  Iterator of edges. Each edge is a tuple of 2 nodes.
        """
        self.nodes, self.adj = [], {}
        if nodes != None:
            self.add_nodes_from(nodes)
        if edges != None:
            self.add_edges_from(edges)

    def __len__(self):
        """Returns the number of nodes in the graph.
        >>> g = Graph(nodes=[x for x in range(7)])
        >>> len(g)
        7
        """
        return len(self.nodes)

    def __contains__(self, x):
        """Return true if a node x is in the graph.
        >>> g = Graph(nodes=[x for x in range(7)])
        >>> 6 in g
        True
        >>> 7 in g
        False
        """
        return x in self.nodes

    def __iter__(self):
        """Iterate over the nodes in the graph.
        >>> g = Graph(nodes=[x for x in range(7)])
        >>> [x * 2 for x in g]
        [0, 2, 4, 6, 8, 10, 12]
        """
        return iter(self.nodes)

    def __getitem__(self, x):
        """Returns the iterator over the adjacent nodes of x.
        >>> g = Graph(nodes=[x for x in range(7)], edges=[(1,0), (1,2), (1,3)])
        >>> [x for x in g[1]]
        [0, 2, 3]
        """
        return iter(self.adj[x])

    def __str__(self):
        return 'V: %s\nE: %s' % (self.nodes, self.adj)

    def add_node(self, n):
        if n not in self.nodes:
            self.nodes.append(n)
            self.adj[n] = []

    def add_nodes_from(self, i):
        for n in i:
            self.add_node(n)

    def add_edge(self, u, v):   # undirected unweighted graph
        self.adj[u] = self.adj.get(u, []) + [v]
        self.adj[v] = self.adj.get(v, []) + [u]

    def add_edges_from(self, i):
        for n in i:
            self.add_edge(*n)

    def number_of_nodes(self):
        return len(self.nodes)

    def number_of_edges(self):
        return sum(len(l) for _, l in self.adj.items()) // 2

def __dfs_hierholzer(g, u, root, subpath, traversed):
    """Dfs on vertex u until get back to u. The argument vertices is a list and
    contains the vertices traversed. If all adjacent edges of starting vertex
    are already traversed, 'vertices' is empty after the call.
    """
    for v in g[u]:
        if (u,v) not in traversed or (v,u) not in traversed:
            traversed[(u,v)] = traversed[(v,u)] = True
            subpath.append(v)
            if v == root:
                return
            else:
                __dfs_hierholzer(g, v, root, subpath, traversed)


def hierholzer(g):
    """Find an Euler circuit on the given undirected graph if one exists.
    Args:
        g:  Undirected graph.
    Returns:
        List of vertices on the circuit or None if a circuit does not exist.
    # http://www.austincc.edu/powens/+Topics/HTML/06-1/ham2.gif
    # two triangles ABC and CDE
    >>> V = ['A', 'B', 'C', 'D', 'E']
    >>> E = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C','D'), ('C', 'E'), ('D', 'E')]
    >>> g = Graph(nodes=V, edges=E)
    >>> print(hierholzer(g))
    ['A', 'B', 'C', 'D', 'E', 'C', 'A']
    # V shape graph
    >>> print(hierholzer(Graph(nodes=[1,2,3], edges=[(1,2), (2,3)])))
    None
    """
    # Check if the graph has an Euler circuit: All vertices have even degrees.
    for u in g:
        if len(list(g[u])) % 2 == 1:
            return None

    # Create necessary data structures.
    start = next(g.__iter__())  # choose the start vertex to be the first vertex in the graph
    circuit = [start]           # can use a linked list for better performance here
    traversed = {}
    ptr = 0
    while len(traversed) // 2 < g.number_of_edges() and ptr < len(circuit):
        subpath = []            # vertices on subpath
        __dfs_hierholzer(g, circuit[ptr], circuit[ptr], subpath, traversed)
        if len(subpath) != 0:   # insert subpath vertices into circuit
            circuit = list(itertools.chain(circuit[:ptr+1], subpath, circuit[ptr+1:]))
        ptr += 1

        return circuit
V = ['A', 'B', 'C', 'D', 'E']
E = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C','D'), ('C', 'E'), ('D', 'E')]
g = Graph(nodes=V, edges=E)
print(hierholzer(g))
