import graphviz

class DerivationTreeGraph:
    def __init__(self, gramatica):
        self.graph = graphviz.Digraph(format='png')
        self.counter = 0
        self.gramatica=gramatica
        
    def generate_tree(self):
        #self._graph_derivation_tree(self.gramatica[3], self.gramatica[4])
        hijos=[Nodo("1",[Nodo("2"),Nodo("3")]), Nodo("4",[Nodo("5")]), Nodo("6",[Nodo("7",[Nodo("8")])])]
        arbol=Nodo("A",hijos)
        print(self.gramatica[3])
        print(self.gramatica[4])
        arbolGramatica=self.produccion_a_arbol(self.gramatica[3], self.gramatica[4],0)
        print("paso")
        self._graph_derivation_tree(arbolGramatica,0)
        self.graph.render('derivation_tree', view=True)
        
    def produccion_a_arbol(self, nombreProduccion, producciones, tabulaciones):
        #print("antes "+str(producciones.__len__()))
        #arbolProduccion=Nodo(nombreProduccion)
        produccionActual=None
        indiceProduccionActual=-1
        for indice, produccion in enumerate(producciones):
            if produccion[0]==nombreProduccion:
                produccionActual=produccion
                indiceProduccionActual=indice
                break
        if indiceProduccionActual != -1:
            eliminado=producciones.pop(indiceProduccionActual)
            #print("se elimino "+str(eliminado))
            #print("despues "+str(producciones.__len__()))
        if produccionActual is not None:
            cadena = ""
            hijos=[]
            for componente in produccionActual[1:]:
                #aqui van los terminales
                if componente in self.gramatica[2]:
                    cadena+=componente
                    hijos.append(Nodo(componente))
                    #arbolProduccion.agregarHijo(Nodo(componente))
                #aqui van los no terminales
                elif componente in self.gramatica[1]:
                    #print("entra a "+componente)
                    cadena+=componente
                    subArbol=self.produccion_a_arbol(componente,producciones,tabulaciones+1)
                    hijos.append(subArbol)
                    #arbolProduccion.agregarHijo(subArbol)
            print(" "*tabulaciones+nombreProduccion+"="+cadena)
            arbol=Nodo(nombreProduccion, hijos)
        #print("sale de "+nombreProduccion)
        return arbol

    def _graph_derivation_tree(self, nodo, padre):
        print(str(nodo.data))
        self.graph.node(str(self.counter),label=str(nodo.data))
        if self.counter != 0:
            self.graph.edge(str(padre), str(self.counter))
        counterPadre=self.counter
        for hijo in nodo.hijos:
            self.counter+=1
            self._graph_derivation_tree(hijo,counterPadre)
            print(str(hijo.data))
            
        
        '''if isinstance(data, str):
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
        return self.counter'''
    
class Arbol():
    def __init__(self):
        self.raiz=None
        
class Nodo():
    def __init__(self,data=None,hijos=[]):
        self.data=data
        self.hijos=hijos
    
    def agregarHijo(self, hijo):
        self.hijos.append(hijo)
        


