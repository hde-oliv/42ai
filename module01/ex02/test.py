from vector import Vector

def main():
    first = Vector(5)
    second = Vector(5)
    third = Vector((0, 10))
    # fourth = Vector((60, 50))
    # fifth = Vector("String")
    sixth = Vector([[1.0], [2.0], [3.0], [4.0]])
    seventh = Vector([[1.0, 2.0, 3.0, 4.0]])

    print(first.T())
    print(second.T())
    print(third)
    print(sixth.T())
    print(seventh.T())
    # print(fourth)

    print("\n\n")

    print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape)
    print(Vector([[0.0], [1.0], [2.0], [3.0]]).values)
    print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape)
    print(Vector([[0.0, 1.0, 2.0, 3.0]]).values)
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    print(v1.shape)
    print(v1.T())
    print(v1.T().shape)
    v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
    print(v2.shape)
    print(v2.T())
    print(v2.T().shape)
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
    print(v1.dot(v2))
    v3 = Vector([[1.0, 3.0]])
    v4 = Vector([[2.0, 4.0]])
    print(v3.dot(v4))
    print(repr(v1))

    print(first * 5)
    print(9 * first)

    print(first / 7)
    # print(7 / first)

    print(first - second)
    print(second - first)
    print(first + second)
    print(second + first)

if __name__ == '__main__':
    main()
