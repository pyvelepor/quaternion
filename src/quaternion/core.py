import re
from math import sqrt


def to_str(a, b, c, d):
    MINUS = '-'
    PLUS  = '+'
    I     = 'i'
    J     = 'j'
    K     = 'k'

    exp = ''
    operators = {MINUS, PLUS}
    imag = {I, J, K}

    exp =  '{sign} {a}'.format(a=abs(a), sign='+' if a >=0 else '-')
    exp += ' {sign} {b} * i'.format(b=abs(b), sign='+' if b >=0 else '-')
    exp += ' {sign} {c} * j'.format(c=abs(c), sign='+' if c >=0 else '-')
    exp += ' {sign} {d} * k'.format(d=abs(d), sign='+' if d >=0 else '-')

    tokens = re.split(' ', exp)
    exp = []

    index = 0

    while index < len(tokens):

        token = tokens[index]

        if token in operators:
            exp.append(token)

            if token == PLUS:
                if not float(tokens[index + 1]):
                    exp.pop()
                    try:
                        while tokens[index + 1] not in operators:
                            index = index + 1
                    except IndexError:
                        index = index + 1

        elif token in imag:
            exp.append(exp.pop() + token)

        try:
            float(token)
        except Exception:
            pass
        else:
            exp.append(token)

        index = index + 1

    expression = ''

    if not exp:
        return str(0.0)

    while exp:
        op1 = exp.pop()
        op = exp.pop()

        expression = op1 + ' ' + expression

        if exp:
            expression = op + ' ' + expression

        elif op == MINUS:
            expression = op + expression

    return expression.strip()

class IQuaternion(object):
    def __init__(self, a, b, c, d):
        raise NotImplemented()

    def __mul__(self, other):
        raise NotImplemented()

    def __add__(self, other):
        raise NotImplemented()

    def __sub__(self, other):
        raise NotImplemented()

    def __neg__(self):
        raise NotImplemented()

    @property
    def a(self):
        raise NotImplemented()

    @a.setter
    def a(self, value):
        raise NotImplemented()

    @property
    def b(self):
        raise NotImplemented()

    @b.setter
    def b(self, value):
        raise NotImplemented()

    @property
    def c(self):
        raise NotImplemented()

    @c.setter
    def c(self, value):
        raise NotImplemented()

    @property
    def d(self):
        raise NotImplemented()

    @d.setter
    def d(self, value):
        raise NotImplemented()

    @property
    def magnitude(self):
        raise NotImplemented()

    @property
    def conjugate(self):
        raise NotImplemented()

    @property
    def inverse(self):
        raise NotImplemented()

    @property
    def real(self):
        raise NotImplemented()

    @property
    def imag(self):
        raise NotImplemented()

class BaseQuaternion(IQuaternion):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self):
        return to_str(self.a, self.b, self.c, self.d)

    def __neg__(self):
        return self * -1.0

    def __add__(self, other):
        q = self
        p = other

        a = q.a + p.a
        b = q.b + p.b
        c = q.c + p.c
        d = q.d + p.d

        return self.__class__(a, b, c, d)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if isinstance(other, int):
            return self._mul_by_scalar(other)

        if isinstance(other, float):
            return self._mul_by_scalar(other)

        raise TypeError()

    def __rmul__(self, other):
        return self.__mul__(other)

    def _mul_by_quaternion(self, quaternion):
        a1 = self.a
        b1 = self.b
        c1 = self.c
        d1 = self.d

        a2 = quaternion.a
        b2 = quaternion.b
        c2 = quaternion.c
        d2 = quaternion.d

        a = (a1 * a2) - (b1 * b2) - (c1 * c2) - (d1 * d2)
        b = (a1 * b2) + (b1 * a2) + (c1 * d2) - (d1 * c2)
        c = (a1 * c2) - (b1 * d2) + (c1 * a2) + (d1 * b2)
        d = (a1 * d2) + (b1 * c2) - (c1 * b2) + (d1 * a2)

        return self.__class__(a, b, c, d)

    def _mul_by_scalar(self, scalar):

        a = self.a * scalar
        b = self.b * scalar
        c = self.c * scalar
        d = self.d * scalar

        return self.__class__(a, b, c, d)

    @classmethod
    def from_quaternion(cls, q):
        return cls(q.a, q.b, q.c, q.d)

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = float(value)

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = float(value)

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        self._c = float(value)

    @property
    def d(self):
        return self._d

    @d.setter
    def d(self, value):
        self._d = float(value)

    @property
    def real(self):
        return self.a

    @property
    def imag(self):
        return self.b*1j, self.c*1j, self.d*1j

    @property
    def conjugate(self):
        a = self.a
        b = -self.b
        c = -self.c
        d = -self.d

        return self.__class__(a, b, c, d)

    @property
    def magnitude(self):
        return sqrt(self.a ** 2 + self.b ** 2 + self.c ** 2 + self.d ** 2)

class Quaternion(BaseQuaternion):
    def __init__(self, a, b, c, d):
        super(Quaternion, self).__init__(a, b, c, d)

    def __mul__(self, other):
        if isinstance(other, IQuaternion):
            return self._mul_by_quaternion(other)

        return super(Quaternion, self).__mul__(other)

    @property
    def inverse(self):
        return self.conjugate * (1 / (self.magnitude * self.magnitude))

class UnitQuaternion(BaseQuaternion):
    def __init__(self, a, b, c, d):
        super(UnitQuaternion, self).__init__(a, b, c, d)
        self.a /= self.magnitude
        self.b /= self.magnitude
        self.c /= self.magnitude
        self.d /= self.magnitude

    def __mul__(self, other):
        if isinstance(other, UnitQuaternion):
            return self._mul_by_quaternion(other)

        if isinstance(other, Quaternion):
            other = self.from_quaternion(other)
            return self._mul_by_quaternion(other)

        return super(UnitQuaternion, self).__mul__(other)

    @property
    def inverse(self):
        return self.conjugate
