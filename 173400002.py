
# q=[]
# length=int(input("enter your length: "))
# i=0
# while(i<length):
#     element=str(input("enter:"))
#     q.append(element)
#     i+=1
    
# print(q)
# delete=input("for pop, write yes:")
# if delete=="yes":
#     delete=int(input("enter you poisition:"))
#     q.pop(delete)
# print(q)
'''
Your task is very simple.

You have to implement a queue. The datatype of the elements of the queue will be anything except integer.
There will be push, pop and display operations.
Implement the operations dynamically. You can take the input/command from user and do the operations.

Use any language of your choice. Your file name will be your student id.
Do not copy others code. It is a simple task. You should write it on your own.
'''
q=[]
x=input()
q.append(x)
while True:
    choice=int(input())
    if choice==1:
        a=input()
        q.append(a)
    elif choice==2:
        q.pop(0)
    elif choice==3:
        print(q)
    else:
        break
