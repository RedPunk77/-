def Euclid_algorithm(a, b):
    while a != b:
        if a > b:
            return Euclid_algorithm(a - b, b)              #Euclid rocks!
        else:
            return Euclid_algorithm(a, b - a)
    return a

x = int(input())
y = int(input())
print(Euclid_algorithm(x, y))
