vetor = [14, 5, 21, 7, 9, 2, 1, 3, 11, 16, 17, 18, 19, 20]


def buscaSeq(array, valor):
    for i in range(len(vetor)):
        if array[i] == valor:
            return i
    return -1


def buscaSeqNaoOrd(array, num):
    for _ in range(len(array)):
        if array[_] == num:
            return _
    return -1


print(buscaSeqNaoOrd(vetor, 16))
