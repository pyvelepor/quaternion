from basequaternion import BaseQuaternion
from quaternion import Quaternion

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

        super(UnitQuaternion, self).__mul__(other)

    @property
    def inverse(self):
        return self.conjugate
