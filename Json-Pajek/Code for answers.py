import networkx as net
import matplotlib.pyplot as plt
g = net.read_pajek('chenchupajek.net')
print("Find the number of nodes in the graph?")
print ("Nodes: ",len(g))

print("Find the number of components (connected subgraphs)?")
print ("Number of components (Connected Subgraphs): ",len(list(net.connected_component_subgraphs(g))))

print("Find the node with the maximum degree? What is that degree?")
deg = net.degree(g)
print("Node with Maximum Degree: ", max(deg, key=deg.get))
print("Maximum Degree: ", max(deg.values()))

undirected = g.to_undirected()
print ('Number of edges for undirected graph: ',len(undirected.edges()))

print("What is the density of the graph?")
print ("Density of the Graph: ",net.density(g))

print("Create a degree distribution plot?")
h = g.to_undirected()
print("Number of edges in the converted undirected graph is: %s"%h.number_of_edges())

print("Density of the undirected graph is: %s"%net.density(h))

degree_sequence=sorted(net.degree(g).values(),reverse=True)
dmax = max(degree_sequence)
plt.hist(degree_sequence,bins=dmax)
plt.title("Degree Distribution Plot")
plt.ylabel("count")
plt.xlabel("degree")
plt.show()