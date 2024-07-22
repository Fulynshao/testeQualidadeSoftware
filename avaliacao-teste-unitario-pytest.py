""" Trabalho avaliativo de testes unitários """
""" Nome: Augusto de Souza Corrêa """
""" Curso: Análise e desenvolvimento de sistemas, 2024/01 """
import pytest
import math

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

# Testes para a função adicionar
@pytest.mark.parametrize("x, y, saida", [
    (1, 2, 3),
    (111, 222, 333),
    (1237765, 97987, 1335752)
])
def test_deveSomarCorretamenteDoisNumerosInteiros(x, y, saida):
    """ Esse teste tem como objetivo garantir que a soma de valores inteiros funcione corretamente,
    com mais de um caso.
    """
    assert adicionar(x, y) == saida

@pytest.mark.parametrize("x, y, saida", [
    (1.1, 2.2, 3.3),
    (14.24, 53.67, 67.91),
    (4524.5623, 12356.8733, 16881.4356)
])
def test_deveSomarCorretamenteDoisNumerosPontoFlutuante(x, y, saida):
    """ Já esse garante que a soma de números com ponto flutuante esteja ok, testando três casos diferentes,
    a tolerância é de 0,000000001 (uma em um bilhão).
    """
    saida_soma = adicionar(x, y)
    assert math.isclose(saida_soma, saida, rel_tol=1e-9)

@pytest.mark.parametrize("x, y, saida", [
    (-354, -678, -1032), 
    (-445.22, 112667, 112221.78),
    (-2, 7, 5)
])
def test_deveSomarCorretamenteDoisNumerosNegativos(x, y, saida):
    """ O último teste da soma garante que números negativos se somem corretamente,
    com a mesma precisão dos de ponto flutuante.
    """
    saida_soma_negativos = adicionar(x, y)
    assert math.isclose(saida_soma_negativos, saida, rel_tol=1e-9)

@pytest.mark.parametrize("x, y", [
    ("peixe", 4), 
    (5, "sacola"), 
    (None, None)
])
def test_deveOcorrerUmErroQuandoHouverEntradasInvalidas(x, y):
    """ Esse teste tem como objetivo garantir que ocorram erros quando ocorrerem entradas inválidas na função de soma """
    with pytest.raises(TypeError):
        adicionar(x, y)

# Testes para a função subtrair
@pytest.mark.parametrize("x, y, saida", [
    (5, 2, 3),
    (-10, 3, -13),
    (12.5, 7.2, 5.3)
])
def test_deveSubtrairCorretamenteDoisValores(x, y, saida):
    """ Esse teste tem como objetivo garantir que os casos comuns de subtração (positivos, negativos e pontos flutuantes)
    sejam tratados corretamente pela função.
    """
    resultado = subtrair(x, y)
    assert resultado == saida

@pytest.mark.parametrize("x, y, saida", [
    (0, 0, 0),
    (1, 1, 0),
    (-100, 0, -100)
])
def test_deveSubtrairCorretamenteComCasosDeBorda(x, y, saida):
    """ Esses casos de teste têm como objetivo validar corretamente os casos de borda,
    como subtração de zero por zero, um número por ele mesmo, e por números negativos.
    """
    resultado = subtrair(x, y)
    assert resultado == saida

@pytest.mark.parametrize("x, y", [
    ("um", 1),
    (2, "dois"),
    ("três", None)
])
def test_deveOcorrerErroEmEntradaInvalidaAoSubtrair(x, y):
    """ Teste para garantir que entradas inválidas gerem um erro ao subtrair """
    with pytest.raises(TypeError):
        subtrair(x, y)

# Testes para a função multiplicar
@pytest.mark.parametrize("x, y, saida", [
    (2, 3, 6),
    (-4, 5, -20),
    (12.5, 0.2, 2.5),
])
def test_deveMultiplicarCorretamenteDoisNumeros(x, y, saida):
    """ Esse teste garante que a multiplicação ocorra corretamente, com números positivos,
    negativos e de ponto flutuante, os casos comuns.
    """
    resultado = multiplicar(x, y)
    assert resultado == saida

@pytest.mark.parametrize("x, y, saida", [
    (0, 0, 0),
    (999, 1, 999),
    (-6533453, 0, 0)
])
def test_deveMultiplicarCorretamenteCasosDeBorda(x, y, saida):
    """ Este teste verifica se a função `multiplicar` se comporta corretamente em casos de borda, 
    como multiplicações que resultam em zero, um número por ele mesmo ou com números negativos.
    """
    resultado = multiplicar(x, y)
    assert resultado == saida

@pytest.mark.parametrize("x, y", [
    (None, 5),
    (5, None),
])
def test_deveOcorrerErroComEntradasInvalidasNaMultiplicacao(x, y):
    """ Teste para garantir que entradas inválidas gerem um erro ao multiplicar """
    with pytest.raises(TypeError):
        multiplicar(x, y)

# Testes para a função dividir
@pytest.mark.parametrize("x, y, saida", [
    (10, 2, 5.0), 
    (-4, 2, -2.0),
    (12.5, 0.5, 25.0),
])
def test_deveDividirCorretamenteNumeros(x, y, saida):
    """ Este teste verifica se a função dividir divide corretamente dois números, 
    cobrindo casos típicos com números inteiros e de ponto flutuante.
    """
    resultado = dividir(x, y)
    assert resultado == saida

@pytest.mark.parametrize("x, y, saida", [
    (1, 1, 1.0),
    (10, 0, None),
    (-100, 1, -100.0),
])
def test_deveDividirCorretamenteCasosDeBorda(x, y, saida):
    """ Este teste verifica se a função dividir se comporta corretamente em casos de borda, 
    como divisão por um, divisão por zero e divisão de números negativos por positivos.
    """
    resultado = dividir(x, y)
    assert resultado == saida

@pytest.mark.parametrize("x, y", [
    ("string", 2342),
    (11699, "string"),
])
def test_deveOcorrerErroComEntradasInvalidasNaDivisao(x, y):
    """ Verifica se a função dividir levanta uma exceção TypeError
    quando recebe entradas inválidas.
    """
    with pytest.raises(TypeError):
        dividir(x, y)
