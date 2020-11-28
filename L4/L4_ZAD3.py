"""
Rozważ sytuację z życia wziętą, np.: 
- auta w kolejce do myjni,
- kasy w supermarkecie,
- samoloty na pasie startowym, 
- okienko w banku. 
Postaw pytanie badawcze. Wykorzystując liniowe struktury danych 
zaprojektuj i przeprowadź symulację, która udzieli na nie odpowiedzi. 
Pamiętaj o określeniu wszystkich uproszczeń swojego modelu. 
Przyjazd szopa
Codziennie około godziny 10.30 do firmy przyjeżdza szop z kanapkami. Informacja ta
jest podawana na kanale jedzenie i wszyscy otrzymują tą wiadomość jednocześnie, jednak niekoniecznie
każdy przeczyta ją w tym samym czasie. Ponadto osoby informujące znajdują się parterze, więc z dużym prawdopodobieństwem
 jak pierwsi będą na miejscu. Osobom z drugiego piętra droga zajmuje za pewne około 2 minut. Jednak sama kolejka nie zaczyna
 się w drodze do szopa, a podczas transakcji zakupu produktu. Czas jednej transakcji to około 15-30 sekund lub 30-45 w zależności
 od tego czy płatność jest kartą czy gotówką. Ile czasu musi minąć od przyjazdu do wyjazdu szopa? 
 Założenia modelu:
 - czas oczekiwania na pierwszą transakcje od przyjazdu - około 5 minut
 - czas transakcji (podejscie, podanie kwoty, transakcja) - 15-30 lub 30-45 sekund na osobę
 - czas spakowania produktów do samochodu - około 5 minut
 Sprzedawca musi dokonywać transkacji kolejkowo. Osoba, która jest najbliżej sprzedawcy jest pierwsza w kolejce. Pierwsza osoba w 
 kolejce po zakonczeniu transkacji wychodzi z kolejki i pierwsza osoba w kolejce jest osoba za nia. Kolejka konczy sie w 
 momencie kiedy ostatnia osoba zostanie obsluzona. Osoba, która chce zapłacić ustawia sie wkolejce ostatnia, czyli najdalej
 od sprzedawcy. Celem symulacji jest wyznaczenie czasu pracy szopa w firmie. Zakładamy, że tylko ok. 10% osób zapłaci gotówką, 
 reszta kartą.
"""
from L4_ZAD1 import QueueBaB
import numpy as np

class SzopQueue:

    def __init__(self, customers):
        self.customers = customers
        self.time = 0
        self.queue = QueueBaB()

    def get_time(self):
        return self.time

    def serve_customer(self):
        while not self.queue.is_empty():
            self._dequeue_customer()
        self._finish()


    def add_customers(self):
        """ W modelu pomijam czasy ustawiania sie w kolejce, ponieważ interesuje
        mnie perspektywa ze strony sprzedawcy - dla niego kolejka jest czasu ciągłego,
        czyli nie ma momentu, w którym po odejściu jednego klienta nie czekałby koleny,
        aż do obsłużenia wszystkich klientów."""
        self._wait_for_first_cust()
        for customer in range(self.customers):
            self._add_customer_to_queue()

    def _wait_for_first_cust(self):
        self.time += np.random.uniform(4.75, 5.25)*60 # czas oczekiwania na pierwszego klienta to około 5 minut

    def _add_customer_to_queue(self):
        self.queue.enqueue('customer')

    def _dequeue_customer(self):
        if np.random.rand() > 0.1:
            self.time += np.random.uniform(15,30)
        else:
            self.time += np.random.uniform(30,45)
        self.queue.dequeue()

    def _finish(self):
        if self.queue.is_empty():
            self.time += np.random.uniform(4.75, 5.25)*60
        else:
            print('Kolejka nie jest pusta.')



if __name__ == '__main__':
    #Symulacja
    customers = 30
    queue = SzopQueue(customers=customers)
    queue.add_customers()
    queue.serve_customer()
    time = queue.get_time()
    print(f" Obsługa {customers} klientów w kolejce zajmuje około {int(np.round(time/60))} minut.")
