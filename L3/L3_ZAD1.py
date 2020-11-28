"""
Zadanie 1.
Przekształcam sobie równanie dystrybuanty rozkłądu dwumianowego na takie, aby maksymalną ilość elementów mieć poza sumą -
zaoszczędzie to mnożeń. Po wyprowadzeniu wzór wygląda następujaco:
P(n, k) = (1-p)**n * (sum_i=0^k dwumian(n i)* (p/1-p)**i)

"""


def probability(n, k, p):
    assert 0 <= p <= 1, 'Prawdopodobieństwo musi być pomiędzy 0 a 1.'
    assert isinstance(n, int) and isinstance(k, int), 'n i k muszą być całkowite.'
    assert k <= n, 'Liczba sukcesów nie może być większa niż liczba prób'
    if n == 1 and k == 1: return p ,0
    if p == 0: return 0, 0 #jesli prawdopodobienstwo jest zerowe, to niewazne ile razy bedziemy próbować ;)
    if p == 1: return 1, 0 #jesli zdarzenie jest pewne, to wygramy zawsze.
    if n == 0 or k == 0: return 0, 0
    assert k > 0 or n > 0, 'Liczba prób i sukcesów musi być dodatnia.'
    triangle_row = pascal_triangle_row(n)
    odds = p/(1-p)
    count_mult = 1 #licznik mnożeń
    prob = 1 # wynik pierwszej iteracji - dwumian (n 0) daje 1 i odds**0 jest rowne 1
    temp = 1
    for i in range(1, k):
        temp *= odds
        prob += triangle_row[i]*temp
        count_mult += 2
    n_odd, count_mult = power((1-p), n, count_mult)
    prob *= n_odd
    count_mult += 1
    return prob, count_mult


def pascal_triangle_row(n):
    if n == 1: return [1]
    else:
        row = [1]
        for i in range(n):
            row = [1] + [sum(i) for i in zip(row, row[1:])]+[1]
    return row


def power(value, to_power, count_mult=0):
    """ Zlożoność obliczeniowa to maksymalnie log(n)"""
    if to_power == 1:
        return value, count_mult
    elif to_power == 0:
        return 1, count_mult
    temp, count_mult = power(value=value, to_power=int(to_power / 2), count_mult=count_mult)
    if to_power % 2 == 0:
        count_mult += 1
        return temp * temp, count_mult
    else:
        if to_power > 0:
            count_mult += 2  # linijke niżej mamy dwa mnożenia, ale po returnie juz nic nie policze
            return value * temp * temp, count_mult
        else:
            count_mult += 2  # linijke nizej jest mnozenie i dzielenie
            return temp * temp / value, count_mult