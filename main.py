def num_para_romano(numero):
    """
    Converte um número inteiro para algarismo romano.

    Parâmetros:
        numero (int): O número inteiro a ser convertido.

    Retorna:
        str: O algarismo romano correspondente ao número fornecido.
    """
    lista_num = []
    
    while numero > 0:
        if numero >= 1000:
            numero -= 1000
            lista_num.append('M')
        elif numero >= 900:
            numero -= 900
            lista_num.append('CM')
        elif 500 <= numero < 1000:
            numero -= 500
            lista_num.append('D')
        elif numero >= 400:
            numero -= 400
            lista_num.append('CD')
        elif 100 <= numero < 500:
            numero -= 100
            lista_num.append('C')
        elif numero >= 90:
            numero -= 90
            lista_num.append('XC')
        elif 50 <= numero < 100:
            numero -= 50
            lista_num.append('L')
        elif numero >= 40:
            numero -= 40
            lista_num.append('XL')
        elif 10 <= numero < 50:
            numero -= 10
            lista_num.append('X')
        elif numero >= 9:
            numero -= 9
            lista_num.append('IX')
        elif 5 <= numero < 10:
            numero -= 5
            lista_num.append('V')
        elif numero >= 4:
            numero -= 4
            lista_num.append('IV')
        else:
            numero -= 1
            lista_num.append('I')
        
    return ''.join(lista_num)


def romano_para_num(numero):
    """
    Converte um algarismo romano para número inteiro.

    Parâmetros:
        numero (str): O algarismo romano a ser convertido.

    Retorna:
        int: O número inteiro correspondente ao algarismo romano fornecido.
    """
    final_answer = 0
    numeral = numero.upper()  # Converte para maiúsculas para garantir a correspondência correta

    for i in numeral:
        if i == "M":
            final_answer += 1000
        elif i == "D":
            final_answer += 500
        elif i == "C":
            final_answer += 100
        elif i == "L":
            final_answer += 50
        elif i == "X":
            final_answer += 10
        elif i == "V":
            final_answer += 5
        elif i == "I":
            final_answer += 1

    # Lógica para tratar os casos especiais (subtração)
    if "CM" in numeral:
        final_answer -= 200  # 1000 - 100 = 900
    if "CD" in numeral:
        final_answer -= 200  # 500 - 100 = 400
    if "XC" in numeral:
        final_answer -= 20   # 100 - 10 = 90
    if "XL" in numeral:
        final_answer -= 20   # 50 - 10 = 40
    if "IX" in numeral:
        final_answer -= 2    # 10 - 1 = 9
    if "IV" in numeral:
        final_answer -= 2    # 5 - 1 = 4
    
    return final_answer

def titulo():
    """
    Exibe o menu principal e solicita a escolha do usuário.
    """
    print('''
      \033[1;36mConversor de Numerais Romanos\033[0m
      
      Selecione qual opcao voce deseja:
      [1] Converter um número para algarismo romano
      [2] Converter um algarismo romano para número
      
      ''')
    opcao_escolhida = int(input("Digite qual sua opcao desejada: "))
    
    if opcao_escolhida == 1:
        numero_vlr = int(input('Digite o número que gostaria de converter para algarismo romano: '))
        print(num_para_romano(numero_vlr))
    elif opcao_escolhida == 2:
        romano_vlr = input('Digite o algarismo romano que gostaria de converter para número: ')
        print(romano_para_num(romano_vlr))

def main():
    titulo()
    

if __name__ == '__main__':
    main()