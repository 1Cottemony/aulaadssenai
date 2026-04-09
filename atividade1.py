while True:
    try:
        numero = int(input("Entre com um número: "))
        print(2/numero)
        break
    except (ValueError, ZeroDivisionError):
        print("Valor Errado ou valor divizão por zero")
    except:
        print("Não sei o que fazer")        
    #except ZeroDivisionError:
        #print("Não posso dividir por zero")
#print("Entre com um número válido.")
                             


