peso = int(input("Digite o seu peso em kg: "))
altura_cm = float(input("Digite a sua altura em metros: "))

altura_m = altura_cm / 100
imc = peso / (altura_m * altura_m)

if imc <= 18.5:
    print("Está abaixo do peso.")
elif imc <= 24.9:
    print("Está com peso normal.")
elif imc <= 29.9:
    print("Está com sobrepeso.")
else:
    print("Está acima do peso.")

print(f"{imc:.2f}")
