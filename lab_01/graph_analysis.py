import networkx as nx
import matplotlib.pyplot as plt


class ChicagoRegionalGraph():

    def __init__(self):
        self.graph = nx.DiGraph()

        self.read_file_and_populate(
            self.graph, "utility/tntp-ChicagoRegional/out.tntp-ChicagoRegional")

        self.vertices = len(self.graph.nodes)
        self.edges = len(self.graph.edges)
        self.max_deg_in = self.node_max_degree("input")
        self.max_deg_out = self.node_max_degree("output")

    def read_file_and_populate(self, graph, filename):
        '''
        This function reads the network file and populates a given directed graph 
        '''
        with open(filename) as file:

            count = 0

            while True:
                count += 1

                # Get next line from file
                line = file.readline().strip()

                # if line is empty
                # end of file is reached
                if not line:
                    break

                args = list(line.split())
                graph.add_edge(args[0], args[1])

    def node_max_degree(self, mode):
        '''
        This function returns the maximum input/output degree of a node in the graph.

        Input: (string) "input" for entering nodes or "output" for exiting nodes

        Output: (int) The maximum degree among all nodes in the graph
        '''

        max_deg = 0

        if mode == "input":

            for node in self.graph.nodes:
                node_deg = len(self.graph.in_edges(node))
                if node_deg > max_deg:
                    max_deg = node_deg

        elif mode == "output":

            for node in self.graph.nodes:
                node_deg = len(self.graph.out_edges(node))
                if node_deg > max_deg:
                    max_deg = node_deg

        else:
            raise ValueError(
                "Mode inserted is wrong.\nAccepted modes are: 'input' or  'output' (strings)\n")

        return max_deg

    def get_degrees_list(self, mode):
        '''
        This function returns a list of the degrees of each node in the graph

        Input: (string) "input" for entering nodes or "output" for exiting nodes

        Output: (list) list of the degrees of each node in the graph
        '''
        deg_list = []
        if mode == "input":

            for node in self.graph.nodes:
                node_deg = len(self.graph.in_edges(node))
                deg_list.append(node_deg)

        elif mode == "output":

            vertex_deg_counter = [0] * self.max_deg_out

            for node in self.graph.nodes:
                node_deg = len(self.graph.out_edges(node))
                deg_list.append(node_deg)

        else:
            raise ValueError(
                "Mode inserted is wrong.\nAccepted modes are: 'input' or  'output' (strings)\n")

        return deg_list

    def get_betweeness(self, node):
        pass


def degree_distribution(graph, mode, filetitle, title, xlabel, ylabel):
    '''
    This function creates and save a fig with the histogram of the distribution

    Input: (string) "input" for entering nodes or "output" for exiting nodes

    Output: (list) Number of nodes with degree == position in list
            output[3] is the number of nodes with degree 3
    '''

    if mode == "input":
        max_deg = CG.max_deg_in

    elif mode == "output":
        max_deg = CG.max_deg_out

    plt.hist(CG.get_degrees_list(mode), bins=2*max_deg)
    plt.xticks(ticks=[x+0.25 for x in range(0, max_deg)],
               labels=[x for x in range(0, max_deg)])

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(axis='y', color='r', linestyle='-', linewidth=.5)
    plt.savefig(filetitle)


if __name__ == "__main__":

    CG = ChicagoRegionalGraph()

    print(f"The number of vertices in the graph is V = {CG.vertices}")
    print(f"The number of edges in the graph is M = {CG.edges}")
    print(
        f"The max degree for entering edges found is MAX_IN = {CG.max_deg_in}")
    print(
        f"The max degree for exiting edges found is MAX_IN = {CG.max_deg_out}")

    # degree_distribution(CG, 'input', 'degrees_distribution_hist',
    #                     'Distribution of nodes degree', 'Node degree', '# of nodes')
