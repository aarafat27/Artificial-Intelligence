import random 

class Object: 

    def __repr__(self): 
        return '<%s>' % getattr(self,'__name__',self.__class__.__name__) 

  

class Agent(Object): 

    def __init__(self): 
        def program(percept):abstract 
        self.program=program 

  

loc_A,loc_B='A','B' 
  

class vaccumEnvironment: 

    def __init__(self): 
        self.status={ loc_A:random.choice(['Clean','Dirty']), 

                      loc_B:random.choice(['Clean','Dirty']) 

                      } 


    def add_object(self,object,location=None): 
        object.location=location or self.default_location(object) 
  

    def default_location(self,object): 
        return random.choice([loc_A,loc_B]) 

  
    def percept(self,agent): 
        return (agent.location,self.status[agent.location]) 

  
    def execute_action(self,agent,action): 
        if action=='Right': agent.location=loc_B 
        elif action=='Left': agent.location=loc_A 
        elif action=='Suck': 
            self.status[agent.location]='Clean' 

 

class modelBasedVacuumAgent(Agent): 

    def __init__(self): 
        Agent.__init__(self) 
        model = {loc_A: None, loc_B: None}
        
        def program(percept):  
            location=percept[0] 
            status=percept[1] 
            model[location]=status    

            if model[loc_A] == model[loc_B] == 'Clean': return 'Nothing' 
            elif status == 'Dirty': return 'Suck' 
            elif location == loc_A: return 'Right' 
            elif location == loc_B: return 'Left' 

            percept= (location, status) 
            print('Agent perceives ', tuple(percepts), ' and does ', action) 
            print(f"Agent perceives {percept} and does {action}") 

            return action 

        self.program = program 

 


Tagent=modelBasedVacuumAgent() 
env=vaccumEnvironment() 
env.add_object(Tagent) 

for _ in range(10): 
    action=Tagent.program(env.percept(Tagent)) 
    env.execute_action(Tagent,action) 
