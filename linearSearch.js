data = ['a', 'b', 'c', 'd']
v = 'd'

let i = null // c1 
for (const j of data.map((e, i)=>i)) {  // c2  n+1
    if (v === data[j]) {  // c3  n
        i = j   // c4     
        break   // c5
    }
} 


console.log(i);