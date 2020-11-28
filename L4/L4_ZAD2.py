
"""
Zaprojektuj i przeprowadź eksperyment porównujący wydajność implementacji kolejek QueueBaB i QueueBaE.
Prosiłabym o chwilę cierpliwości na wykonanie testów, ponieważ są one wydajnościowe. Po wykonaniu testu wyświetli się
komunikat z wynikiem.
"""
from time import time

from numpy import mean, std

from L4_ZAD1 import QueueBaB, QueueBaE


def test_01_check_which_enqueue_is_faster():
    """
    Test porownuje szybkość działania dodawania nowych elementów do kolejki.
       Dodając pojedyńczy element czas działania byłby tak krótki, że możnaby nie zauważyć różnicy,
       jednak jeśli spróbuje dodać np. po 1000 elementów różnice w szybkości działania
       obu kolejek powinny być zauważalne.
    """

    n = 10000
    queue_b_a_b = QueueBaB()
    queue_b_a_e = QueueBaE()
    b_a_b_time = []
    b_a_e_time = []
    for k in range(15):
        begin = time()
        for i in range(n):
            queue_b_a_b.enqueue(i)
        end = time()
        b_a_b_time.append(end - begin)
        begin = time()
        for i in range(n):
            queue_b_a_e.enqueue(i)
        end = time()
        b_a_e_time.append(end - begin)
    b_a_e_mean = mean(b_a_e_time)
    b_a_e_mean_time = b_a_e_mean
    b_a_b_mean = mean(b_a_b_time)
    b_a_b_mean_time = b_a_b_mean
    b_a_e_std = std(b_a_e_time)
    b_a_b_std = std(b_a_b_time)
    print(f"Test 1: Średni czas dodawania elementu w kolejce BaB to: {b_a_b_mean}. Odchylenie standardowe wynosi: {b_a_b_std}")
    print(f"Test 1: Średni czas dodawania elementu w kolejce BaE to: {b_a_e_mean}. Odchylenie standardowe wynosi: {b_a_e_std}")
    print(f"Test 1: Czy w BaE elementy do kolejki średnio są dodawane szybciej? {b_a_e_mean < b_a_b_mean} ")
    b_a_b_time = []
    b_a_e_time = []
    for k in range(25):
        begin = time()
        while not queue_b_a_b.is_empty():
            queue_b_a_b.dequeue()
        end = time()
        b_a_b_time.append(end - begin)
        begin = time()
        while not queue_b_a_e.is_empty():
            queue_b_a_e.dequeue()
        end = time()
        b_a_e_time.append(end - begin)
    b_a_e_mean = mean(b_a_e_time)
    b_a_e_mean_time += b_a_e_mean
    b_a_b_mean = mean(b_a_b_time)
    b_a_b_mean_time += b_a_b_mean
    b_a_e_std = std(b_a_e_time)
    b_a_b_std = std(b_a_b_time)
    print(f"Test 1: Średni czas usuwania elementu w kolejce BaB to: {b_a_b_mean}. Odchylenie standardowe wynosi: {b_a_b_std}")
    print(f"Test 1: Średni czas usuwania elementu w kolejce BaE to: {b_a_e_mean}. Odchylenie standardowe wynosi: {b_a_e_std}")
    print(f"Test 1: Czy w BaE elementy do kolejki średnio są usuwane szybciej? {b_a_e_mean < b_a_b_mean} ")
    print(f"Test 1: Łączny średni czas dodawania i ściagania elementów w kolejce BaE to: {b_a_e_mean_time}, a w BaB: {b_a_b_mean_time}")
    print(f"Test 1: Czy w BaE elementy do kolejki średnio są dodawane i usuwane szybciej? {b_a_e_mean_time < b_a_b_mean_time} ")
