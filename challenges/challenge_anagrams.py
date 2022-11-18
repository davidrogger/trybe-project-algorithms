from challenges.quick_sort import quick_sort


def quick_sort_word(word):
    letters = list(word.lower())
    quick_sort(letters)
    new_ordered_word = "".join(letters)
    return new_ordered_word


def is_anagram(first_string, second_string):
    first_string_ordered = quick_sort_word(first_string)
    second_string_ordered = quick_sort_word(second_string)

    anagram = first_string_ordered == second_string_ordered

    if not first_string and not second_string:
        anagram = False

    return (first_string_ordered, second_string_ordered, anagram)
