class Livro:
    def __init__(self, nome, autor, editora):
        self.nome = nome
        self.autor = autor
        self.editora = editora

# --

class Livro:
    def __del__(self):
        print("Destruindo...")
        
l = Livro()
del l