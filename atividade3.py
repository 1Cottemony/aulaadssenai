def salvar_novo_registro():
    arquivo = None
    try:
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        arquivo = open("registro.txt", "a", encoding="utf-8")
        arquivo.write("Nome: ", nome, "|", "Idade: ", idade, "\n")
        print("Dados salvos com sucesso!")
    except ValueError:
        print("Digite um número válido.")
    except IOError as e:
        print("Não foi possível gravar o arquivo.", e)   
    except Exception as e:
        print("Ocorreu um erro inesperado.", e)   
    finally:
        if arquivo:
            arquivo.close()
            print("arquivo fechado com sucesso!")