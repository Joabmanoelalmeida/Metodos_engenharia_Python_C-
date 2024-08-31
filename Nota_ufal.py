def media(x,y):
    s = (x + y)/2
    return s

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

soma = media(nota1, nota2)
print(f"A media da nota 1: {nota1} e nota2: {nota2} vale {soma}.")

if soma >= 7:
    print("Aprovado, parabéns!")
elif soma < 7 and soma >= 5:
    print(f"recuperação")
else: 
    print("reprovado")
    