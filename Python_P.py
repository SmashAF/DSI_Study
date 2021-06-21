def fact(num):
    prod = 1
    for num in range(1, num+1):
        prod*=num
    return prod
print(fact(4))



