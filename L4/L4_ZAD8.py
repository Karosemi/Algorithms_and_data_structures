"""
Zaprojektuj i przeprowadź eksperyment porównujący wydajność listy jednokierunkowej i listy wbudowanej w Pythona.

Prosiłabym o chwilę cierpliwości (kilka sekund) na wykonanie sie testu, ponieważ jest to test wydajnościowy.
Metody zastosowane w teście wyświetlają to co usunęły stąd może jest pojawić trochę printów. Na samym dole pojawi sie
komunikat z testu.
"""
import time

import numpy as np

from L4_ZAD5 import UnorderedList

def test_01_compare_capability():
    #najpierw dodam 1000 elementow do listy, po kazdym dodaniu sprawdze rozmiar i znajduje ten element,
    #nastepnie dodaje kolejny element na koniec kolejki i znajduje jego indeks, umieszczam kolejny element na pozycji i +1,
    # i wyrzucam i-ty element z listy i pierwszy element
    #sprawdzam w powyższy sposób szybkość działania obu list za pomocą modułu time
    n = 1000
    iter = 25
    un_times = []
    for k in range(iter):
        un_beg_time = time.time()
        unordered_list = UnorderedList()
        for i in range(n):
            element = str(i)
            unordered_list.add(element)
            unordered_list.search(element)
            unordered_list.append(element)
            unordered_list.index(element)
            unordered_list.insert(i+1, element)
            unordered_list.pop()
            unordered_list.pop(i)
        un_end_time = time.time()
        un_time = un_end_time - un_beg_time
        un_times.append(un_time)
    py_times = []
    for k in range(iter):
        py_beg_time = time.time()
        python_list = list()
        for i in range(n):
            element = str(i)
            python_list.insert(0, element)
            element in python_list
            python_list.append(element)
            python_list.index(element)
            python_list.insert(i+1, element)
            python_list.pop()
            python_list.pop(i)
        py_end_time = time.time()
        py_time = py_end_time - py_beg_time
        py_times.append(py_time)

    un_mean = np.mean(un_times)
    un_std = np.std(un_times)
    py_mean = np.mean(py_times)
    py_std = np.std(py_times)
    print(f"Test 1: Średni czas wykonywania się poleceń w liście jednokierunkowej to: {un_mean} sekund. \r\n"
          f"        Odchylenie standardowe wynosi: {un_std}.\r\n"
          f"Test 1: Średni czas wykonywania się poleceń w liście pythonowej to: {py_mean} sekund. \r\n"
          f"        Odchylenie standardowe wynosi: {py_std}.\r\n"
          f"Test 1: Czy pythonowa lista jest szybsza? {py_mean < un_mean}")