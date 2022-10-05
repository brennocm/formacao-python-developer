lista = []
lista.append(1)
lista.append("python")
lista.append([40, 30, 20])
print(lista)

lista.clear()
print(lista)

lista = [1, 'python', [40, 30, 20]]
lista2 = lista.copy()
print(lista2)
print(id(lista), id(lista2))
lista2[0] = 20
print(lista, lista2)

cores = ['Preto', 'Cinza', 'Branco']
print(cores.count('Vermelho'))
print(cores.count('Azul'))
print(cores.count('Preto'))
print(cores.count('preto'))

linguagens = ['python', 'C', 'PHP', 'Assembly']
print(linguagens)
linguagens.extend(['java', 'javascript'])
print(linguagens)

linguagens = ['python', 'C', 'PHP', 'Assembly']
print(linguagens.index("Assembly"))
print(linguagens.index("C"))

linguagens = ['python', 'C', 'PHP', 'Assembly']
linguagens.pop(1)
print(linguagens)

linguagens = ['python', 'C', 'PHP', 'Assembly']
linguagens.remove('Assembly')
print(linguagens)

linguagens = ['python', 'C', 'PHP', 'Assembly']
linguagens.reverse()
print(linguagens)

linguagens = ['python', 'C', 'PHP', 'Assembly']
linguagens.sort()
print(linguagens)
linguagens.sort(reverse=True)
print(linguagens)

linguagens = ['python', 'C', 'PHP', 'Assembly']
print(len(linguagens))


