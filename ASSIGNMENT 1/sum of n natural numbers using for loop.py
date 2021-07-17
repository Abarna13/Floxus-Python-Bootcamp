#Write a program to find the sum of first N natural number using for loop

n =  int(input("Enter a number : "))
sum = 0
for i in range(1,n+1):
    sum = sum + i
print("The sum is : ", sum)