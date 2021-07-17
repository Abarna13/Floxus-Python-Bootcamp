'''
Write a python program to print the inverted pyramid?

* * * * *
* * * *
* * *
* *
*

'''

#Program

rows = 5
for i in range(rows,0,-1):
    for j in range(0,rows-1):
        print(end="")
    for j in range(0,i):
        print("*",end= " ")
    print()
