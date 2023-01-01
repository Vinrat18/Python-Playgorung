def binary_search(elements: list[int], value: int):
    first = 0
    last = len(elements) - 1

    while first <= last:
        mid = (first + last) // 2

        if elements[mid] == value:
            return mid
        
        elif elements[mid] < value:
            first = mid + 1
        else:
            last = mid - 1

    return -1

if __name__ == '__main__':
   a_list = [1, 4, 7, 10, 14, 19, 102, 2575, 10000]

   print('Binary Search:', binary_search(a_list, 25))