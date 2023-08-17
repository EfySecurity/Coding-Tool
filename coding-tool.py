import base64

# Cores ANSI
class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    ENDC = "\033[0m"

def encode(data):
    try:
        encoded_data = base64.b64encode(data.encode()).decode()
        return encoded_data
    except Exception as e:
        return f"{Colors.RED}Erro ao codificar: {e}{Colors.ENDC}"

def decode(encoded_data):
    try:
        decoded_data = base64.b64decode(encoded_data).decode()
        return decoded_data
    except Exception as e:
        return f"{Colors.RED}Erro ao decodificar: {e}{Colors.ENDC}"

def custom_operation(data):
    # Adicione sua operação personalizada aqui
    # Por exemplo: substituir vogais por números
    custom_data = data.replace('a', '4').replace('e', '3').replace('i', '1').replace('o', '0').replace('u', '9')
    return custom_data

while True:
    print(f"{Colors.BLUE}Escolha uma opção:")
    print("1. Encode")
    print("2. Decode")
    print("3. Operação Personalizada")
    print("4. Sair")
    
    choice = input()
    
    if choice == '1':
        data = input(f"{Colors.YELLOW}Digite os dados a serem codificados: {Colors.ENDC}")
        encoded_data = encode(data)
        print(f"{Colors.GREEN}Dados codificados:", encoded_data, f"{Colors.ENDC}")
    elif choice == '2':
        encoded_data = input(f"{Colors.YELLOW}Digite os dados codificados: {Colors.ENDC}")
        decoded_data = decode(encoded_data)
        print(f"{Colors.GREEN}Dados decodificados:", decoded_data, f"{Colors.ENDC}")
    elif choice == '3':
        data = input(f"{Colors.YELLOW}Digite os dados para a operação personalizada: {Colors.ENDC}")
        custom_data = custom_operation(data)
        print(f"{Colors.GREEN}Resultado da operação personalizada:", custom_data, f"{Colors.ENDC}")
    elif choice == '4':
        print(f"{Colors.BLUE}Saindo do script.{Colors.ENDC}")
        break
    else:
        print(f"{Colors.RED}Opção inválida. Escolha novamente.{Colors.ENDC}")
