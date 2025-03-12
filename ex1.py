def obter_temperatura(mensagem):
    while True:
        try:
            temperatura = float(input(mensagem))
            return temperatura
        except ValueError:
            print("Valor informado é inválido. Por favor, insira um número decimal.")

def calcular_media(temperatura_maxima, temperatura_minima):
    return (temperatura_maxima + temperatura_minima) / 2

def calcular_variacao(temperatura_maxima, temperatura_minima):
    return temperatura_maxima - temperatura_minima

def soma_digitos(numero):
    if not isinstance(numero, int):
        return "Valor informado é inválido. Por favor, insira um número inteiro."
    
    return sum(int(digito) for digito in str(abs(numero)))

def main():
    print("Avaliador de Temperatura")
    
    # Obter temperaturas
    temperatura_maxima = obter_temperatura("Informe a temperatura máxima do dia: ")
    temperatura_minima = obter_temperatura("Informe a temperatura mínima do dia: ")
    
    # Calcular média e variação
    media = calcular_media(temperatura_maxima, temperatura_minima)
    variacao = calcular_variacao(temperatura_maxima, temperatura_minima)
    
    # Exibir resultados
    print(f"A média entre atemperatura máxima e mínima é: {media:.2f}")
    print(f"A variação entre as temperaturas é: {variacao:.2f}")
    
    # Obter número para soma dos dígitos
    numero = input("Informe um número inteiro para calcular a soma dos dígitos: ")
    
    try:
        numero_inteiro = int(numero)
        resultado_soma = soma_digitos(numero_inteiro)
        print(f"A soma dos dígitos do número {numero_inteiro} é: {resultado_soma}")
    except ValueError:
        print("Valor informado é inválido. Por favor, insira um número inteiro.")

if __name__ == "__main__":
    main()