motos=["HRV","Apollo","Thanatus","Jetta","Cruzes"]

itMotos = iter(motos)

while itMotos:
    try:
        print(next(itMotos))
    except StopIteration:
        break