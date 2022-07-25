if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    
    if (a == b and a == c and b == c):
        print((a+b+c)*3)
    else:
        print((a+b+c))