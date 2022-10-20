
from datetime import datetime, timedelta
from random import randint

input = [randint(1, 875) for i in range(23)]
start = datetime.now()

for j in range(1, len(input)):
    key = input[j]
    i = j - 1
    while i > -1 and input[i] > key:
        input[i + 1] = input[i]
        i = i - 1
    input[i + 1] = key


print(input)
print(datetime.now() - start)