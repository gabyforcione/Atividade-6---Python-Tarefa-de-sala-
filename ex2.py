def soma_digitos(numero):
    return sum(int(digito) for digito in str(abs(numero)))

def main():
    numero = input("Informe um número inteiro: ")
    
    try:
        numero_inteiro = int(numero)
        resultado_soma = soma_digitos(numero_inteiro)
        print(f"A soma dos dígitos do número {numero_inteiro} é: {resultado_soma}")
    except ValueError:
        print("Valor informado é inválido. Por favor, insira um número inteiro.")

if __name__ == "__main__":
    main()