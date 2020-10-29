import pygame
import graphUI
from node_color import white, yellow, black, red, blue, purple, orange, green

import time
from queue import PriorityQueue


"""
Feel free print graph, edges to console to get more understand input.
Do not change input parameters
Create new function/file if necessary
"""


def BFS(graph, edges, edge_id, start, goal):
 
    visit = [start]
    queue = [(start, [start])]
    pathGraph = []
    flagEnd = 0
    while queue:
        (v, path) = queue.pop(0)  
        
        graph[v][3] = yellow
        graphUI.updateUI()
        for w in graph[v][1]:
            if w not in visit:
                visit.append(w)
                edges[edge_id(v, w)] = [(v, w), white]
                graph[w][3] = red
                graphUI.updateUI()
                time.sleep(1)
                if w == goal:
                    flagEnd = 1
                    pathGraph =  path + [w]
                    break
                queue.append((w, path + [w]))

        if (flagEnd == 1):
            break
        graph[v][3] = blue
        graphUI.updateUI()
        time.sleep(1)
    
    graph[start][3] = orange

    for i in range(0, len(pathGraph) - 1):
        edges[edge_id(pathGraph[i], pathGraph[i+1])] = [(pathGraph[i], pathGraph[i + 1]), green]
    
    #end
    graph[goal][3] = purple

    graphUI.updateUI()

    print("Implement BFS algorithm.")
    pass


def DFS(graph, edges, edge_id, start, goal):
    
    stack = [(start, [start])]
    visit = [start]
    pathGraph = []

    flagEnd = 0

    while stack:
        #print(stack)
        (v, path) = stack.pop()

        #set node graphic
        graph[v][3] = yellow
        graphUI.updateUI()
        
        for w in graph[v][1]:
            if w not in visit:
                visit.append(v)
                
                edges[edge_id(v, w)] = [(v, w), white]
                graph[w][3] = red
                graphUI.updateUI()
                time.sleep(1)
                if w == goal:
                    flagEnd = 1
                    pathGraph =  path + [w]
                    break
                stack.append((w, path + [w]))

        if (flagEnd == 1):
            break

        graph[v][3] = blue
        graphUI.updateUI()

        time.sleep(1)


    graph[start][3] = orange

    for i in range(0, len(pathGraph) - 1):
        edges[edge_id(pathGraph[i], pathGraph[i+1])] = [(pathGraph[i], pathGraph[i + 1]), green]
    
    #end
    graph[goal][3] = purple

    graphUI.updateUI()

    print("Implement DFS algorithm.")
    pass


#Get distance of 2 v
def DistanceEdges(v, w):
    return ((v[0][0] - w[0][0])**2 + (v[0][1] - w[0][1])**2)**(1/2)



def UCS(graph, edges, edge_id, start, goal):
    """
    Uniform Cost Search search
    """
    priQueue = PriorityQueue()

    priQueue.put((0, start, [start]))  # (priority, current_node, path, cost)


    closeList = []
  

   
    while priQueue:
        cost, v, path = priQueue.get()
        
        if v in closeList:
            continue

        if v == goal:
            pathGraph = path
            break

        graph[v][3] = yellow
        graphUI.updateUI()
        
        closeList.append(v)
         

        for w in graph[v][1]:
            if w not in closeList:  

                #put in priority queue
                priQueue.put((
                    cost + DistanceEdges(graph[v], graph[w]),
                    w,
                    path + [w]
                ))

            
                #set graphic
                edges[edge_id(v, w)] = [(v, w), white]
                graph[w][3] = red
                graphUI.updateUI()
                time.sleep(1)
                
            
                    

                
        graph[v][3] = blue
        graphUI.updateUI()
            
        time.sleep(1) 
            

    graph[start][3] = orange
 
    for i in range(0, len(pathGraph) - 1):
        edges[edge_id(pathGraph[i], pathGraph[i+1])] = [(pathGraph[i], pathGraph[i + 1]), green]
    
    #end
    graph[goal][3] = purple
    graphUI.updateUI() 
    
    print("Implement Uniform Cost Search algorithm.")
    pass


def euclid(u, v):
    return ((u[0][0] - v[0][0]) ** 2 + (u[0][1] - v[0][1]) ** 2) ** (1/2)
    

def AStar(graph, edges, edge_id, start, goal):
    """
    A star search
    """
    #f(x) = G(x) + H(x)

    G: Dict[Location, float] = {}
    G[start] = 0


    #create priority queue
    queue = PriorityQueue()

    queue.put((0, start, [start]))


    # Init open and closed list

    openList = [start]
    closeList = []

    #list edges are tranported
    pathGraph = []

  
    # Lặp tới khi queue rỗng
    while queue:
        # Lấy một đỉnh từ queue
        
        cost, v, path = queue.get()
        openList.remove(v)
        closeList.append(v)

        graph[v][3] = yellow
        graphUI.updateUI()


        #go to goal
        if v == goal:
            pathGraph = path
            break
        
        # for each adjacency v
        for w in graph[v][1]:   
            newCost = G[v] + euclid(graph[w], graph[v]) 
            if (w not in closeList) and (w not in G or newCost < G[w]):

                #add open list
                openList.append(w)

                #set graphic    
                edges[edge_id(v, w)] = [(v, w), white]
                graph[w][3] = red
                graphUI.updateUI()
                time.sleep(1)

                G[w] = newCost
                f = G[w] + euclid(graph[w], graph[goal])
        
                queue.put((f, w, path + [w]))
            

        graph[v][3] = blue
        graphUI.updateUI()
         
        time.sleep(1) 
            

    graph[start][3] = orange

    for i in range(0, len(pathGraph) - 1):
        edges[edge_id(pathGraph[i], pathGraph[i+1])] = [(pathGraph[i], pathGraph[i + 1]), green]
    
    #end
    graph[goal][3] = purple
    graphUI.updateUI() 

    print("Implement A* algorithm.")
    pass


def example_func(graph, edges, edge_id, start, goal):
    """
    This function is just show some basic feature that you can use your project.
    @param graph: list - contain information of graph (same value as global_graph)
                    list of object:
                     [0] : (x,y) coordinate in UI
                     [1] : adjacent node indexes
                     [2] : node edge color
                     [3] : node fill color
                Ex: graph = [
                                [
                                    (139, 140),             # position of node when draw on UI
                                    [1, 2],                 # list of adjacent node
                                    (100, 100, 100),        # grey - node edged color
                                    (0, 0, 0)               # black - node fill color
                                ],
                                [(312, 224), [0, 4, 2, 3], (100, 100, 100), (0, 0, 0)],
                                ...
                            ]
                It means this graph has Node 0 links to Node 1 and Node 2.
                Node 1 links to Node 0,2,3 and 4.
    @param edges: dict - dictionary of edge_id: [(n1,n2), color]. Ex: edges[edge_id(0,1)] = [(0,1), (0,0,0)] : set color
                    of edge from Node 0 to Node 1 is black.
    @param edge_id: id of each edge between two nodes. Ex: edge_id(0, 1) : id edge of two Node 0 and Node 1
    @param start: int - start vertices/node
    @param goal: int - vertices/node to search
    @return:
    """

    # Ex1: Set all edge from Node 1 to Adjacency node of Node 1 is green edges.
    node_1 = graph[1]
    for adjacency_node in node_1[1]:
        edges[edge_id(1, adjacency_node)][1] = green
    graphUI.updateUI()

    # Ex2: Set color of Node 2 is Red
    graph[2][3] = red
    graphUI.updateUI()

    # Ex3: Set all edge between node in a array.
    path = [4, 7, 9]  # -> set edge from 4-7, 7-9 is blue
    for i in range(len(path) - 1):
        edges[edge_id(path[i], path[i + 1])][1] = blue
    graphUI.updateUI()
