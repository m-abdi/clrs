const input = [3, 1, 66, 43, 20]

for (const j of input.map((e, i)=>i).slice(1)) {
    let key = input[j]
    let i = j - 1
    while (i > -1 && input[i] > key) {
        input[i + 1] = input[i]
        i = i - 1
    }
    input[i + 1] = key
}

console.log(input);