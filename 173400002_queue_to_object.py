'''
In this task, you have to implement a queue of obejct.

Consider matrix as an entity first. If we push three different matrices, the queue will look like below.

1 2 3    2 3 4    1 2 3
4 5 6    5 6 7    7 8 0
7 8 0    1 0 8    4 5 6

If we pop, the queue will look like below.

2 3 4    1 2 3
5 6 7    7 8 0
1 0 8    4 5 6

As we are dealing with object, there will be objects in the queue instead of matrices. Each object will contain multiple information like matrix no, parent no and the combination of the matrix.

First, take a matrix combination, matrix no and parent no from the user. Create an object with these information and push it to the queue. Then in a loop, create objects with random combination, matrix no and parent no and push them. Matrix no should be different for each matrix.

After pushing, perform pop operation.
You can print the values/attributes of the popped object also at the same time.


Get comfortable with the concepts. We will need these ideas later. Write the code on your own. Any kind of plagiarism is strictly prohibited. If found any, you will be penalized.
'''

import numpy as np
start=np.array([[9,8,7],[6,5,4],[3,2,1]])

class state:
    def __init__(self,matno,parentno,mat):
        self.matno=matno
        self.parentno=parentno
        self.mat=mat
    def display(self):
        return f"matno:{self.matno},parentno:{self.parentno},mat:{self.mat}"

obj=state(1,0,start)
q=[]
q.append(obj.matno)
q.append(obj.parentno)
q.append(obj.mat)


while True:
    choice=int(input("enter you choice: "))
    if choice==1:
        matno=int(input("enter matno: "))
        parentno=1
        mats=[[int(input())for i in range(3)] for j in range(3)]
        mat=np.array(mats)
        obj=state(matno,parentno,mat)
        q.append(obj.matno)
        q.append(obj.parentno)
        q.append(obj.mat)
    elif choice==2:
        q.pop(0)
        q.pop(0)
        q.pop(0)
        
    elif choice==3:
        print(q)
    else:
        break


