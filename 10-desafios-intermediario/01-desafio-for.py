exclama_inseto = "Inseto!"
exclama_8000 = "Mais de 8000!"

C = int(input()) 
for i in range (C): 
    analise = int(input())

    if analise <= 8000:
        print(exclama_inseto)
    else:
        print(exclama_8000)