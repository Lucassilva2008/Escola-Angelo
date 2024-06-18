# with open('arquivo.txt', 'r') as arquivo:
#    conteudo = arquivo.read()
   # linhas = arquivo.readlines()
   # for linha in arquivo:
        # processa cada linha individualmente
        # pass
    
    
with open('arquivo.txt', 'w') as arquivo:
    arquivo.write("Ola, mundo!\n")
    arquivo.write("Estou Aqui!\n")
    linhas = ['Proxima linha', 'Outra linha']
    arquivo.writelines(linhas)

    arquivo = open('teste2.txt', 'w')
    arquivo.write(texto)
    arquivo.write("\nOutra linha \n")
    arquivo.write


