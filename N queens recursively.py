n=4 
r=0 
Q=[False]*n 


def placeQueens(Q,r): 
    if (r== n): 
        print(Q) 
    else: 
        for j in range(n): 
            legal = True 
            for i in range (r): 
                if((Q[i]==j) or (Q[i]==j+r-i) or (Q[i]==j-r+i)): 
                    legal = False      

            if (legal): 
                Q[r]=j 
                placeQueens(Q,r+1) 

                 

placeQueens(Q,r)        

                 

         

 
