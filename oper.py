velocidade = int(input("Digite a velocidade  atual: "))

if velocidade > 110:
    print("Acima da velocidade permitida!")
    print("Reduza a velocidade!")
elif velocidade < 60:
    print("Está muito lento, Favor dirigir acima de 80km")
else:
    print("Velocidade OK!")
