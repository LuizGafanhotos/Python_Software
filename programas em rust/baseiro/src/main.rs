fn main() {
    let s1 = String::from("Tua mae");
    let len = calculate_length(&s1);

    println!("O comprimento de {} é {}.",s1 , len);
}
fn calculate_length(s: &String) -> usize {
    s.len()
}
