horarioAtual = int(input("Digite a hora atual, por gentiliza: "))

if horarioAtual < 12:
    print("Bom dia!")
elif horarioAtual < 18:
    print("Boa tarde!")
else:
    print("Boa noite!")
