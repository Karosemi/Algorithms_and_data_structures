from ZAD2 import BinHeap, sort_list


class LimitedBinHeap:

    def __init__(self, n):
        self.heap_list = [0]
        self.current_size = 0
        self.n = n

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
        i = i // 2

    def insert(self,k):
        if self.size() < self.n:
            self.__insert(k)
        else:
            if self.find_min() < k:
                self.del_min()
                self.insert(k)
            else:
                print('Maximum size of BinHeap is gained, and value is lower than other: pass')

    def __insert(self,k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)
        self.n -= 1

    def find_min(self):
        return self.heap_list[1]

    def perc_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def del_min(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.perc_down(1)
        return retval

    def build_lim_heap(self, alist):
        over = len(alist) - self.n
        print('over', over)
        if over > 0:
            while len(alist) != self.n:
                max_a = max(alist)
                if not self.is_empty() and self.find_min() < max_a:
                    self.del_min()
                    # self.insert(max_a)
                    # alist.remove(max_a)
                elif self.is_empty():
                    while self.n != len(alist):
                        alist.remove(min(alist))
                else:
                    alist.remove(max_a)

        else:
            self.__build_lim_heap(alist)

    def __build_lim_heap(self, alist):
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [0] + alist[:]
        while (i > 0):
            self.perc_down(i)
            i = i - 1

    def size(self):
        return self.current_size

    def is_empty(self):
        return self.current_size == 0

    def __str__(self):
        txt = "{}".format(self.heap_list[1:])
        return txt


if __name__ == '__main__':
    ldst = LimitedBinHeap(6)
    ldst.build_lim_heap([3, 67, 2, 4, 1, 96])
    ldst.insert(9)
    print(ldst.size())