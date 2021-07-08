
def getBit(number, hex) :
    if number & hex :
        return 1

    return 0

def getAllSegments(_input) :
    # decimal, A(MSB), B(second bit), C(third bit), D(LSB) => a
    #  0, 0, 0, 0, 0 => 1
    #  1, 0, 0, 0, 1 => 0
    #  2, 0, 0, 1, 0 => 1
    #  3, 0, 0, 1, 1 => 1
    #  4, 0, 1, 0, 0 => 0
    #  논리식(K-map 추론) : a = A`B`C + A`B`D`

    a = ((not getBit(_input, 0x8)) * (not getBit(_input, 0x4)) * getBit(_input, 0x2)) | ((not getBit(_input, 0x8)) * (not getBit(_input, 0x4)) * (not getBit(_input, 0x1)))

    # decimal, A(MSB), B(second bit), C(third bit), D(LSB) => f
    #  0, 0, 0, 0, 0 => 1
    #  1, 0, 0, 0, 1 => 0
    #  2, 0, 0, 1, 0 => 0
    #  3, 0, 0, 1, 1 => 0
    #  4, 0, 1, 0, 0 => 1
    #  논리식(K-map 추론) : f = A`C`D`

    f = (not getBit(_input, 0x8)) * (not getBit(_input, 0x2)) * (not getBit(_input, 0x1))

    # decimal, A(MSB), B(second bit), C(third bit), D(LSB) => b
    #  0, 0, 0, 0, 0 => 1
    #  1, 0, 0, 0, 1 => 1
    #  2, 0, 0, 1, 0 => 1
    #  3, 0, 0, 1, 1 => 1
    #  4, 0, 1, 0, 0 => 1
    #  논리식(K-map 추론) : b = A`B` + A`C`D`

    b = ((not getBit(_input, 0x8)) * (not getBit(_input, 0x4))) | ((not getBit(_input, 0x8)) * (not getBit(_input, 0x2)) * (not getBit(_input, 0x1)))

    # decimal, A(MSB), B(second bit), C(third bit), D(LSB) => g
    #  0, 0, 0, 0, 0 => 0
    #  1, 0, 0, 0, 1 => 0
    #  2, 0, 0, 1, 0 => 1
    #  3, 0, 0, 1, 1 => 1
    #  4, 0, 1, 0, 0 => 1
    #  논리식(K-map 추론) : g = B + A`B`C

    g = getBit(_input, 0x4) | ((not getBit(_input, 0x8)) * (not getBit(_input, 0x4)) * getBit(_input, 0x2))

    # decimal, A(MSB), B(second bit), C(third bit), D(LSB) => e
    #  0, 0, 0, 0, 0 => 1
    #  1, 0, 0, 0, 1 => 0
    #  2, 0, 0, 1, 0 => 1
    #  3, 0, 0, 1, 1 => 0
    #  4, 0, 1, 0, 0 => 0
    #  논리식(K-map 추론) : e = A'B'D'

    e = (not getBit(_input, 0x8)) * (not getBit(_input, 0x4)) * (not getBit(_input, 0x1))

    # decimal, A(MSB), B(second bit), C(third bit), D(LSB) => c
    #  0, 0, 0, 0, 0 => 1
    #  1, 0, 0, 0, 1 => 1
    #  2, 0, 0, 1, 0 => 0
    #  3, 0, 0, 1, 1 => 1
    #  4, 0, 1, 0, 0 => 1
    #  논리식(K-map 추론) : c = A`C`D` + A`B`D

    c = ((not getBit(_input, 0x8)) * (not getBit(_input, 0x2)) * (not getBit(_input, 0x1))) | ((not getBit(_input, 0x8)) * (not getBit(_input, 0x4)) * getBit(_input, 0x1))

    # decimal, A(MSB), B(second bit), C(third bit), D(LSB) => d
    #  0, 0, 0, 0, 0 => 1
    #  1, 0, 0, 0, 1 => 0
    #  2, 0, 0, 1, 0 => 1
    #  3, 0, 0, 1, 1 => 1
    #  4, 0, 1, 0, 0 => 0
    #  논리식(K-map 추론) : c = A`B`D` + A`B`C

    d = ((not getBit(_input, 0x8)) * (not getBit(_input, 0x4)) * (not getBit(_input, 0x1))) | ((not getBit(_input, 0x8)) * (not getBit(_input, 0x4)) * getBit(_input, 0x2))

    return int(a), int(f), int(b), int(g), int(e), int(c), int(d)