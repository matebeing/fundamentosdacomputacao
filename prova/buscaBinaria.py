array = []
menu = """

1- Inserir número
2- Buscar número
## 1 - Busca Sequencial
## 2 - Busca Binária
3- Exibir lista
4- Sair
      
"""


def is_list_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


def searchNonOrd(array, target):
    for _ in range(len(array)):
        if array[_] == target:
            return _
    return -1


def searchOrd(array, target):
    for _ in range(len(array)):
        if array[_] == target:
            return _
        elif array[_] > target:
            return -1
    return -1


def binarySearch(array, target):
    low = 0
    high = len(array) - 1

    while (low <= high):
        mid = int((low + high) / 2)
        if array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1


while True:
    print(menu)

    option = int(input("O que deseja realizar? [1-4] "))

    match option:
        case 1:
            array += [int(input("Digite um número: "))]
        case 2:
            search = int(input("Qual tipo de busca deseja realizar? [1-2]"))
            match search:
                case 1:
                    target = int(input("Qual número deseja procurar? "))
                    if is_list_sorted:
                        print("Resultado da busca: ", searchOrd(array, target))
                    else:
                        print("Resultado da busca: ",
                              searchNonOrd(array, target))
                case 2:
                    target = int(input("Qual número deseja procurar? "))
                    if is_list_sorted:
                        print("Resultado da busca: ",
                              binarySearch(array, target))
                    else:
                        print(
                            "Não foi possível realizar a busca, pois o vetor não está em ordem.")
        case 3:
            print(array)
        case 4:
            break
