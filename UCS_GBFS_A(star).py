
romania = { 
    "Arad": {"Timisoara": 118, "Sibiu": 140, "Zerind": 75}, 
    "Zerind": {"Arad": 75, "Oradea": 71}, 
    "Oradea": {"Zerind": 71, "Sibiu": 151}, 
    "Timisoara": {"Arad": 118, "Lugoj": 111}, 
    "Lugoj": {"Timisoara": 111, "Mehadia": 70}, 
    "Mehadia": {"Lugoj": 70, "Dobreta": 75}, 
    "Dobreta": {"Mehadia": 75, "Craiova": 120}, 
    "Craiova": {"Dobreta": 120, "RimnicuVilcea": 146, "Pitesi": 138}, 
    "RimnicuVilcea": {"Craiova": 146, "Pitesi": 97, "Sibiu": 80}, 
    "Sibiu": {"Arad": 140, "Oradea": 151, "RimnicuVilcea": 80, "Fagaras": 99}, 
    "Fagaras": {"Sibiu": 99, "Bucharest": 211}, 
    "Pitesi": {"Bucharest": 101, "RimnicuVilcea": 97, "Craiova": 138}, 
    "Bucharest": {"Pitesi": 101, "Fagaras": 211, "Giurgiu": 90, "Urziceni": 85}, 
    "Giurgiu": {"Bucharest": 90}, 
    "Urziceni": {"Bucharest": 85, "Hirsova": 98, "Vaslui": 142}, 
    "Hirsova": {"Urziceni": 98, "Eforie": 86}, 
    "Eforie": {"Hirsova": 86}, 
    "Vaslui": {"Urziceni": 142, "Iasi": 92}, 
    "Iasi": {"Vaslui": 92, "Neamt": 87}, 
    "Neamt": {"Iasi": 87} 
} 

  

straight_line_cost= { 
    "Arad": 366, 
    "Bucharest": 0, 
    "Craiova": 160, 
    "Dobreta": 242, 
    "Eforie": 161, 
    "Fagaras": 176, 
    "Giurgiu": 77, 
    "Hirsova": 151, 
    "Iasi": 226, 
    "Lugoj": 244, 
    "Mehadia": 241, 
    "Neamt": 234, 
    "Oradea": 380, 
    "Pitesi": 100, 
    "RimnicuVilcea": 193, 
    "Sibiu": 253, 
    "Timisoara": 329, 
    "Urziceni": 80, 
    "Vaslui": 199, 
    "Zerind": 374 
} 

  


class graphProblem: 

  
    def __init__(self, initialState, goalState, graph): 
        self.initial = initialState 
        self.goalState= goalState 
        self.graph = graph 


    def actions(self, state): 
        return list(self.graph[state].keys()) 

  

    def result(self, state, action): 
        return action 

  
    def goalTest(self, state): 
        return state == self.goalState
    
  
    def pathCost(self, cost_so_far, fromState, action, toState): 
        return cost_so_far + self.graph[fromState][toState] 


class Node: 

    def __init__(self, state, parent=None, action=None, path_cost=0): 
        self.state = state 
        self.parent = parent 
        self.action = action 
        self.path_cost = path_cost 

  
    def childNode(self, gp, action): 
        childState = gp.result(self.state, action) 
        path_cost_to_childNode = gp.pathCost(self.path_cost, self.state, action, childState) 
        return Node(childState, self, action, path_cost_to_childNode) 


    def expand(self, gp): 
        return [self.childNode(gp, action) for action in gp.actions(self.state)] 


    def path(self): 
        node=self 
        pathBack=[] 

        while node: 
            pathBack.append(node) 
            node=node.parent 

        result= [node.state for node in pathBack] 
        return list(reversed(result)) 

  

def Uniform_cost_search(gp):
    
    initialNode = Node(gp.initial) 
    frontier = [] 
    frontier.append(initialNode) 
    explored = set() 

    while frontier: 
        frontier.sort(key=lambda node: node.path_cost)  
        print('Frontier: ',[node.state for node in frontier])
        
        if len(frontier) == 0: return 'Failure' 
        node = frontier.pop(0)
        
        if gp.goalTest(node.state): return node 
        explored.add(node.state) 
        print("Explored: ",explored) 

        for child in node.expand(gp): 
            if child.state not in explored and child not in frontier: 
                frontier.append(child) 

    return None 

  

def Greedy_best_first_search(gp): 
  
    frontier = [] 
    initialNode = Node(gp.initial) 
    frontier.append(initialNode) 
    explored = set() 

    while frontier: 
        frontier.sort(key=lambda node: straight_line_cost[node.state])   
        print('Frontier: ',[node.state for node in frontier])
        
        if len(frontier) == 0: return 'Failure' 

        node = frontier.pop(0) 
        if gp.goalTest(node.state): return node
        
        explored.add(node.state) 
        print("Explored: ",explored) 

        for child in node.expand(gp): 
            if child.state not in explored and child.state not in frontier: 
                frontier.append(child) 

    return None 

  

def A_star_search(gp):
    
    initialNode = Node(gp.initial) 
    frontier = [] 
    frontier.append(initialNode) 
    explored = set() 
  
    while frontier: 
        frontier.sort(key=lambda node: node.path_cost + straight_line_cost[node.state])   
        print('Frontier: ',[node.state for node in frontier])
        
        if len(frontier) == 0: return 'Failure'
        
        node = frontier.pop(0) 
        if gp.goalTest(node.state): return node 


        explored.add(node.state) 
        print("Explored: ",explored) 
        for child in node.expand(gp): 
            if child.state not in explored and child not in frontier: 
                frontier.append(child) 

    return None 
 


gp = graphProblem('Arad', 'Bucharest', romania)

print("\nUniform Cost Search ") 
print('***********************************')
goalNode= Uniform_cost_search(gp) 
print("\nReached Goal Node: ",goalNode.state) 
print("Solution: ", goalNode.path(),"\nPath cost to goal : ", goalNode.path_cost) 

print("\nGreedy best first search ") 
print('***********************************') 
goalNode= Greedy_best_first_search(gp) 
print("\nReached Goal Node: ",goalNode.state) 
print("Solution: ", goalNode.path(),"\nPath cost to goal : ", goalNode.path_cost) 

  
print(" \nA*  Search ") 
print('***********************************') 
goalNode= A_star_search(gp) 
print("\nReached Goal Node: ",goalNode.state) 
print("Solution: ", goalNode.path(),"\nPath cost to goal : ", goalNode.path_cost) 


