num = int(input("Enter a number : "))
i=0
result = 0
while result<num: 
    result = 1<<i
    if result == num:
        print("Yes number if power of 2! : 2 power ", i)
        break
    i = i+1
else:
    print("No its not power of 2!")



