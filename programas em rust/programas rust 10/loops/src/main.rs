fn main() {
    /*
    let mut contador = 0;

    let resultado = loop{
        contador += 1;

        if contador == 10{
            break contador * 2;
        }
    };
    println!("O valor de contandor e {}", resultado);
    */

    let mut valor = 1;

    while valor <= 10{
        println!("{}!",valor);

        valor += 1;
    }
    println!("Explosao!!");
}
