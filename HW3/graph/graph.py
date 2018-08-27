import numpy as np
import heapq
from ast import literal_eval



def read_file(file):
    """
    Read text file.
    :param file: a .txt file storing graph data
    :return: graph
    """
    with open(file) as f:
        text = f.readlines()
    cnt = 0
    source = []
    edges = []
    for i in range(len(text)):
        temp = text[i].strip().split("\n")
        if cnt % 2 == 0:
            source.append(temp[0])
        else:
            edges.append(temp[0])
        cnt += 1
    graph = dict([(float(elem), []) for elem in source])
    next = [[] for i in range(len(source))]
    for i in range(len(source)):
        start = 0
        if edges[i] != "":
            for j in range(len(edges[i])-1):
                if edges[i][j] == ")" and edges[i][j + 1] == ",":
                    next[i].append(literal_eval(edges[i][start: j + 1]))  #
                    start = j + 2
            next[i].append(literal_eval(edges[i][start: len(edges[i])]))
        else:
            next[i].append("")
    for i in range(len(source)):
        for j in range(len(next[i])):
            if edges[i] != "":
                temp = (float(next[i][j][0]), float(next[i][j][1]))
                graph[float(source[i])].append(temp)
    return(graph)

def find_shortest_path(file, source, destination):
    """
    Find shortest path using Dijkstra’s algorithm.
    :param file: a .txt file
    :param source: a start point of a graph
    :param destination: a end point of a graph
    :return: shortest path
    """
    s = []
    F = []
    F_node = []
    s_node = []
    graph = read_file(file)
    dist = dict()
    dist[source] = 0.0
    path = dict([(float(element), []) for element in graph.keys()])
    for i in path.keys():
        path[i].append(float(source))
    heapq.heappush(F, (dist[source], source))
    F_node.append(F[-1][1])
    while F != []:
        f = heapq.heappop(F)
        s.append(f)
        s_node.append(s[-1][1])
        for node in graph[f[1]]:
            if node[0] not in F_node and node[0] not in s_node:
                dist[node[0]] = dist[f[1]] + node[1]
                path[node[0]] = (path[f[1]][:])
                path[node[0]].append(node[0])
                heapq.heappush(F, (dist[node[0]], node[0]))
                F_node.append(node[0])
            elif dist[f[1]] + node[1] < dist[node[0]]:
                dist[node[0]] = dist[f[1]] + node[1]
                path[node[0]] = (path[f[1]][:])
                path[node[0]].append(node[0])
                if node[0] not in s_node:
                    for i in range(len(F)):
                        if F[i][1] == node[0]:
                            del F[i]
                            heapq.heappush(F, (dist[node[0]], node[0]))
                            s_node.append(node[0])
                            break
                    tempF = []
                    for i in range(len(F)):
                        temp = heapq.heappop(F)
                        heapq.heappush(tempF, temp)
                    F = tempF
                    F_node.append(node[0])
    if len(path[destination]) == 1 and source != destination:
        return [], float("inf")
    else:
        return path[destination], dist[destination]

def min_path(graph, num_step, source, destination):
    """
    Find the min path
    :param graph: the graph
    :param num_step: number of step
    :param source: the start point of a graph
    :param destination: the end point of graph
    :return: the min path
    """
    if num_step==0:
        if destination==source:
            return 0, [source]
        else:
            return float("inf"), []
    child=[]
    path=[]
    for node in graph[source]:
        temp = min_path(graph, num_step-1, node[0], destination)
        child.append(temp[0] + node[1])
        path.append(temp[1])
    if len(child)==0:
        if source==destination:
            return 0, [source]
        else:
            return float("inf"), []
    temp_min=np.min(child)
    min_path=path[np.argmin(child)][:]
    previous=min_path(graph, num_step-1, source, destination)
    minimum = np.min([temp_min,previous[0]])
    if temp_min<previous[0]:
        min_path.insert(0,source)
    else:
        min_path=previous[1][:]
    return minimum, min_path

def find_negative_cicles(name_txt_file):
    graph = read_file(name_txt_file)
    N=len(graph)
    for source,source_child in graph.items():
        for destination, destination_child in graph.items():
            temp_N=min_path(graph, N, source, destination)
            temp_n=min_path(graph, N-1, source, destination)
            path=[]
            if temp_N[0]<temp_n[0]:
                path=temp_N[1][:]
                start=0
                end=0
                for end in range(1,len(path)):
                    for start in range(0,end):
                        if path[end]==path[start]:
                            return path[start:end+1]
    return []


