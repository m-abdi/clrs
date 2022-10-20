const input = [700, 10, 6, 7, 2.2];

for (const j of input.map((e, i) => i).slice(0, input.length - 1)) {  //   c1  n
  let i = j + 1;   //  c2   n - 1
  let key = input[j];    // c3  n-1
  while (i < input.length) {  // c4   n(n+1)/2
    if (input[i] < key) {   // c5      n(n - 1) / 2
      input[j] = input[i];  // c6      n(n - 1) / 2
      input[i] = key; // c7      n(n - 1) / 2
      key = input[j];  // c8      n(n - 1) / 2
    }
    i++;    // c9      n(n - 1) / 2
  }
}

console.log(input);
