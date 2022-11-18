def is_palindrome_iterative(word):
    first_element = 0
    last_element = len(word) - 1

    if not word:
        return False

    while first_element <= last_element:
        if word[first_element] != word[last_element]:
            return False
        else:
            first_element += 1
            last_element -= 1

    return True
