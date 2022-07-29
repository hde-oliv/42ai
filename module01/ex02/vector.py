class Vector:
    def __init__(self, vector):
        self.__set_values(vector)
        self.__set_shape()

        if len(self.values) == 1:
            self.__type = "row" 
        else:
            self.__type = "column"

    def __check_argument_type(self, argument):
        allowed_types = [list, tuple, int]
        for _type in allowed_types:
            if isinstance(argument, _type):
                return _type
        raise TypeError("Wrong argument type.")

    def __set_values(self, argument) -> list:
        _type = self.__check_argument_type(argument)
        if _type == int:
            self.values = [[float(n)] for n in range(0, argument)]
        elif _type == tuple:
            if (argument[1] < argument[0]):
                raise TypeError("Wrong tuple values.")
            self.values = [[float(n)] for n in range(*argument)]
        else:
            self.values = argument

    def __set_shape(self):
        if len(self.values) == 1:
            self.shape = (1, len(self.values[0]))
        else:
            self.shape = (len(self.values), 1)

    def T(self):
        if self.__type == "row":
            return Vector([[n] for n in self.values[0]])
        else:
            return Vector([[l[0] for l in self.values]])

    def dot(self, vector):
        if not self.shape == vector.shape:
            raise ValueError("Wrong vector shape.")
        else:
            if self.__type == "row":
                return sum([i * j for i, j in zip(self.values[0], vector.values[0])])
            else:
                return sum([i[0] * j[0] for i, j in zip(self.values, vector.values)])

    def __add__(self, vector):
        if not self.shape == vector.shape:
            raise ValueError("Wrong vector shape.")
        else:
            if self.__type == "row":
                return Vector([[i + j for i, j in zip(self.values[0], vector.values[0])]])
            else:
                return Vector([[i[0] + j[0]] for i, j in zip(self.values, vector.values)])

    def __radd__(self, vector):
        return self + vector

    def __sub__(self, vector):
        if not self.shape == vector.shape:
            raise ValueError("Wrong vector shape.")
        else:
            if self.__type == "row":
                return Vector([[i - j for i, j in zip(self.values[0], vector.values[0])]])
            else:
                return Vector([[i[0] - j[0]] for i, j in zip(self.values, vector.values)])
    
    def __rsub__(self, vector):
        return self - vector

    def __truediv__(self, scalar: int):
        if self.__type == "row":
            return Vector([[i / scalar] for i in self.values[0]])
        else:
            return Vector([[i[0] / scalar] for i in self.values])
    
    def __rtruediv__(self, scalar: int):
        raise NotImplementedError("Division of a scalar by a Vector is not defined here.")

    def __mul__(self, scalar: int):
        if self.__type == "row":
            return Vector([[i * scalar] for i in self.values[0]])
        else:
            return Vector([[i[0] * scalar] for i in self.values])
    
    def __rmul__(self, scalar: int):
        return self * scalar

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return str(self.values)
