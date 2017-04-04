import csv
###########################################################
#To cut two columns from nodes file
with open('nodes.gdf', encoding="utf8") as f:
    reader = csv.reader(f)
    your_list1 = list(reader)
t = list()
for n in your_list1:
    del n[2:]
print(your_list1)
with open('nodesCut.gdf', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(your_list1)
###########################################################
###########################################################
#To cut two columns from links file
with open('links.gdf', encoding="utf8") as f:
    reader = csv.reader(f)
    your_list2 = list(reader)
t = list()
for n in your_list2:
    del n[2:]
#print(your_list2)
with open('links0.gdf', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(your_list2)
###########################################################
####To Create a dictionary for nodes file
###########################################################
n0 = []
for n in your_list1:
    if n not in n0:
        n0.append(n[0])
    else:
        'Do nothing'
print(n0)
n1 = []
for n in enumerate(n0):
    n1.append(n)
d1 = dict(n1)
#print(d1)
d = {value: key for key, value in d1.items()}
#print(d)
#print(your_list2)
nodes_list = []
n = []
for n1, m in enumerate(your_list2):
    try:
        temp =list()
        temp.append(d[m[0]])
        temp.append(d[m[1]])
        n.append(temp)
    except:
        temp.append(m[0])
        temp.append(m[1])
        n.append(temp)
################################################
######To get nodes
###############################################
your_list4 = []
with open('nodes.gdf', encoding="utf8") as f:
    reader = csv.reader(f)
    your_list3 = list(reader)
for n2 in your_list3:
    del n2[1:]
    your_list4.append(n2[0])
your_list4.pop(0)
n.pop(0)
print(your_list4)
print(n)
##########################################
print (your_list1)

#########################################
###############################################
###To create a json file
################################################
j1 = '{\n\t"nodes":['
f = open('Jsonfile.json', 'w')
f.write(j1)
for i in range(len(your_list4) - 1):
    f.write('\n\t\t{"name": "' + your_list4[i] + '"},')
f.write('\n\t\t{"name": "' + your_list4[-1] + '"}' + '\n\t],\n\t"links":[')
for j in range(len(n) - 1):
    f.write('\n\t\t{"source": ' + str(n[j][0]) + ',' +'"target": ' + str(n[j][1]) + '},')
f.write('\n\t\t{"source": ' + str(n[-1][0]) + ',' +'"target": ' + str(n[-1][1]) + '}' + '\n\t]\n}')
f.close()






