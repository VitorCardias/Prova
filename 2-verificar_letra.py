# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula,
# além de informar a quantidade de vezes em que ela ocorre.

def verificar_letra(texto):
    texto = texto.lower()
    quantidade = 0

    if 'a' in texto:
        for letra in texto:
            if letra == 'a':
                quantidade += 1
        return  f"A letra 'a' aparece {quantidade} vezes no texto."

    else:
        return "A letra 'a' não foi encontrada no texto."

numero = input("Informe uma palavra ou frase: ")
print(verificar_letra(numero))