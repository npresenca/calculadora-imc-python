classe = {
    "Abaixo do peso": "Você está abaixo do peso. Procure um nutricionista!",
    "Peso normal": "Você está com peso normal. Parabéns!",
    "Sobrepeso": "Você está com sobrepeso. Atenção!",
    "Acima do peso": "Você está acima do peso."

}

peso = float(input("Digite o seu peso (kg): "))
altura_cm = float(input("Digite a sua altura (cm): "))

altura_m = altura_cm / 100
imc = peso / (altura_m * altura_m)

if imc <= 18.5:
    faixa = "Abaixo do peso"
elif imc <= 24.9:
    faixa = "Peso normal"
elif imc <= 29.9:
    faixa = "Sobrepeso"
else:
    faixa = "Acima do peso"

print(f"\nIMC: {imc:.2f}")
print(f"Classificação: {faixa}")
print(classe[faixa])
