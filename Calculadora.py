print("Bem-vindo à calculadora do Mário!")

def calcule():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    numero_1 = int(input("Por favor, insira o primeiro número: "))
    numero_2 = int(input("Agora o segundo número: "))

    print("Os números escolhidos foram: ", numero_1, "e", numero_2)

    if operation == '+':
        print('{} + {} = '.format(numero_1, numero_2))
        print(numero_1 + numero_2)

    elif operation == '-':
        print('{} - {} = '.format(numero_1, numero_2))
        print(numero_1 - numero_2)

    elif operation == '*':
        print('{} * {} = '.format(numero_1, numero_2))
        print(numero_1 * numero_2)

    elif operation == '/':
        print('{} / {} = '.format(numero_1, numero_2))
        print(numero_1 / numero_2)

    else:
        print ("Você não digitou uma operação válida! Por favor, comece novamente.")

    again()

def again():

    # Take input from user
    calc_again = input('''
Você quer realizar um novo cáculo?
Por favor, digite S para SIM ou N para não.
''')

    # If user types Y, run the calculate() function
    if calc_again.upper() == 'S':
        calcule()

    # If user types N, say good-bye to the user and end the program
    elif calc_again.upper() == 'N':
        print('Até mais!')

    # If user types another key, run the function again
    else:
        again()

# Call calculate() outside of the function
calcule()