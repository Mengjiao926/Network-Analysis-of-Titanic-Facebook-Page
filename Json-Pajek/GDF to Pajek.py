##Pajek File Conversion
import networkx as net
import matplotlib.pyplot as plot

GDF = open('chenchu.gdf')
pajek = open('chenchupajek.paj', 'w')
pajek1 = open('chenchupajek.net', 'w')
dict  = {}
p1 = 0
list = []
for line in GDF:
    if line.startswith('nodedef>name'):
        continue
    if line.startswith('edgedef>node1'):
        break
    lane = line.rstrip('\n').split(',')
    list.append(lane)
    if lane[0] not in dict.keys():
        p1 = p1 + 1
        dict[lane[0]] = p1
p2 = len(dict.keys())
vertices = "*vertices" + " " + str(p2)
ver = vertices + '\n'
for i in list:
    p3 = dict[i[0]]
    p4 = i[0]
    ver = ver + str(p3) + ' ' + p4 + '\n'
ver = ver + '*edges' + '\n'
for j in GDF:
    p5 = j.rstrip('\n').split(',')
    ver = ver + str(dict[p5[0]]) + ' ' + str(dict[p5[1]]) + '\n'
print(ver)
pajek.write(ver)
pajek1.write(ver)
pajek.close()
pajek1.close()
