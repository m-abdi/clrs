allowed_input_sizes = []


for n in range(1,100):
    if 100 * (n ** 2) < 2 ** n:
        allowed_input_sizes.append(n)
    
print("smallest value of n is: ", allowed_input_sizes[0])