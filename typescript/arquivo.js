var n1 = document.querySelector("input#input1");
var n2 = document.querySelector("input#input2");
var oi = document.querySelector("button#buton");
function sub(v1, v2) {
    return v1 - v2;
}
if (oi) {
    oi.addEventListener("click", function () {
        console.log(sub(Number(n1.value), Number(n2.value)));
    });
}
