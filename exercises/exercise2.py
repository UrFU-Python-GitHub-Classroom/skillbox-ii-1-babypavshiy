"""Любимый палиндром"""
def is_palindrome(s: str) -> bool:
    if s[::-1] == s:
        return True
    return False

"""Возващает False если слово не является палиндромом и True в противном случае"""

