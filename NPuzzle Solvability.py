#puzzle = [ [7,1,2], [5,1000,4], [8,3,6] ] 
#puzzle = [[6,1,10,2], [7,11,4,14], [5,1000,9,15], [8,12,13,3]] 
puzzle= [[13,10,11,6], [5,7,4,8], [1,12,14,9],[3,15,2,1000]]
# 1000 --> Blank 
onePuzzle= [] 

  
def makeIntoOnePuzzle(puzzle):  
    for i in puzzle: 
        for j in i: 
            onePuzzle.append(j) 
    return onePuzzle 


def dimension(onePuzzle): 
    return len(onePuzzle) 


def inversion(onePuzzle, dimension): 
    inversion=0 
    for i in range (dimension): 
        temp=0 
        for j in range(i+1, dimension): 
            if(onePuzzle[i]>onePuzzle[j]): 
                if(onePuzzle[i]==1000): 
                    continue 
                else: 
                    temp=temp+1 
        inversion=inversion+temp 
  
    return inversion      

  

def blankPosition(puzzle): 
    blankSpace=0 
    for i in puzzle: 
        for j in i: 
            if(j==1000): 
                blankSpace=len(puzzle)-puzzle.index(i) 
    return blankSpace 

     

makeIntoOnePuzzle(puzzle) 
print("Flat Puzzle: ",onePuzzle)

dimensions= dimension(onePuzzle) 
print('Dimension: ',dimensions) 

inversions =inversion(onePuzzle, dimensions) 
print('Inversions: ', inversions) 

blankSpace=blankPosition(puzzle) 
print('Blank Position:', blankSpace) 

  
def solvability(dimensions,inversions,blankSpace): 
    if((dimensions %2 !=0) and (inversions %2==0) ): 
        print('Solveable') 

    elif((dimensions %2 ==0) and (blankSpace %2!=0) and (inversions %2==0) ): 
         print('Solveable') 

    elif((dimensions %2 ==0) and (blankSpace %2==0) and (inversions %2!=0) ): 
         print('Solveable') 

    else: 
        print('Not Solveable!') 

  

solvability(dimensions,inversions,blankSpace)

