'''
In this task you have to implement a check function in the queue of matrix.

First, define a goal matrix. For example,
1 2 3
4 5 6
7 8 0

Then push some random matrix in the queue along with the goal matrix. After that iteratively pop matrix from the queue. When you get the popped matrix, you have to determine if it is the goal matrix. If it is, then print "Found goal" and break the loop.

An abstract idea is given below for the implementation.

Define goalMatrix 
1 2 3
4 5 6
7 8 0

The queue of matrix (m2, m3, m4, m5 are just notations for representing the matrices)
Q = m2 m3 m4 m5

while(!queue.empty()){
	popMatrix = Q.pop()
	same = checkGoal(goalMatrix, popMatrix)
	if same is true:
		print("Found goal")
		break
}

function checkGoal(g, p){
	if g and p are equal:
		return true
	return false
}
'''

import numpy as np
start=np.array([[0,8,7],[6,5,4],[3,2,1]])
goal=np.array([[1,2,3],[4,5,6],[7,8,0]])

class state:
    def __init__(self,matno,parentno,mat):
        self.matno=matno
        self.parentno=parentno
        self.mat=mat
    
    
q=[]
matno=1
obj=state(matno,0,start)
q.append(obj)

for i in range(3):
    mats=[[int(input(f"matrix element {[i]} {[j]}: "))for i in range(3)] for j in range(3)]
    mat=np.array(mats)
    matno=matno+1
    obj=state(matno,0,mat)
    q.append(obj)
print(q[0].matno,q[0].mat)
print(q[1].matno,q[1].mat)
print(q[2].matno,q[2].mat)
print(q[3].matno,q[3].mat)
  
def checkgoal(popped_mat,goal):
    if (np.array_equal(popped_mat,goal)):
        return True
    else:
        return False

while (q!=[]):
    popped_state=q[0]
    goal_flag = checkgoal(popped_state.mat,goal)
    q.pop(0)
    if goal_flag==True:
        print(f"MatrixNO: {popped_state.matno} is the Goal !")
        break
