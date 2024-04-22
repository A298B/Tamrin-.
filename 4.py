def fact(num):
    if(num > 1):
        return num*fact(num-1)
    else:
        return 1
print(fact(6))

input()