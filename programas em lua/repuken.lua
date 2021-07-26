function pular(intensidade)
    print("vou pular com a intensidade " .. toString(intensidade))
end

function calcFisica(forca)
    return forca * 0.5 + 32.98 / 4
end

function calcFormSecreta(senha)
    print("Calcularei a forma secreta do pulo...")
    return senha + 1
end

pular(calcFisica(13.5) + calcFormSecreta(987))