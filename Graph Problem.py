
romaniaMap = { 
    "Arad": {"Timisoara": 118, "Sibiu": 140,"Zerind": 75}, 
    "Zerind": {"Arad": 75, "Oradea": 71}, 
    "Oradea": {"Zerind": 71, "Sibiu": 151}, 
    "Timisoara": {"Arad": 118, "Lugoj": 111}, 
    "Lugoj": {"Timisoara": 111, "Mehadia":70}, 
    "Mehadia": {"Lugoj": 70, "Dobreta": 75}, 
    "Dobreta": {"Mehadia":75, "Craiova":120}, 
    "Craiova": {"Dobreta": 120, "RimnicuVilcea": 146, "Pitesi": 138}, 
    "RimnicuVilcea": {"Craiova": 146, "Pitesi": 97, "Sibiu":80}, 
    "Sibiu": {"Arad": 140, "Oradea":151, "RimnicuVilcea": 80, "Fagaras": 99}, 
    "Fagaras": {"Sibiu": 99, "Bucharest":211}, 
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

  

class graphProblem: 

    def __init__(self,initial,goal,graph): 
        self.initial=initial 
        self.goal=goal 
        self.graph=graph 

  
    def actions(self,state): 
        return list(self.graph[state].keys()) 


    def result(self,stateFrom,action): 
        return action 


    def goalTest(self,state): 
        return state==self.goal 

  
    def pathCost(self,costSoFar,stateFrom,action,stateTo): 
        return costSoFar + self.graph[stateFrom][stateTo] 

  

class Node: 

    def __init__(self,state,parent=None,action=None,path_cost=0): 

        self.state=state 
        self.parent=parent 
        self.action=action 
        self.path_cost=path_cost 

  
    def expand(self,gp):     
        return [self.childNode(gp,action) for action in gp.actions(self.state)] 


    def childNode(self,graphProblem,action):
        
        nextState=graphProblem.result(self.state,action) 
        return Node(nextState,self,action,graphProblem.pathCost(self.path_cost,self.state,action,nextState)) 


    def path(self):
        
        node,pathBack=self,[] 
        while node: 
            pathBack.append(node) 
            node=node.parent 

        return list(reversed(pathBack)) 


    def solution(self):
        return [node.action for node in self.path()[1:]] 

  

def graphSerch(gp,popIndex):
    
    node = Node(gp.initial) 
    frontier=[] 
    explored=set() 
    frontier.append(node) 
    while frontier: 
        print("Frontier: ",[node.state for node in frontier]) 
        node=frontier.pop(popIndex) 
        if gp.goalTest(node.state): return node 
        explored.add(node.state) 
        print("Explored: ",explored) 
        for child in node.expand(gp): 
            if child.state not in explored and child.state not in frontier: 
                frontier.append(child)
                

def dfs(gp, popIndex=-1):
    
    node = graphSerch(gp,popIndex) 
    return node 

 

def bfs(gp, popIndex=0):
    
     node = graphSerch(gp,popIndex) 
     return node 

  

gp=graphProblem("Arad","Bucharest",romaniaMap) 
goalNode=bfs(gp) 

  
print(gp.initial,goalNode.solution(),goalNode.path_cost)


