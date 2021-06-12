const n1 = document.querySelector("input#input1") as HTMLInputElement;
const n2 = document.querySelector("input#input2") as HTMLInputElement;
const oi = document.querySelector("button#buton");

function sub(v1: number, v2: number){
    return v1 - v2;
}
if (oi){
    oi.addEventListener("click", () =>{
        console.log(sub(Number(n1.value),Number(n2.value)));
    })
}
/*
let value: Array<number>;
value =  [1,2,3,4,5,6];

let tupla: [boolean,string,number];
tupla = [true,"duro",31];

enum Cores{
    verde = 'verdinho',
    vermelho = 'vermelhinho',
    azul = 'azulzinho'
}
*/
