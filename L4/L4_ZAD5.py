class Node:
  
    def __init__(self,init_data):
        self.data = init_data
        self.next = None
  
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next
  
    def set_data(self,new_data):
        self.data = new_data
  
    def set_next(self,new_next):
        self.next = new_next
    

class UnorderedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count
    
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None: #jeśli usuwamy pierwszy element
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
      
    def append(self, item):
        """
        Metoda dodająca element na koniec listy.
        Przyjmuje jako argument obiekt, który ma zostać dodany.
        Niczego nie zwraca.
        """
        current = self.head
        if current is None:
            self.head = Node(item)
        else:
            while current.get_next() is not None:
                current = current.get_next()
            temp = Node(item)
            current.set_next(temp)

    def index(self, item):
        """
        Metoda podaje miejsce na liście,
        na którym znajduje się określony element -
        element pod self.head ma indeks 0.
        Przyjmuje jako argument element,
        którego pozycja ma zostać określona.
        Zwraca pozycję elementu na liście lub None w przypadku,
        gdy wskazanego elementu na liście nie ma.
        """
        i = 0
        current = self.head
        try:
            while current.get_data() is not None:
                if current.get_data() == item:
                    return i
                else:
                    current = current.get_next()
                i += 1
        except AttributeError:
            print('Element is not in list.')
            return None

    def insert(self, pos, item):
        """
        Metoda umieszcza na wskazanej pozycji zadany element.
        Przyjmuje jako argumenty pozycję,
        na której ma umiescić element oraz ten element.
        Niczego nie zwraca.
        Rzuca wyjątkiem IndexError w przypadku,
        gdy nie jest możliwe umieszczenie elementu
        na zadanej pozycji (np. na 5. miejsce w 3-elementowej liście).
        """
        if pos == 0:
            self.add(item)
            return
        i = 0
        current = self.head
        try:
            while current.get_data() is not None:
                if i == pos-1:
                    next = current.get_next()
                    temp = Node(item)
                    temp.set_next(next)
                    current.set_next(temp)
                    break
                else:
                    current = current.get_next()
                    i += 1
            if current.get_next() is None:
                temp = Node(item)
                current.set_next(temp)
        except AttributeError:
        # if current.get_data() is None:
            raise IndexError('Index is out of range.')

    def pop(self, pos=-1):
        """
        Metoda usuwa z listy element na zadaniej pozycji.
        Przyjmuje jako opcjonalny argument pozycję,
        z której ma zostać usunięty element.
        Jeśli pozycja nie zostanie podana,
        metoda usuwa (odłącza) ostatni element z listy.
        Zwraca wartość usuniętego elementu.
        Rzuca wyjątkiem IndexError w przypadku,
        gdy usunięcie elementu z danej pozycji jest niemożliwe.
        """
        if pos == 0:
            print(self.head.get_data())
            self.remove(self.head.get_data())
            return self.head.get_data()
        i = 0
        current = self.head
        try:
            while current.get_data() is not None:
                if i == pos:
                    print(current.get_data())
                    next = current.get_next()
                    i += 1
                    break
                else:
                    current = current.get_next()
                    i += 1
            if pos == -1:
                print(current.get_data())
                self.remove(current.get_data())
                return current.get_data()
        except AttributeError:
            raise IndexError('Index is out of range.')
        j = 0
        current = self.head
        while current.get_next() is not None:
            if j == pos - 1:
                current.set_next(next)
                break
            else:
                current = current.get_next()
                j += 1

