fn main() {
    let value: u32 = 29;
    let sorted_array: [u32; 6] = [1, 5, 6, 18, 29, 83];
    let result = binary_search(&sorted_array, 0, sorted_array.len() - 1, value);
    println!("{}", result);
}

fn binary_search(sorted_array: &[u32; 6], s: usize, e: usize, v: u32) -> Option<usize> {
    if s == e {
        if sorted_array[s] == v {
            return Some(s);
        }
        return None;
    }
    if s > e {
        return None;
    }
    let m = (s + e) / 2;
    if v < sorted_array[m] {
        return binary_search(&sorted_array, s, m, v);
    } else if v > sorted_array[m] {
        return binary_search(&sorted_array, m + 1, e, v);
    } else if v == sorted_array[m] {
        return Some(m);
    }
    None
}
