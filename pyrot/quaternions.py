# -*- coding: utf-8 -*-
import numpy as np


class Quaternion(object):
    def __init__(self, a, b=0, c=0, d=0):
        if isinstance(a, np.ndarray):
            self.data = a
        else:
            self.data = np.float64([a, b, c, d])

    def __add__(self, other):
        sum_data = self.data + other.data
        return Quaternion(sum_data)

    def __sub__(self, other):
        if isinstance(other, (float, int)):
            other = Quaternion(other, 0, 0, 0)
        sub_data = self.data - other.data
        return Quaternion(sub_data)

    def __rsub__(self, other):
        if isinstance(other, (float, int)):
            other = Quaternion(other, 0, 0, 0)
        sub_data = other.data - self.data
        return Quaternion(sub_data)

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return Quaternion(self.data[0]*other,
                              self.data[1]*other,
                              self.data[2]*other,
                              self.data[3]*other)

        a = self.data[0]*other.data[0] - self.data[1]*other.data[1] \
            - self.data[2]*other.data[2] - self.data[3]*other.data[3]

        b = self.data[0]*other.data[1] + self.data[1]*other.data[0] \
            + self.data[2]*other.data[3] - self.data[3]*other.data[2]

        c = self.data[0]*other.data[2] - self.data[1]*other.data[3] \
            + self.data[2]*other.data[0] + self.data[3]*other.data[1]

        d = self.data[0]*other.data[3] + self.data[1]*other.data[2] \
            - self.data[2]*other.data[1] + self.data[3]*other.data[0]

        return Quaternion(a, b, c, d)

    def __rmul__(self, other):
        if isinstance(other, (float, int)):
            return self.__mul__(other)

    def __div__(self, other):
        if isinstance(other, (float, int)):
            return Quaternion(self.data / other)

    def conjugate(self):
        return Quaternion(self.data[0],
                          -self.data[1],
                          -self.data[2],
                          -self.data[3])

    def norm(self):
        return np.sqrt(np.sum(self.data * self.data))

    def inverse(self):
        a = self.conjugate()
        b = np.sum(self.data * self.data)
        inv = a / b
        return inv

    def __eq__(self, other):
        return np.all(self.data == other.data)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        result = ''
        result += '{:.2f}'.format(self.data[0])
        if self.data[1] < 0:
            result += ' - '
        else:
            result += ' + '
        result += '{:.2f}i'.format(abs(self.data[1]))

        if self.data[2] < 0:
            result += ' - '
        else:
            result += ' + '
        result += '{:.2f}j'.format(abs(self.data[2]))

        if self.data[3] < 0:
            result += ' - '
        else:
            result += ' + '
        result += '{:.2f}k'.format(abs(self.data[3]))
        return result

    def __repr__(self):
        return 'Quaternion({}, {}, {}, {})'.format(self.data[0],
                                                   self.data[1],
                                                   self.data[2],
                                                   self.data[3])
