idade = int(input("Qual a sua idade? "))

if (idade < 16):
	print("Você não pode votar.")
else:
	zona = input("Qual a zona de Porto Alegre você mora? (oeste, leste, norte, sul ou centro) ").lower()

	if (zona == "oeste" or zona == "norte"):
		print("Você vota na escola UNIRITTER")
	elif (zona == "leste"):
		print("Você vota na escola PUCRS")
	elif (zona == "sul" or zona == "centro"):
		print("Você vota na escola UFRGS.")
	else:
		print("Insira uma zona válida.")
# Renato Barbosa
