import random
import string
from time import sleep
import os


# Generate password function
def generate_pw(length, uppercase=True, lowercase=True, numbers=True, symbols=True):
    characters = ""

    if uppercase:
        characters += string.ascii_uppercase

    if lowercase:
        characters += string.ascii_lowercase

    if numbers:
        characters += string.digits

    if symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("Por favor, escolha ao menos uma opção.")

    pw = "".join(random.choice(characters) for _ in range(length))

    return pw


# Number warning
def only_num():
    print('\nPor favor, utilize apenas números inteiros.')
    sleep(3)
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# User choice condition
def get_user_choice(prompt):
    while True:
        choice = input(prompt + " (s/n): ").lower()
        if choice in ['s', 'n']:
            return choice == 's'
        else:
            print("\nEntrada inválida! Por favor, digite 's' para sim ou 'n' para não.")
            sleep(3)
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print("*"*20, "GERADOR DE SENHAS", "*"*20, "\n")


# Main function
def main():
    while True:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print("*"*20, "GERADOR DE SENHAS", "*"*20, "\n")
        try:
            lenght_input = input("Digite um comprimento para a sua senha: ")
            lenght = int(lenght_input)
            if lenght > 0:
                include_uppercase = get_user_choice(
                    "Incluir letras maiúsculas?")
                include_lowercase = get_user_choice(
                    "Incluir letras minúsculas?")
                include_numbers = get_user_choice("Incluir números?")
                include_symbols = get_user_choice("Incluir símbolos?")
                break
            else:
                print("\nPor favor, digite um número maior que zero.")
                sleep(3)
        except ValueError:
            only_num()

    try:
        password = generate_pw(
            lenght, include_uppercase, include_lowercase, include_numbers, include_symbols)
        print(f"\nA sua senha gerada é: {password}\n")

        while True:
            new_pw = input("Deseja gerar uma nova senha? (s/n): ")
            if new_pw == 's':
                print(f"\nReiniciando...")
                sleep(3)
                if os.name == "nt":
                    os.system("cls")
                else:
                    os.system("clear")
                main()

            elif new_pw not in ['s', 'n']:
                print(
                    "\nEntrada inválida! Por favor, digite 's' para sim ou 'n' para não.")
                sleep(3)
                if os.name == "nt":
                    os.system("cls")
                else:
                    os.system("clear")
                print("*"*20, "GERADOR DE SENHAS", "*"*20, "\n")

            elif new_pw == 'n':
                print("\nObrigado por utilizar o gerador de senhas...\nAté mais!")
                sleep(3)
                break
            break

    except ValueError:
        print("\nPor favor, selecione pelo menos um tipo de caractere e tente novamente.")
        sleep(3.5)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        main()


if __name__ == "__main__":
    main()
