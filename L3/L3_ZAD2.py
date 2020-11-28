"""
Zadanie 2.
"""


def ordinary_polynomial_value_calc(coeff, arg):
    """
    :param coeff: lista współczynników wielomianu. type: list
    :param arg: argument, dla którego wyznaczamy wartość wielomianu. type: float or int
    :return: wartość wielomianu, suma mnożeń, suma dodawań. type: float or int, int, int
    """
    assert isinstance(coeff, list), 'Argument coeff musi być listą.'
    assert coeff, 'Lista współczynnikow nie może być pusta.'
    assert arg, 'Należy podać punkt, w którym wyznaczona zostanie wartosc wielomianu.'
    value = coeff[0] #wyraz wolny
    if not coeff: return value, 0, 0
    count_mult = 0
    count_add = 0
    temp = 1
    for i in range(1, len(coeff)):
        temp *= arg
        value += coeff[i]*temp
        count_add += 1
        count_mult += 2
    return value, count_mult, count_add



def smart_polynomial_value_calc(coeff, arg):
    """
    Metodą Hornera rekursywnie rozkładam wielomian do np. z postaci 2x^3+2x*2+x+5 do postaci ((2x-2)x-1)*x+5
    :param coeff: lista współczynników wielomianu. type: list
    :param arg: argument, dla którego wyznaczamy wartość wielomianu. type: float or int
    :return: wartość wielomianu, suma mnożeń, suma dodawań. type: float or int, int, int
    """
    assert isinstance(coeff, list), 'Argument coeff musi być listą.'
    assert coeff, 'Lista współczynnikow nie może być pusta.'
    assert arg, 'Należy podać argument, dla którego ma być wyznaczona wartość wielomianu.'
    if len(coeff) == 1: return coeff[0], 0, 0
    value = coeff[0] #wyraz wolny
    poly, count_mult, count_add = smart_polynomial_value_calc(coeff[1:], arg)
    value += poly * arg
    count_mult += 1
    count_add += 1
    return value,  count_mult, count_add
