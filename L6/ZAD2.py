from numpy.random import randint
from numpy import array, log, polyfit
from time import time
import matplotlib.pyplot as plt

class BinHeap:

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
        i = i // 2

    def insert(self,k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)

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

    def build_heap(self, alist):
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


def sort_list(unsorted_list: list):
    bh = BinHeap()
    sorted_list =[]
    bh.build_heap(unsorted_list)
    for i in range(len(unsorted_list)):
        min = bh.find_min()
        sorted_list.append(min)
        bh.del_min()
    return sorted_list


# def heap_sort(arr, )
if __name__ == '__main__':
    hp = BinHeap()
    # hp.insert(4)
    unsorted_list = [5,4,89,43,54,6,123,24,64,34,87]
    # hp.build_heap(unsorted_list)
    print(sort_list(unsorted_list))


    N = 10000
    n = 10
    N_list = list(range(n,N+1,n))
    times = []
    for k in range(n,N+1,n):
        temp_list = list(randint(1, 1000, k))
        beg = time()
        sort_temp_list = sort_list(temp_list)
        end = time()
        times.append(end-beg)
    times = array(times)
    N_list = array(N_list)
    coeff = polyfit(log(N_list),times, 1)
    print(coeff)
    plt.plot(N_list, times, label = 'times')
    plt.plot(N_list, coeff[0]*log(N_list)+coeff[1]/2)
    # plt.plot(array(N_list), array(N_list)*log(array(N_list)), label = 'funnc')
    plt.legend()
    plt.savefig('com_3.png')
    plt.show()