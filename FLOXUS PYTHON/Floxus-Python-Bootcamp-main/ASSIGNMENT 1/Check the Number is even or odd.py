#Program for checking the number is even or odd using bitwise operator


num = int(input("Enter a number : "));
if (num&1==1):
    print(num,"is an odd number");
else:
    print(num,"is an even number");


