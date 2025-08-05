import heapq
def greedy_best_First_Search(graph,start,goal,heuristic):
    priority_queue = [(heuristic[start],start,[start])]
    visited = set()

    while priority_queue:
        h_cost,current_node,path = heapq.heappop(priority_queue)
        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node == goal:
            return path
        for neighbor in graph.get(current_node,{}):
            if neighbor not in visited:
                new_path = path + [neighbor]
                heapq.heappush(priority_queue,(heuristic[neighbor],neighbor,new_path))
    return None
if __name__ == "__main__":
    graph1 = {
        'A':{'B':1, 'C':5},
        'B':{'D':3, 'E':6},
        'C':{'F':2},
        'D':{'G':4},
        'E':{'G':2},
        'F':{'G':7},
        'G':{}

    }

    heuristic1 ={
        'A':7,
        'B':6,
        'C':3,
        'D':4,
        'E':2,
        'F':1,
        'G':0
    }

    path1 = greedy_best_First_Search(graph1,'A','G',heuristic1)
    if path1:
        print(f"path from A to G:{path1}")
    else:
        print("No path found")
        
