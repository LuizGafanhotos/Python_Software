use std::io;


fn main() {
    let a = [1,2,3,4,5];

    println!("Por favor digite uma matriz aqui");

    let mut index = String::new();

    io::stdin()
        .read_line(&mut index)
        .expect("Falhou ao ler a linha");

    let index: usize = index
        .trim()
        .parse()
        .expect("O index nao tem numero");

    let elemento = a[index];

    println!("O valor do elemento inserido no index {} e {}",index, elemento);
}
