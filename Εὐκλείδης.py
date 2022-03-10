def Euclid_algorithm(a, b):
    while a != b:
        if a > b:
            return Euclid_algorithm(a - b, b)              #Euclid rocks!
        else:
            return Euclid_algorithm(a, b - a)
    return a


print(Euclid_algorithm(31, 30))
