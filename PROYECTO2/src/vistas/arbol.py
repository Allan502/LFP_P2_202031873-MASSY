import graphviz

class DerivationTreeGraph:
    def __init__(self, gramatica):
        self.graph = graphviz.Digraph(format='png')
        self.counter = 1
        self.gramatica=gramatica
        # Datos del árbol de derivación
        self.derivation_data = [
                    "*",
                    "X",
                    "X"
        ]

        
    def generate_tree(self, data):
        self._graph_derivation_tree(self.gramatica[3], self.derivation_data)
        self.graph.render('derivation_tree', view=True)

    def _graph_derivation_tree(self, parent_node, data):
        if isinstance(data, str):
            node_label = data
            self.graph.node(str(self.counter), label=node_label)
            if parent_node != '':
                self.graph.edge(parent_node, str(self.counter))
            self.counter += 1
        elif isinstance(data, list):
            for item in data:
                child_node = str(self.counter)
                self.graph.node(child_node)
                self.graph.edge(parent_node, child_node)
                self.counter = self._graph_derivation_tree(child_node, item)
        return self.counter


