import numpy as np

size = 3*3

w = np.zeros((size, size))

# [0,0,0, #0
#          0,0,0,
#          0,0,0],

data = [[1,0,1, #U
         1,0,1,
         1,1,1],

        [1,0,1, #H
         1,1,1,
         1,0,1],

        [1,1,1, #T
         0,1,0,
         0,1,0],

        [1,1,1, #C
         1,0,0,
         1,1,1]
        
       ]

alphabet = data


for index1 ,i in enumerate(alphabet):
    for index2 ,j in enumerate(i) :
        if j == 0:
            alphabet[index1][index2] = -1

######################################################
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


######################################################

#Testing stage

input_sample =[1,1,1, 
               0,1,0,
               1,1,0]

x = np.zeros((size,), dtype=int)
y = np.zeros((size,), dtype=int)

for i in range(size):
        x[i]=input_sample[i]

iteration = 1


while ( not (all(x[i] == y[i] for i in range(size))) ):
    
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

    #print ("X = " , x)
    #print ("Y = ", y)

    print(y[0:3])
    print(y[3:6])
    print(y[6:9])


    print("X == Y ? ",all(x[i] == y[i] for i in range(size)), "\n" )



    if(not (all(x[i] == y[i] for i in range(size)) )):
        x= y
        y= np.zeros((size,), dtype=int)

            
    iteration +=1



# counter_matrix = np.zeros((len(data),), dtype=int)

# for index1 ,i in enumerate(data):
#     for index2 ,j in enumerate(i) :
#         if j == -1:
#             data[index1][index2] = 0


# for index_i,i in enumerate(data) :
#     for index_j,j in enumerate(i):
#         if (j == y[index_j]):
#             counter_matrix[index_i] +=1
    

# boo = np.where(counter_matrix == max(counter_matrix))
# #print(boo[0][0])
# print("your letter is:")
# print(alphabet[boo[0][0]])