# ============================================
# EXERCÍCIO 1: Remover o primeiro elemento
# ============================================
# Você tem uma lista de tuplas com (nome, idade, cidade)
# Remova a idade (índice 1) de cada tupla e retorne uma string
# com cada tupla limpa em uma linha

def remove_age(people):
    cleaned_version = [str(i[:1] + i[2:]) + "\n" for i in people]
    return "".join(cleaned_version)
    """
    Input: (('João', 25, 'SP'), ('Maria', 30, 'RJ'))
    Output: "('João', 'SP')\n('Maria', 'RJ')\n"
    """


# ============================================
# EXERCÍCIO 2: Pegar só números pares
# ============================================
# Use list comprehension para filtrar apenas números pares
# e retornar uma lista

def get_even_numbers(numbers):
    return [i for i in numbers if i % 2 == 0]
    """
    Input: [1, 2, 3, 4, 5, 6, 7, 8]
    Output: [2, 4, 6, 8]
    """
    pass


# ============================================
# EXERCÍCIO 3: Remover primeiro e último
# ============================================
# De cada tupla, remova o primeiro E o último elemento
# Retorne uma string com cada tupla limpa em uma linha

def remove_first_and_last(records):
    firt_last = [str(r[1:-1]) + "\n" for r in records]
    return "".join(firt_last)
    """
    Input: (('A', 'B', 'C', 'D'), ('1', '2', '3', '4'))
    Output: "('B', 'C')\n('2', '3')\n"
    """
    pass


# ============================================
# EXERCÍCIO 4: Transformar coordenadas
# ============================================
# Você tem tuplas com coordenadas separadas: ('2', 'A')
# Junte elas em uma string '2A' para cada tupla
# Retorne uma lista de strings

def join_coordinates(coord_list):
    return [i[0] + i[1] for i in coord_list]
    
    """
    Input: [('2', 'A'), ('5', 'B'), ('8', 'C')]
    Output: ['2A', '5B', '8C']
    """
    pass


# ============================================
# EXERCÍCIO 5: Filtrar e limpar (DESAFIO!)
# ============================================
# Você tem tuplas com (nome, preço, categoria)
# Remova o preço (índice 1) MAS só de produtos da categoria 'eletrônicos'
# Retorne uma string com as tuplas limpas, uma por linha

def filter_and_clean(products):
    filter = [str(i[:1] + i[2:]) + "\n" for i in products if i[2] == "eletrônicos"]
    return "".join(filter)
    """
    Input: (('Mouse', 50, 'eletrônicos'), ('Cadeira', 300, 'móveis'), ('Teclado', 150, 'eletrônicos'))
    Output: "('Mouse', 'eletrônicos')\n('Teclado', 'eletrônicos')\n"
    
    Dica: você pode usar 'if' dentro da list comprehension!
    [item for item in lista if condição]
    """
    pass


# ============================================
# TESTES - Cole isso no final do arquivo
# ============================================
if __name__ == "__main__":
    print("=== TESTE 1 ===")
    result1 = remove_age((('João', 25, 'SP'), ('Maria', 30, 'RJ')))
    print(result1)
    print("Esperado: \"('João', 'SP')\\n('Maria', 'RJ')\\n\"")
    
    print("\n=== TESTE 2 ===")
    result2 = get_even_numbers([1, 2, 3, 4, 5, 6, 7, 8])
    print(result2)
    print("Esperado: [2, 4, 6, 8]")
    
    print("\n=== TESTE 3 ===")
    result3 = remove_first_and_last((('A', 'B', 'C', 'D'), ('1', '2', '3', '4')))
    print(result3)
    print("Esperado: \"('B', 'C')\\n('2', '3')\\n\"")
    
    print("\n=== TESTE 4 ===")
    result4 = join_coordinates([('2', 'A'), ('5', 'B'), ('8', 'C')])
    print(result4)
    print("Esperado: ['2A', '5B', '8C']")
    
    print("\n=== TESTE 5 ===")
    result5 = filter_and_clean((('Mouse', 50, 'eletrônicos'), ('Cadeira', 300, 'móveis'), ('Teclado', 150, 'eletrônicos')))
    print(result5)
    print("Esperado: \"('Mouse', 'eletrônicos')\\n('Teclado', 'eletrônicos')\\n\"")