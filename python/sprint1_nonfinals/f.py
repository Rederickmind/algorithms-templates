import string


def is_palindrome(line: str) -> bool:
    delete_sym = string.punctuation + ' '
    prep_line = line.lower()
    for c in delete_sym:
        if c in prep_line:
            prep_line = prep_line.replace(c, '')
    prep_line.strip('')
    reverse_line = prep_line[::-1]
    if prep_line == reverse_line:
        return True
    else:
        return False


print(is_palindrome(input().strip()))
