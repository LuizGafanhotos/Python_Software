type Bla = string | undefined;

//never
function error(): never {
    throw new Error("error")
}

//objetc : objeto

let cart: object;

cart = {
    key: "fi",
}

//mensagem
let mensagem = "Ola prastiranhas"