input = [i for i in range(10000000)]
input.reverse()
for i in range(1, len(input)):
    key = input[i]
    j = i - 1
    while j > -1 and input[j] > key:
        input[j + 1] = input[j]
        j = j - 1
    input[j + 1] = key


print(i)
print(input)