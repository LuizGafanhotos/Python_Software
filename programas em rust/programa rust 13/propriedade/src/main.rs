fn main() {
    let linha = "-";
    let mut s = String::from("Ola");
    s.push_str(", Mundo");
    println!("{}",s);
    println!("{}",linha.repeat(30));
    
    let s1 = String::from("Ola");
    let s2 = s1.clone();

    println!("s1 = {} || s2 = {}",s1,s2);
    



}
