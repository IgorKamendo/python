def binary_search(array, element):
    mid = 0
    start = 0
    end = len(array)
    step = 0

    while (start <= end):
        print("Subarray in step {}: {}".format(step, str(array[start:end + 1])))
        step = step + 1
        mid = (start + end) // 2

        if element == array[mid]:
            return mid
        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return - 1


array = list(input("Введите последовательность случайных целых чисел через пробел по мере их возрастания: ").split())
element = input("Введите число из введенной последовательности, которое нужно найти: ")

print("Searching for {} in {}".format(element, array))
print("Index of {}: {}".format(element, binary_search(array, element)))
