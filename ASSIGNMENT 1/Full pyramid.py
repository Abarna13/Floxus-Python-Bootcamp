'''

Write a program to print the full pyramid?
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *

'''

#Program

rows = 5
for i in range(0,rows):
    for j in range(0,rows-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()