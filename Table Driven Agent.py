
import random 

loc_A,loc_B = 'A','B' 
percepts=[] 

def tableDrivenAgent(percept): 
    table={ 
        (('A','Clean'),):'Right', 
        (('A','Dirty'),):'Suck', 
        (('B','Clean'),):'Left', 
        (('B','Dirty'),):'Suck', 

        (('A','Clean'),('A','Clean'),):'Right', 
        (('A','Clean'),('A','Dirty'),):'Suck', 
        (('A','Clean'),('B','Clean'),):'Left', 
        (('A','Clean'),('B','Dirty'),):'Suck', 


        (('A','Dirty'),('A','Clean'),):'Right', 
        (('A','Dirty'),('A','Dirty'),):'Suck', 
        (('A','Dirty'),('B','Clean'),):'Left', 
        (('A','Dirty'),('B','Dirty'),):'Suck', 


        (('B','Clean'),('A','Clean'),):'Right', 
        (('B','Clean'),('A','Dirty'),):'Suck', 
        (('B','Clean'),('B','Clean'),):'Left', 
        (('B','Clean'),('B','Dirty'),):'Suck', 


        (('B','Dirty'),('A','Clean'),):'Right', 
        (('B','Dirty'),('A','Dirty'),):'Suck', 
        (('B','Dirty'),('B','Clean'),):'Left', 
        (('B','Dirty'),('B','Dirty'),):'Suck', 

        } 

    percepts.append(percept) 
    action = table[tuple(percepts)] 
    return action 

  
location = random.choice([loc_A,loc_B]) 
status = random.choice(['Clean','Dirty'])

for _ in range(2): 
    location = random.choice([loc_A,loc_B]) 
    status = random.choice(['Clean','Dirty']) 
    percept=location,status 
    action=tableDrivenAgent(percept) 
    print(f'Agent has perceived: {percepts} and returned action: {action}')

    
