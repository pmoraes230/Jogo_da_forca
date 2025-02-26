import random

comida = [
    'Lasanha',
    'Churrasco',
]

animal = [
    'Cachorro',
    'Gato',
]

paises = [
    'França',
    'Alemanha',
]

linguagem_programacao = [
    'Javascript',
    'Assembly',
]

categorias = {
    'Comida': comida,
    'Animal': animal,
    'Países': paises,
    'Linguagem de Programação': linguagem_programacao
}

todas_palavras = []
for categoria, palavras in categorias.items():
    for palavra in palavras:
        todas_palavras.append((palavra, categoria))
    print(todas_palavras)

palavra_aleatoria, categoria_aleatoria = random.choice(todas_palavras)