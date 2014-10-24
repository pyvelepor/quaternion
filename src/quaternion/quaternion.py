from api import IQuaternion, BaseQuaternion

class Quaternion(BaseQuaternion):
    def __init__(self, a, b, c, d):
        super(Quaternion, self).__unit__(a, b, c, d)

    def __mul__(self, other):
        if isinstance(other, IQuaternion):
            return self._mul_by_quaternion(other)

        return super(Quaternion, self).__init__(other)

    @property
    def inverse(self):
        self.conjugate / self.magnitude
