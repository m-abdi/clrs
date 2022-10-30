fn main() {
    let mut a = [15, 11, 7, 3, 2];
    bubble_sort(&mut a);
    println!("{:#?}", a);
}

fn bubble_sort(input_array: &mut [u32; 5]) {
    for i in 0..input_array.len() - 1 {
        for j in (i+1 ..input_array.len()).rev() {
            if input_array[j] < input_array[j - 1] {
                (input_array[j], input_array[j - 1]) = (input_array[j - 1], input_array[j])
            }
        }
    }
}
