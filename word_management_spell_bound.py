import sys
import time
import string
import random
import operator

"""This is for handling words from user input in the GUI"""
sys.setrecursionlimit(10**6)

FILEPATH = "valid.txt"
with open(FILEPATH) as f:
    words_list = f.read().splitlines()

three = [word for word in words_list if len(word) == 3]
four = [word for word in words_list if len(word) == 4]


def sort_words_list(words_list: list):
    """Quicksort the words recursively. Python's own sorted() is extremely fast. Like, really really fast"""
    if len(words_list) == 0:
        return words_list
    else:
        pivot_word = words_list[len(words_list) // 2]
        left = [words for words in words_list if words < pivot_word]
        middle = [words for words in words_list if words == pivot_word]
        right = [words for words in words_list if words > pivot_word]
        return sort_words_list(left) + middle + sort_words_list(right)


def search_words(words: str, words_list_ulti: list):
    """Try to do a more stable version this time!"""
    # This function use a more stable version that will not destroy the list in the process
    words = words.upper()
    upper = len(words_list_ulti)
    lower = 0
    while len(words_list_ulti[lower:upper]) > 0:
        middle_index = len(words_list_ulti[lower:upper]) // 2 + lower
        temp = words_list_ulti[lower:upper]
        if words < words_list_ulti[middle_index]:
            upper = middle_index
        elif words > words_list_ulti[middle_index]:
            lower = middle_index
        elif words == words_list_ulti[middle_index]:
            return True, middle_index
        if len(temp) == 1:
            if words != temp[0]:
                return False, middle_index

    # Edge case in case the parameter list is empty!
    if len(words_list_ulti) == 0:
        return False, 0


def shuffle():
    list_letters = []
    alphabet_list = list(string.ascii_uppercase)
    vowels_list = ["A", "E", "I", "O", "U"]
    consonants_list = [letter for letter in alphabet_list if letter not in vowels_list]
    first = random.randint(0, 100)
    if first >= 26:
        num_vowels = random.randint(2, 3)
        list_letters += random.sample(vowels_list, num_vowels)
        list_letters += random.sample(consonants_list, 7 - num_vowels)
    elif first <= 25:
        print("LOL")
        three_letter = random.choice(sorted_three)
        four_letter = random.choice(sorted_four)
        list_letters = list(three_letter + four_letter)
    random.shuffle(list_letters)
    return


start_time = time.time()
sorted_all = sort_words_list(words_list)
sorted_three = sort_words_list(three)
empty_list = []
boom = {"A": 7.8, "B": 2, "C": 4, "D": 3.8, "E": 11, "F": 1.4, "G": 3, "H": 2.3, "I": 8.6,
        "J": 0.21, "K": 0.97, "L": 5.3, "M": 2.7, "N": 7.2, "O": 6.1, "P": 2.8, "Q": 0.19,
        "R": 7.3, "T": 6.7, "U": 3.3, "V": 1, "W": 0.91, "X": 0.27, "Y": 1.6, "Z": 0.44, "S": 8.7}
boom = sorted(boom.items(), key=operator.itemgetter(1), reverse=True)
sorted_four = sort_words_list(four)
print(f"--- {time.time() - start_time} seconds ---")
