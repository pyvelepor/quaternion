import unittest
from quaternion.api import Quaternion

class QuaternionTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_components(self):
        q = Quaternion(1, 2, 3, 4)

        self.assertEqual(q.a, 1)
        self.assertEqual(q.b, 2)
        self.assertEqual(q.c, 3)
        self.assertEqual(q.d, 4)

        q.a = 0
        q.b = 0
        q.c = 0
        q.d = 0

        self.assertEqual(q.a, 0)
        self.assertEqual(q.b, 0)
        self.assertEqual(q.c, 0)
        self.assertEqual(q.d, 0)

    def test_real(self):
        q = Quaternion(1, 0, 0, 0)

        self.assertEqual(q.real, 1)

    def test_imag(self):
        q = Quaternion(0, 1, 1, 1)

        self.assertEqual(q.imag, (1j, 1j, 1j))

    def test_str(self):
        q = Quaternion(0, 0, 0, 0)
        self.assertEqual(str(q), '+0.0+0.0i+0.0j+0.0k')

    def test_add(self):
        q = Quaternion(0, 0, 0, 0)
        p = Quaternion(1, 1, 1, 1)

        r = q + p

        self.assertEqual(r.a, 1.0)
        self.assertEqual(r.b, 1.0)
        self.assertEqual(r.c, 1.0)
        self.assertEqual(r.d, 1.0)

    def test_sub(self):
        q = Quaternion(1, 1, 1, 1)
        p = Quaternion(1, 1, 1, 1)

        r = q - p

        self.assertEqual(r.a, 0.0)
        self.assertEqual(r.b, 0.0)
        self.assertEqual(r.c, 0.0)
        self.assertEqual(r.d, 0.0)

    def test_mul_by_quaternion(self):
        q = Quaternion(1, 1, 1, 1)
        p = Quaternion(0.25, -0.25, -0.25, -0.25)

        r = q * p
        t = p * q

        self.assertEqual(r.a, 1)
        self.assertEqual(r.b, 0)
        self.assertEqual(r.c, 0)
        self.assertEqual(r.d, 0)

        self.assertEqual(t.a, 1)
        self.assertEqual(t.b, 0)
        self.assertEqual(t.c, 0)
        self.assertEqual(t.d, 0)

    def test_mul_by_scalar(self):
        q = Quaternion(0.5, 0.5, 0.5, 0.5)

        p = q * 2
        r = 2 * q

        self.assertTrue(p.a, 1)
        self.assertTrue(p.b, 1)
        self.assertTrue(p.c, 1)
        self.assertTrue(p.d, 1)

        self.assertTrue(r.a, 1)
        self.assertTrue(r.b, 1)
        self.assertTrue(r.c, 1)
        self.assertTrue(r.d, 1)

    def test_magnitude(self):
        q = Quaternion(1, 0, 0, 0)
        p = Quaternion(1, 1, 1, 1)
        r = Quaternion(1, -1, -1, -1)

        self.assertEqual(q.magnitude, 1)
        self.assertEqual(p.magnitude, 2)
        self.assertEqual(r.magnitude, 2)

    def test_conjugate(self):
        q = Quaternion(1, 1, 1, 1)
        p = q.conjugate

        self.assertEqual(p.a, 1)
        self.assertEqual(p.b, -1)
        self.assertEqual(p.c, -1)
        self.assertEqual(p.d, -1)

    def test_inverse(self):
        q = Quaternion(1, 1, 1, 1)
        p = q.inverse

        self.assertEqual(p.a, 0.25)
        self.assertEqual(p.b, -0.25)
        self.assertEqual(p.c, -0.25)
        self.assertEqual(p.d, -0.25)


if __name__ == "__main__":
    unittest.main()
