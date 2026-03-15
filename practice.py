"""
Задача 2: Дан отсортированный массив целых чисел a, индекс элемента index и целое число k. Необходимо вернуть в любом
порядке k чисел из массива, которые являются ближайшими по значению к элементу a[index].

Input: [2, 3, 5, 7, 11], index=0, k=2 Output: [2, 3]
Input: [2, 3, 5, 7, 11], index=3, k=2 Output: [5, 7]
Input: [2, 3, 5, 7, 11], index=4, k=2 Output: [7, 11]
Input: [4, 12, 15, 15, 24], index=1, k=3 Output: [12, 15, 15]
Input: [2, 3, 5, 7, 11], index=2, k=2 Output: [3, 5] или [5, 7]
"""


def closest(a: list[int], index: int, k: int) -> list[int]:
    """Возвращает k-чисел из массива, ближайшие к значению a[index].

    >>> closest([2, 3, 5, 7, 11], 4, 2)
    [11, 7]

    >>> closest([2, 3, 5, 7, 11], 3, 2)
    [7, 5]

    >>> closest([4, 12, 15, 15, 24], 1, 3)
    [12, 15, 15]

    >>> closest([2, 3, 5, 7, 11], 0, 2)
    [2, 3]
    """

    res = [a[index]]
    l = index - 1
    r = index + 1

    while l >= 0 and r < len(a):
        if len(res) == k:
            return res
        if abs(a[index] - a[l]) <= abs(a[index] - a[r]):
            res.append(a[l])
            l -= 1
        else:
            res.append(a[r])
            r += 1

    if len(res) < k:
        if l < 0:
            res.extend(a[r:r + (k - len(res))])
        elif r >= len(a):
            res.extend(a[l:l - (k - len(res)):-1])

    return res
