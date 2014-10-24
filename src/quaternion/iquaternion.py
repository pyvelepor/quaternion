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
