def toBinary(n, len):
    binary = ""
    i = 1 << len - 1
    while i > 0:
        binary += "1" if (n & i) else "0"
        i = i // 2
    return binary
 
if __name__ == '__main__':
 
    n = 20
    len = 8
    print(f"The binary representation of {n} is", toBinary(n, len))