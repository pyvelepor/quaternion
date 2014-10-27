import unittest
import quaternion.api as qapi

class ArithmeticTestCase(unittest.TestCase):
    def test_add(self):
        q = qapi.Quaternion(1, 1, 1, 1)
        p = qapi.Quaternion(1, 1, 1, 1)

        r = qapi.add(q, p)

        self.assertEqual(r.a, 2)
        self.assertEqual(r.b, 2)
        self.assertEqual(r.c, 2)
        self.assertEqual(r.d, 2)

    def test_sub(self):
        q = qapi.Quaternion(1, 1, 1, 1)
        p = qapi.Quaternion(1, 1, 1, 1)

        r = qapi.sub(q, p)

        self.assertEqual(r.a, 0)
        self.assertEqual(r.b, 0)
        self.assertEqual(r.c, 0)
        self.assertEqual(r.d, 0)

    def test_mul(self):
        q = qapi.Quaternion(1, 1, 1, 1)
        p = qapi.Quaternion(0.25, -0.25, -0.25, -0.25)

        r = qapi.mul(q, p)

        self.assertEqual(r.a, 1)
        self.assertEqual(r.b, 0)
        self.assertEqual(r.c, 0)
        self.assertEqual(r.d, 0)

    def test_div(self):
        q = qapi.Quaternion(1, 1, 1, 1)
        p = qapi.div(1, 1, 1, 1)

        r = qapi.div(q, p)

        self.assertEqual(r.a, 1)
        self.assertEqual(r.b, 0)
        self.assertEqual(r.c, 0)
        self.assertEqual(r.d, 0)

class ChecksTestCase(unittest.TestCase):
    pass

class UtilTestCase(unittest.TestCase):
    pass
