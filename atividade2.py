try:
    file = open("arquivo.txt","r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado")
finally:
    #Este bloco sempre é executado
    print("Finalizando a Operação")
    if 'file' in locals() and not file.close:
        file.close()
        print("Arquivo fechado com sucesso!")