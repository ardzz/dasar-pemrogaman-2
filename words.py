def count_words_from_sentence(sentence: str) -> int:
    return len(sentence.split())


def count_alphabets_from_word(word: str) -> int:
    return len(word)


def remove_symbols_from_word(word: str) -> str:
    output = ""
    for char in word:
        if char.isalpha():
            output += char
    return output


def get_vowel_count_from_word(word: str) -> int:
    vowel = "aiueo"
    count = 0
    for char in word:
        if char in vowel:
            count += 1
    return count


def count_each_vowel_from_word(word: str) -> dict:
    vowel = "aiueo"
    count = {}
    for char in word:
        if char in vowel:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    return count


def count_each_alphabet_from_word(word: str) -> dict:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count = {}
    for char in word:
        if char in alphabet:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    return count


def count_each_consonant_from_sentence(sentence: str) -> dict:
    consonant = "bcdfghjklmnpqrstvwxyz"
    count = {}
    for char in sentence:
        if char in consonant:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    return count


def count_each_word_from_sentence(sentence: str) -> dict:
    count = {}
    for word in sentence.split():
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count


def count_each_consonant_from_word(word: str) -> dict:
    consonant = "bcdfghjklmnpqrstvwxyz"
    count = {}
    for char in word:
        if char in consonant:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    return count
