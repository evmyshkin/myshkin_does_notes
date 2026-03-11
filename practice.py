"""Задача 1: Нужно написать функцию, которая определяет является ли строка палиндромом (
стандартная задача с литкода).

Доп. вопросы:

Определить сложность алгоритма по времени и по памяти;
Перепишите код так, чтобы было O(1) по памяти.
"""
from curses.ascii import isalnum


def is_palindrom(s: str) -> bool:
    """Определяет, является ли строка палиндромом.

    >>> is_palindrom('aaa')
    True

    >>> is_palindrom('aa')
    True

    >>> is_palindrom('ab')
    False

    >>> is_palindrom('ab')
    False

    >>> is_palindrom('9A man, a plan, a canal: Panama9')
    True

    >>> is_palindrom('')
    True
    """

    if len(s) < 2:
        return True

    l = 0
    r = len(s) - 1

    while l < r:
        if not isalnum(s[l]):
            l += 1
            continue
        if not isalnum(s[r]):
            r -= 1
            continue
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1

    return True


is_palindrom('9A man, а plan, а canal: Panama9')
