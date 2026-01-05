"""
10 Exercícios de Dicionários e Inventário
Rode com: pytest exercicios.py -v
"""

# ============================================================================
# EXERCÍCIO 1 – Frequência de palavras
# ============================================================================

def word_frequency(words):
    d = {}
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1


# ============================================================================
# EXERCÍCIO 2 – Mesclar inventários
# ============================================================================

def merge_inventories(inv_a, inv_b):
    return inv_a | inv_b


# ============================================================================
# EXERCÍCIO 3 – Normalizar inventário (remover zeros e negativos)
# ============================================================================

def normalize_inventory(inventory):
    """
    Recebe um dicionário {item: quantidade} e:
      - remove itens com quantidade <= 0
    Retorna um novo dicionário (não modifica o original).
    """
    pass  # seu código aqui


# ============================================================================
# EXERCÍCIO 4 – Inverter dicionário simples
# ============================================================================

def invert_mapping(mapping):
    """
    Recebe um dicionário {chave: valor} onde os valores são únicos
    e retorna um novo dicionário {valor: chave}.
    """
    pass  # seu código aqui


# ============================================================================
# EXERCÍCIO 5 – Agrupar por quantidade
# ============================================================================

def group_by_quantity(inventory):
    """
    Recebe um dicionário {item: quantidade}
    e retorna outro dicionário {quantidade: [itens_com_essa_quantidade]}.
    A lista de itens pode estar em qualquer ordem.
    """
    pass  # seu código aqui


# ============================================================================
# EXERCÍCIO 6 – Top N itens mais abundantes
# ============================================================================

def top_n_items(inventory, n):
    """
    Recebe um inventário {item: quantidade} e um inteiro n.
    Retorna uma lista de tuplas (item, quantidade) com os n itens
    de maior quantidade, em ordem decrescente de quantidade.
    Em caso de empate, não precisa ordenar por nome.
    Se n > número de itens, retorna todos.
    """
    pass  # seu código aqui


# ============================================================================
# EXERCÍCIO 7 – Aplicar transações no inventário
# ============================================================================

def apply_transactions(inventory, transactions):
    """
    `inventory`: dict {item: quantidade_atual}
    `transactions`: lista de tuplas (item, delta)
        - delta > 0 -> adicionar
        - delta < 0 -> remover
    Deve aplicar todos os deltas, sem deixar quantidade negativa.
    Retorna o próprio inventário modificado.
    """
    pass  # seu código aqui


# ============================================================================
# EXERCÍCIO 8 – Converter lista de pares em inventário válido
# ============================================================================

def to_inventory(pairs):
    """
    Recebe uma lista de tuplas (item, quantidade) possivelmente
    com itens repetidos, e retorna um dicionário somando as quantidades
    de itens iguais.
    Ex: [("wood", 1), ("coal", 2), ("wood", 3)] -> {"wood": 4, "coal": 2}
    """
    pass  # seu código aqui


# ============================================================================
# EXERCÍCIO 9 – Inventário suficiente para crafting
# ============================================================================

def can_craft(recipe, inventory):
    """
    `recipe`: dict {item: quantidade_necessaria}
    `inventory`: dict {item: quantidade_disponivel}
    Retorna True se o inventário tem quantidade suficiente
    de todos os itens da receita, senão False.
    Não modifica os dicionários.
    """
    pass  # seu código aqui


# ============================================================================
# EXERCÍCIO 10 – Aplicar crafting no inventário
# ============================================================================

def craft(recipe, inventory):
    """
    Usa `can_craft` como pré-condição.
    Se for possível craftar (inventário suficiente), retorna um novo
    inventário com as quantidades decrementadas.
    Se não for possível, retorna None.
    Não deve modificar o inventário original.
    """
    pass  # seu código aqui


# ============================================================================
# TESTES
# ============================================================================

def test_word_frequency_basic():
    words = ["a", "b", "a", "c", "b", "a"]
    assert word_frequency(words) == {"a": 3, "b": 2, "c": 1}


def test_word_frequency_empty():
    assert word_frequency([]) == {}


def test_word_frequency_single():
    assert word_frequency(["python"]) == {"python": 1}


def test_merge_basic():
    inv_a = {"wood": 2, "coal": 1}
    inv_b = {"wood": 3, "diamond": 1}
    result = merge_inventories(inv_a, inv_b)
    assert result == {"wood": 5, "coal": 1, "diamond": 1}
    # garante que originais não mudaram
    assert inv_a == {"wood": 2, "coal": 1}
    assert inv_b == {"wood": 3, "diamond": 1}


def test_merge_with_empty():
    assert merge_inventories({}, {"a": 1}) == {"a": 1}
    assert merge_inventories({"a": 1}, {}) == {"a": 1}


def test_normalize_basic():
    inv = {"wood": 2, "coal": 0, "diamond": -1}
    result = normalize_inventory(inv)
    assert result == {"wood": 2}
    assert inv == {"wood": 2, "coal": 0, "diamond": -1}


def test_normalize_all_removed():
    inv = {"a": 0, "b": -2}
    assert normalize_inventory(inv) == {}


def test_invert_basic():
    m = {"a": 1, "b": 2, "c": 3}
    assert invert_mapping(m) == {1: "a", 2: "b", 3: "c"}


def test_invert_strings():
    m = {"x": "y", "foo": "bar"}
    assert invert_mapping(m) == {"y": "x", "bar": "foo"}


def test_group_basic():
    inv = {"wood": 2, "coal": 1, "diamond": 2}
    result = group_by_quantity(inv)
    # ordem das listas não importa
    assert result[1] == ["coal"]
    assert set(result[2]) == {"wood", "diamond"}


def test_group_single():
    inv = {"wood": 5}
    assert group_by_quantity(inv) == {5: ["wood"]}


def test_top_n_basic():
    inv = {"wood": 5, "coal": 1, "diamond": 3}
    assert top_n_items(inv, 2) == [("wood", 5), ("diamond", 3)]


def test_top_n_bigger_than_size():
    inv = {"wood": 5, "coal": 1}
    result = top_n_items(inv, 10)
    # pode estar em qualquer ordem, desde que todos estejam lá
    assert set(result) == {("wood", 5), ("coal", 1)}


def test_apply_transactions_basic():
    inv = {"wood": 5, "coal": 1}
    txs = [("wood", -2), ("coal", 3), ("diamond", 1)]
    result = apply_transactions(inv, txs)
    assert result == {"wood": 3, "coal": 4, "diamond": 1}
    assert inv is result  # mesma referência


def test_apply_transactions_no_negative():
    inv = {"wood": 1}
    txs = [("wood", -5)]
    result = apply_transactions(inv, txs)
    assert result["wood"] == 0


def test_to_inventory_basic():
    pairs = [("wood", 1), ("coal", 2), ("wood", 3)]
    assert to_inventory(pairs) == {"wood": 4, "coal": 2}


def test_to_inventory_empty():
    assert to_inventory([]) == {}


def test_can_craft_true():
    recipe = {"wood": 3, "iron": 1}
    inv = {"wood": 5, "iron": 2, "coal": 10}
    assert can_craft(recipe, inv) is True


def test_can_craft_false_missing_item():
    recipe = {"wood": 3, "diamond": 1}
    inv = {"wood": 5}
    assert can_craft(recipe, inv) is False


def test_can_craft_false_not_enough_quantity():
    recipe = {"wood": 3}
    inv = {"wood": 2}
    assert can_craft(recipe, inv) is False


def test_craft_success():
    recipe = {"wood": 3, "iron": 1}
    inv = {"wood": 5, "iron": 2, "coal": 10}
    result = craft(recipe, inv)
    assert result == {"wood": 2, "iron": 1, "coal": 10}
    assert inv == {"wood": 5, "iron": 2, "coal": 10}  # original intacto


def test_craft_fail():
    recipe = {"wood": 3, "diamond": 1}
    inv = {"wood": 5}
    result = craft(recipe, inv)
    assert result is None 