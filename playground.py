# a = 5
# print(a, "is of type", type(a))

# a = 2.0
# print(a, "is of type", type(a))

# a = 1+2j
# print(a, "is complex number?", isinstance(1+2j,complex))


# l = [10,20,30,40,50];
# for item in l:
#     print(item)

# for item in range(len(l)):
#     print(item)


# def appendItem(itemName, itemList = []):
#     itemList.append(itemName)
#     return itemList


# print(appendItem('notebook'))
# print(appendItem('pencil'))
# print(appendItem('eraser'))

# def factorial(x):
#     """This is a recursive function
#     to find the factorial of an integer"""

#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))


# num = 100
# print("The factorial of", num, "is", factorial(num))


from typing import Dict, TypeVar
x = "global "

# def foo():
#     global x
#     y = "local"
#     x = x * 2
#     print(x)
#     print(y)

# def foo():
#     global x
#     y = x
#     y = x * 2
#     print(x)
#     print(y)

# print(x)
# foo()
# print(x)

# print([0 for i in range(10)])

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


def get_first(container: Dict[K, T ]) -> T:
    # mypy raises: Incompatible return value type (got "V", expected "K")
    return list(container.values())[0]


if __name__ == "__main__":
    test: Dict[str, int] = {"k": 1}
    print(get_first(test))
    test1: Dict[str, int] = {"a": 1}
    get_first[int](test1)
