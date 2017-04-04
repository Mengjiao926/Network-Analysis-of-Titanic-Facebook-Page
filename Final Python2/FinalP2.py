def gdf_to_gml(gdf, gml):
    top0 = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" + '\n' + "<graphml xmlns=\"http://graphml.graphdrawing.org/xmlns\""
    top1 = '\t' + '\t' + 'xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"' + '\n' + '\t' + '\t' + "xsi:schemaLocation=\"http://graphml.graphdrawing.org/xmlns" + '\n' + '\t' + '\t' + "http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd\">"
    top = top0 + '\n' + top1
    top2 = '\t' + "<graph id=\"G\" edgedefault=\"undirected\">" + '\n'
    space = '\t' + '\t'
    Q = ''
    nId = "<node id=\""
    nEnd = "\"/>"
    edges = "<edge source=\""
    tar = "\" target=\""
    tarEnd = "\"/>"
    for line in gdf:
        lane = line.rstrip('\n').split(',')
        if line.startswith('nodedef>name'):
            continue
        if len(lane)>4:
            space = space + nId + lane[0] + nEnd + '\n' + '\t' + '\t'
        elif line.startswith('edgedef>node1'):
            continue
        else:
            Q = Q + edges + lane[0] + tar + lane[1] + tarEnd + '\n' + '\t' + '\t'
    Q = Q[:-1]
    graph = "</graph>" + '\n' + "</graphml>"
    gmlw = top + '\n' + top2 + space + Q + graph
    print(gmlw)
    gml.write(gmlw)

gdf = open('mashable.gdf',encoding="utf8")
gml = open('GML.graphml', 'w')

gdf_to_gml(gdf, gml)
gdf.close()
gml.close()
