fn main() {
    println!("Funcao ola mundo com valor");
    println!("--------------------");
    println!("Ola mundo");
    funcao();
    println!("------------------");
    println!("Agora funcao com parametro e valor??");
    parametro(4);
    println!("-------------------");

}

fn funcao(){
    let num: i32 = 41;
    println!("Outro ola mundo {}", num);
}
fn parametro(par: i32){
    println!("O parametro: {}", par);
}