# ÍNDICE DE MASSA CORPORAL — Desenvolva uma lógica que leia o peso e a altura de uma
# pessoa, calcule seu IMC e mostre seu estado, conforme a tabela abaixo:
#
# — Abaixo de 18,5: Abaixo do peso
# — Entre 18,5 e 25: Peso ideal
# — Entre 25 e 30: Sobrepeso
# — Entre 30 e 40: Obesidade
# — Acima de 40: Obesidade mórbida

peso = float(input('Digite o seu peso, em kg: '))
altura = float(input('Digite a sua altura, em m: '))
imc = peso / (altura ** 2)

print('\nVocê tem um IMC de {:.1f}. '.format(imc), end='')
if imc < 18.5:
    print('Portanto, você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Portanto, você está em um peso ideal.')
elif 25 <= imc < 30:
    print('Portanto, você está em sobrepeso.')
elif 30 <= imc < 40:
    print('Portanto, você tem obesidade.')
else:
    print('Portanto, você tem obesidade mórbida.')
