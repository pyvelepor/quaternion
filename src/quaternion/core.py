import re

from math import sqrt
from numbers import Number

class IQuaternion(object):
    def __init__(self, *args, **kargs):
        raise NotImplementedError()

    def __mul__(self, other):
        raise NotImplementedError()

    def __add__(self, other):
        raise NotImplementedError()

    def __sub__(self, other):
        raise NotImplementedError()

    def __neg__(self):
        raise NotImplementedError()

    @property
    def a(self):
        raise NotImplementedError()

    @property
    def b(self):
        raise NotImplementedError()

    @property
    def c(self):
        raise NotImplementedError()

    @property
    def d(self):
        raise NotImplementedError()

    @property
    def magnitude(self):
        raise NotImplementedError()

    @property
    def conjugate(self):
        raise NotImplementedError()

    @property
    def inverse(self):
        raise NotImplementedError()

    @property
    def real(self):
        raise NotImplementedError()

    @property
    def imag(self):
        raise NotImplementedError()

class BaseQuaternion(IQuaternion):
    def __init__(self, *args, **kargs):
        if self._are_numbers(args):
            self._init_from_components(*args)

        elif self._implements_iquaternion(args):
            self._init_from_iquaternion(*args)

        else:
            raise TypeError(
                "Arguments for BaseQuaternion.__init__ must be of type " \
                "'IQuaternion' or 'number, number, number, number'"
            )

    def _are_numbers(self, args):
        return all([isinstance(x, Number) for x in args])

    def _implements_iquaternion(self, args):
        if len(args) != 1:
            return False

        return isinstance(args[0], IQuaternion)

    def _init_from_components(self, a, b, c, d):
        self._a = float(a)
        self._b = float(b)
        self._c = float(c)
        self._d = float(d)

    def _init_from_iquaternion(self, iquaternion):
        self._init_from_components(
            iquaternion.a,
            iquaternion.b,
            iquaternion.c,
            iquaternion.d
        )

    def __repr__(self):
        class_name = self.__class__.__name__

        string = '{name}<a={a}, b={b}, c={c}, d={d}>'
        string = string.format(
            name=class_name,
            a=self.a,
            b=self.b,
            c=self.c,
            d=self.d
        )

        return string

    def __str__(self):
        MINUS = '-'
        PLUS  = '+'
        I     = 'i'
        J     = 'j'
        K     = 'k'

        exp = ''
        operators = {MINUS, PLUS}
        imag = {I, J, K}

        a = self.a
        b = self.b
        c = self.c
        d = self.d

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
            token = exp.pop()

            if exp:
                expression = token + ' ' + expression

            elif token == MINUS:
                expression = token + expression

        return expression.strip()

    def __neg__(self):
        return self * -1.0

    def _add(self, other):
        q = self
        p = other

        a = q.a + p.a
        b = q.b + p.b
        c = q.c + p.c
        d = q.d + p.d

        return a, b, c ,d

    def __add__(self, other):
        return self.__class__(*self._add(other))

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if isinstance(other, int):
            return self.__class__(*self._mul_by_scalar(other))

        if isinstance(other, float):
            return self.__class__(*self._mul_by_scalar(other))

        raise TypeError()

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        return self.__mul__(1.0 / other)

    def __iadd__(self, other):
        self._set_components(*self._add(other))

        return self

    def __isub__(self, other):
        return self.__iadd__(-other)

    def __imul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self._set_components(*self._mul_by_scalar(other))
            return self

        raise TypeError()

    def __idiv__(self, other):
        return self.__imul__(1.0 / other)

    def _set_components(self, a, b, c, d):
        self._a = a
        self._b = b
        self._c = c
        self._d = d

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

        return a, b, c, d

    def _mul_by_scalar(self, scalar):

        a = self.a * scalar
        b = self.b * scalar
        c = self.c * scalar
        d = self.d * scalar

        return a, b, c, d

    @classmethod
    def from_quaternion(cls, q):
        return cls(q.a, q.b, q.c, q.d)

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def c(self):
        return self._c

    @property
    def d(self):
        return self._d

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
    def __init__(self, *args, **kargs):
        super(Quaternion, self).__init__(*args, **kargs)

    def __mul__(self, other):
        if isinstance(other, IQuaternion):
            return self.__class__(*self._mul_by_quaternion(other))

        return super(Quaternion, self).__mul__(other)

    def __div__(self, other):
        if isinstance(other, IQuaternion):
            return self.__mul__(other.inverse)

        return super(Quaternion, self).__div__(other)

    def __imul__(self, other):
        if isinstance(other, IQuaternion):
            self._set_components(*self._mul_by_quaternion(other))
            return self

        return super(Quaternion, self).__imul__(other)

    def __idiv__(self, other):
        return self.__imul__(other.inverse)

    @property
    def inverse(self):
        return self.conjugate / self.magnitude ** 2

class UnitQuaternion(BaseQuaternion):
    def __init__(self, *args, **kargs):
        super(UnitQuaternion, self).__init__(*args, **kargs)
        self /= self.magnitude

    def __mul__(self, other):
        if isinstance(other, IQuaternion):
            if isinstance(other, Quaternion):
                other = self.from_quaternion(other)

            return self.__class__(*self._mul_by_quaternion(other))

        return super(UnitQuaternion, self).__mul__(other)

    def __div__(self, other):
        if isinstance(other, IQuaternion):
            return self.__mul__(other.inverse)

        return super(UnitQuaternion, self).__div__(other)

    def __imul__(self, other):

        if isinstance(other, IQuaternion):
            if isinstance(other, Quaternion):

                other = self.from_quaternion(other)

            self._set_components(*self._mul_by_quaternion(other))

            return self

        return super(UnitQuaternion, self).__imul__(other)

    def __idiv__(self, other):
        if isinstance(other, IQuaternion):
            return self.__imul__(other.inverse)

        return super(UnitQuaternion, self).__idiv__(other)

    def _set_components(self, a, b, c, d):
        super(UnitQuaternion, self)._set_components(a, b, c, d)
        magnitude = self.magnitude
        a /= magnitude
        b /= magnitude
        c /= magnitude
        d /= magnitude
        super(UnitQuaternion, self)._set_components(a, b, c, d)

    @property
    def inverse(self):
        return self.conjugate
