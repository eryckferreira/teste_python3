notaAluno = int(input("Digite a nota do aluno: "))

if notaAluno >= 9:
    print("Excelente, você tirou um A")
elif notaAluno >= 7:
    print("Bom trabalho, você tirou um B")
elif notaAluno >= 5:
    print("Você passou, mas precisa melhorar, sua nota é C")
else:
    print("Você está REPROVADO!")