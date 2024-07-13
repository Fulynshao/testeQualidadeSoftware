""" Trabalho avaliativo de testes unitários """
""" Nome: Augusto de Souza Corrêa """
""" Curso: Análise e desenvolvimento de sistemas, 2024/01 """
import pytest

""" Operações matemáticas básicas """


def adicionar(x, y):
    """Adiciona dois números."""
    return x + y


def subtrair(x, y):
    """Subtrai o segundo número do primeiro."""
    return x - y


def multiplicar(x, y):
    """Multiplica dois números."""
    return x * y


def dividir(x, y):
    """Divide o primeiro número pelo segundo. Retorna None se o divisor for zero."""
    if y == 0:
        return None
    return x / y

@pytest.mark.parametrize("x, y, saida", [(2, 2, 4), # soma com inteiros
                                         (333, 888, 1221),
                                         (3.14, 2.71, 5.85), # soma com numeros em ponto flutuante
                                         (-1.5, 2.5, 1.0) # soma com numeros negativos
                                         ])
def test_adicao_inteiros(x, y, saida):
    """Testa a função de adição com valores inteiros, negativos e de ponto flutuante
    com objetivo de validar vários casos diferentes de soma"""
    assert adicionar(x, y) == saida