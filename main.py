#Receiving information from user
number = int(input("Digite um número: \n"))

#Condition
if number < 0 or number == 0 :
    print("Número inválido")
else :
    if number == 1 :
        print("Não primo")
    if number > 1 :
        i = 2
        i = int(i)
        primo = True
        while i < number:
            if (number % i) == 0:
                primo = False
                break
            i += 1
        if primo:
            print("Primo")
        else:
            print("Não primo")
    else :
        print("Não primo")



