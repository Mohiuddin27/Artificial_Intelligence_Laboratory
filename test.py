import numpy as np 

goal=np.array([[1,2,3],
              [4,5,6],
              [0,8,7]])
r=1
c=1

temp=goal[r][c]
goal[r][c]=goal[r][c+1]
goal[r][c+1]=temp
print({goal[r][c+1]})
print({goal[r][c]})
print(goal)

