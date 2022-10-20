from math import factorial, log


allowed_input_sizes = []


for n in range(1,100):
    if factorial(n) < 10 ** 6:
        allowed_input_sizes.append(n)
    
print(allowed_input_sizes[-1])