def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if low_index >= high_index:
        return True
    if word[low_index] != word[high_index]:
        return False
    if not word:
        return False
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
