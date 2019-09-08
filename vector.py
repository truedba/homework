#!/usr/local/bin/python3
import operator
import numpy as np


class Vector:

    def __init__(self, *args):
        self.vector = []
        for i in args:
            self.vector.append(i)

    def check_vectors(self, obj):
        if len(self.vector) == len(obj.vector):
            pass
        else:
            raise TypeError("Unsupported operands error - Vectors must be the same dimension")

    def __add__(self, obj):
        self.check_vectors(obj)
        self.vector = list(map(operator.add, self.vector, obj.vector))
        print(self.vector)

    def __mul__(self, obj):
        if isinstance(obj, int) or isinstance(obj, float):
            self.vector = [i * obj for i in self.vector]
            print(self.vector)
        elif isinstance(obj, object):
            self.check_vectors(obj)
            mult_vector = np.cross(self.vector, obj.vector)
            print(mult_vector)

    def __matmul__(self,obj):
        self.check_vectors(obj)
        self.vector = list(map(operator.mul, self.vector, obj.vector))
        print(sum(self.vector))


if __name__ == '__main__':

    v1 = Vector(5, 1)
    v1 + Vector(1, 3)
    Vector(2, 3, -1) @ Vector(5, 1, 5)
    Vector(2, 3, -1) * Vector(5, 1, 5)
    v1 * 2
