fn main() {
    let linha = "-";
    let a = [10,20,30,40,50];

    for elemento in a.iter(){
        println!("O valor e: {}", elemento);
    }
    println!("{}",linha.repeat(30));
    
    for numero in (1..4).rev() {
        println!("{}", numero);
    }
    println!("SCADUSH");

}
