'''
Write a python program to print the following number pyramid?
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

'''

#Program 

rows = 5
for i in range(1, rows+1):     
    for j in range(1, i+1):    
        print(i, end = " ")
    print()
