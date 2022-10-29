fn main() {
    let value: u32 = 18;
    let sorted_array: [u32; 6] = [1, 5, 6, 18, 29, 83];
    let result = binary_search(&sorted_array, 0, sorted_array.len() - 1, value);
    println!("{:#?}", result);
}

fn binary_search(sorted_array: &[u32; 6], mut s: usize, mut e: usize, v: u32) -> Option<usize> {
    while e > s {
        let m = (s + e) / 2;
        if sorted_array[m] == v {
            return Some(m);
        } else if sorted_array[m] > v {
            e = m - 1;
        } else if sorted_array[m] < v {
            s = m + 1;
        }
    }
    if sorted_array[e] == v {
        return Some(s);
    };
    None
}
