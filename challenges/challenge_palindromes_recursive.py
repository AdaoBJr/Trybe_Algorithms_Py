def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False
    if len(word) <= 2 and word[0] == word[-1]:
        return True
    else:
        return is_palindrome_recursive(
            word[1:-1], low_index, high_index
        )
