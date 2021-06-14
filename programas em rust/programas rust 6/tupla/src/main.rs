fn main() {
    let tupla: (i32, f64, u8) = (600,6.5,2);
    
    let (_x, _y, _z) = tupla;

    println!("O valor de y e {}", _y);
    println!("O valor de x e {}", _x);
    println!("O valor de z e {} \n", _z);
    println!("---------------------------");

    let valor2: (i32,f64, i8) = (560 , 1.0 , 4);

    let c1 = valor2.0;
    let c2 = valor2.1;
    let c3 = valor2.2;

    println!("O valor de c1 e {}", c1);

}
