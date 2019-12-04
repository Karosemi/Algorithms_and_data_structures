class Hanoi:

    def __init__(self, n: int, names=None):
        self.A = Stack()
        [self.A.push('disk') for i in range(n)]
        self.B = Stack()
        self.C = Stack()
        if type(names) == list and len(names) == 3:
            self.towers = {self.A: names[0], self.B: names[1],  self.C: names[2]}
        elif names is None:
            self.towers = {self.A: 'A',self.B: 'B', self.C: 'C'}
        else:
            print("Names have to be 3 element list. Applied names are: A, B and C.")
            self.towers = {self.A: 'A', self.B: 'B', self.C: 'C'}
        self.move_tower(n, self.A, self.B, self.C)

    def move_tower(self, n: int, from_: object, with_: object, to_:object):
        if n >= 1:
            self.move_tower(n-1, from_, to_, with_)
            self.move_disk(from_, with_)
            self.move_tower(n-1, to_, with_, from_)

    def move_disk(self, from_: object, to_: object):
        from_.pop()
        to_.push('disk')
        print(f"moving disk from {self.towers[from_]} to {self.towers[to_]}")

class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    hanoi = Hanoi(4, names=['A', 'B', 'C'])