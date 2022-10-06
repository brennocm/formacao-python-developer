def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}")

def exibir_mensagem_3(nome='Anônimo'):
    print(f"Seja bem vindo {nome}")

exibir_mensagem()
exibir_mensagem_2(nome="Brenno")
exibir_mensagem_3()
exibir_mensagem_3(nome="Cavalcante")

## --

def calcular_total(numeros):
    return print(sum(numeros))

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return print(antecessor, sucessor)

calcular_total([10, 20, 34])
calcular_total([10, 10])
retorna_antecessor_e_sucessor(10)

# --

def salvar_livro(nome_autor, titulo):
    print(f"Livro salvado com sucesso! {nome_autor} / {titulo}")

salvar_livro(nome_autor="Machado de Assis", titulo="Quincas Borba")
salvar_livro("Liev Tolstoi", "Guerra e Paz")

# --

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("\nZen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)