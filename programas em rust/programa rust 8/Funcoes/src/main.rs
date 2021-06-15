fn linha(){
    let line = "-".repeat(30);
    println!("{}",line);
}

fn cinco() -> i32{
    5
}

fn main() {
    
    println!("Uma funcao com valores de retorno");
    let func = cinco();
    println!("Ta ai, o valor de func e {}", func);
    linha();

    println!("Funcao ola mundo com valor");
    linha();
    println!("Ola mundo");
    funcao();

    linha();
    println!("Agora funcao com parametro e valor??");
    parametro(4);
    linha();


}

fn funcao(){
    let num: i32 = 41;
    println!("Outro ola mundo {}", num);
}
fn parametro(par: i32){
    println!("O parametro: {}", par);
}