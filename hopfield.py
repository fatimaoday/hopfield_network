import numpy as np

size = 5*5

w = np.zeros((size, size))

alphabet =[
    [-1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1],
    [1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1 ,-1 , 1, 1, 1, 1, 1],
    [1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1 ]
    ]

######################################################################################################
#Learing stage

for i in range(size):
    for j in range(size):
        if i == j :
            w[i][j]=0
        else:
            a=0
            for n in range(len(alphabet)):
                a = a+  alphabet[n][i] * alphabet[n][j]    
            w[i][j]= a

print (w)


######################################################################################################
#Testing stage

input_sample =[0,1,1,1,0,
               0,1,0,1,0,
               1,0,0,0,1,
               1,1,1,1,1,
               1,0,0,0,0]

x = np.zeros((size,), dtype=int)
y = np.zeros((size,), dtype=int)

for i in range(size):
        x[i]=input_sample[i]

iteration = 1
boo = 0

while ( not (all(x[i] == y[i] for i in range(size))) or boo == 1 ):
    
    for index_i, i in enumerate(x) :
            
        a=0
        for index_j, j in enumerate(x) :
            a= a+ ( w[index_i][index_j] * j )

        result = i+a
        #print(index_i+1, result)
            
        if(result) > 1:
            y[index_i] = 1
        elif (result) < 0 :
            y[index_i] = 0
        else:
            y[index_i] = result

    print("iteration :", iteration)        
    print ("X = " , x)
    print ("Y = ", y)
    print("X == Y ? ",all(x[i] == y[i] for i in range(size)) )



    if(not (all(x[i] == y[i] for i in range(size)) )):
        x= y
        y= np.zeros((size,), dtype=int)
    else :
        boo += 1
        
    print("Equal two times ?", boo, "\n")
    
    iteration +=1

















