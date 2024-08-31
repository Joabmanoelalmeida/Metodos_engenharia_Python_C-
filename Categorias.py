def categoria(a):
    if a > 25:
        return "Senior"
    elif a < 25 and a > 20:
        return "Master"
    else:
        return "Junior"
    
idade = float(input("Digite a sua idade: "))
categoria_ = categoria(idade)

print(f"A sua categoria é: {categoria_}")
    