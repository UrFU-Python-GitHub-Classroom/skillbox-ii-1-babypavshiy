def is_palindrome(s: str) -> bool:
    if (s[::-1] == s):
        return True
    return False