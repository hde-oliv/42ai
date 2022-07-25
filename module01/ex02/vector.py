
class Vector:
    def __init__(self, vector):
        self.values = self._set_vector(vector)
        self.shape = self._set_shape()

    def _set_vector(self, vector):
        pass

    def _set_shape(self):
        if len(self.values) == 1:
            self.shape = "row"
        else:
            self.shape = "column"

    def T(self):
        if self.shape == "row":
            return Vector([[n] for n in self.values[0]])
        else:
            return Vector([l[0] for l in self.values])

    def dot(self, vector):
        if self.shape == vector.shape:
           pass 

