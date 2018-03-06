from unittest import TestCase

import pyrot


class TestQuaternions(TestCase):
    def test_init(self):
        s = pyrot.Quaternion(1, 2, 3, 4)
        self.assertIsInstance(s, pyrot.Quaternion)

    def test_addition_stays_quaternion(self):
        a = pyrot.Quaternion(0, 0, 0, 0)
        b = pyrot.Quaternion(1, 2, 3, 4)

        c = a + b
        self.assertIsInstance(c, pyrot.Quaternion)

    def test_add(self):
        a = pyrot.Quaternion(-6, 2, 1, 2)
        b = pyrot.Quaternion(1, 2, 3, 4)

        c = a + b
        self.assertEqual(c, pyrot.Quaternion(-5, 4, 4, 6))

    def test_sub(self):
        a = pyrot.Quaternion(-6, 2, 1, 2)
        b = pyrot.Quaternion(1, 2, 3, 4)

        c = a - b
        self.assertEqual(c, pyrot.Quaternion(-7, 0, -2, -2))

    def test_left_scalar_sub(self):
        a = pyrot.Quaternion(1, 2, 3, 4)
        b = 3

        c = a - b
        self.assertEqual(c, pyrot.Quaternion(-2, 2, 3, 4))

    def test_right_scalar_sub(self):
        a = 3
        b = pyrot.Quaternion(1, 2, 3, 4)

        c = a - b
        self.assertEqual(c, pyrot.Quaternion(2, -2, -3, -4))

    def test_left_scalar_multiplication(self):
        a = pyrot.Quaternion(1, -2, 3, 4)
        b = 6

        c = a * b
        self.assertEqual(c, pyrot.Quaternion(6, -12, 18, 24))

    def test_left_float_scalar_multiplication(self):
        a = pyrot.Quaternion(1, -2, 3, 4)
        b = 6.0

        c = a * b
        self.assertEqual(c, pyrot.Quaternion(6, -12, 18, 24))

    def test_right_scalar_multiplication(self):
        a = pyrot.Quaternion(1, -2, 3, 4)
        b = 6

        c = b * a
        self.assertEqual(c, pyrot.Quaternion(6, -12, 18, 24))

    def test_left_scalar_division(self):
        a = pyrot.Quaternion(1, -2, 3, 4)
        b = 2

        c = a / b
        self.assertTrue((c - pyrot.Quaternion(1./2,
                                              -2./2,
                                              3./2,
                                              4./2)).norm() < 1e-7)

    def test_conjugation(self):
        a = pyrot.Quaternion(1, -2, 3, 4)

        b = a.conjugate()
        self.assertEqual(b, pyrot.Quaternion(1, 2, -3, -4))

    def test_norm(self):
        a = pyrot.Quaternion(1, -2, 3, 4)

        b = a.norm()
        self.assertAlmostEqual(b, 5.47722557505)

    def test_inverse(self):
        a = pyrot.Quaternion(1, -2, 3, 4)
        b = a.inverse()

        c = a * b

        norm  = (1 - c).norm()
        self.assertAlmostEqual(norm, 0)
