import random

population=['01101','11000','01000','10011'] 
print('Chromosomes : ',population) 


def returnPhenotype(chromosome): 
    decodingScheme=[2**i for i in range(4,-1,-1)] 
    phenotype=sum([int(i)*j for i,j in zip(chromosome,decodingScheme)]) 
    return phenotype 

phenotypes=[returnPhenotype(chromosome) for chromosome in population] 
print('Phenotypes : ',phenotypes) 
  
def computFitness(phenotype): return phenotype*phenotype 

fitness=[computFitness(phenotype) for phenotype in phenotypes] 
print('Fitness : ',fitness) 
print('Total Fitness : ',sum(fitness) ) 


def computeProbability(fitness): 
    probabilities=[individualFitness/sum(fitness) for individualFitness in fitness] 
    probabilities=[round(p,3) for p in probabilities] 
    probabilities=[round(p,2) for p in probabilities] 
    return probabilities 


probabilities=computeProbability(fitness) 
print('Probabilities : ',probabilities) 
print('Total Probability : ',sum(probabilities) ) 
bins=[] 


def binning(probabilities):  
    higherRange=0.0 
    lowerRange=0.0  
    for i in probabilities: 
        higherRange=i 
        bins.append((lowerRange,higherRange +lowerRange )) 
        lowerRange=lowerRange+higherRange 

    return bins 

  

print('Associated Bin : ',binning(probabilities)) 
random_value=[]


def randomNumber(): 
    n=len(population) 
    for i in range(n): 
       randomValue= round(random.uniform(0,1),2) 
       random_value.append(randomValue) 
       #print(f"Random No: {randomValue}") 

        
randomNumber() 
print("Random Number:",random_value) 
choosenString=[] 

  
def fallsIntoBin(bins,random_value): 
    for j in random_value: 
        temp =j 
        for i,x in enumerate(bins): 
            if(temp>x[0] and temp<x[1]): 
               choosenString.append(population[i])               

    return choosenString 

  

fallsIntoBin(bins,random_value) 
print("ChoosenString:",choosenString) 

  

def crossover(choosenString): 
    crossoverPoint = random.choice([0,1,2,3,4]) 
    print("CrossoverPoint: ",crossoverPoint)
    
    if((choosenString[0]==choosenString[1])and(choosenString[0]!=choosenString[2])): 
        off1=choosenString[0][:crossoverPoint]+choosenString[2][crossoverPoint:] 
        off2=choosenString[2][:crossoverPoint]+choosenString[0][crossoverPoint:] 
        off3=choosenString[1][:crossoverPoint]+choosenString[3][crossoverPoint:] 
        off4=choosenString[3][:crossoverPoint]+choosenString[1][crossoverPoint:] 
        print("New Chromosomes after Crossover:",off1,off2,off3,off4)     

    elif((choosenString[0]==choosenString[1])and(choosenString[2]==choosenString[3])): 
        off1=choosenString[0][:crossoverPoint]+choosenString[2][crossoverPoint:] 
        off2=choosenString[2][:crossoverPoint]+choosenString[0][crossoverPoint:] 
        off3=choosenString[1][:crossoverPoint]+choosenString[3][crossoverPoint:] 
        off4=choosenString[3][:crossoverPoint]+choosenString[1][crossoverPoint:] 
        print("New Chromosomes after Crossover:: ",off1,off2,off3,off4) 
     

    elif((choosenString[0]==choosenString[2])and(choosenString[1]==choosenString[3])): 
        off1=choosenString[0][:crossoverPoint]+choosenString[2][crossoverPoint:] 
        off2=choosenString[2][:crossoverPoint]+choosenString[0][crossoverPoint:] 
        off3=choosenString[1][:crossoverPoint]+choosenString[3][crossoverPoint:] 
        off4=choosenString[3][:crossoverPoint]+choosenString[1][crossoverPoint:] 
        print("New Chromosomes after Crossover: ",off1,off2,off3,off4) 

    else: 
        off1=choosenString[0][:crossoverPoint]+choosenString[1][crossoverPoint:] 
        off2=choosenString[1][:crossoverPoint]+choosenString[0][crossoverPoint:] 
        off3=choosenString[2][:crossoverPoint]+choosenString[3][crossoverPoint:] 
        off4=choosenString[3][:crossoverPoint]+choosenString[2][crossoverPoint:] 
        print("New Chromosomes after Crossover:",off1,off2,off3,off4) 


crossover(choosenString)  
