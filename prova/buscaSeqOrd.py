vetor = [1, 2, 3, 4, 5]


def buscaSeqOrd(array, num):
    for _ in range(len(array)):
        if array[_] == num:
            return _
        elif array[_] > num:
            return -1
    return -1


print(buscaSeqOrd(vetor, 2))
