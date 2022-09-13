def count_alphabet_from_sentence(sentence: str) -> int:
    alphabets_count = 0
    for word in sentence:
        for string in word:
            if string.isalpha():
                alphabets_count += 1
    return alphabets_count


def count_words_from_sentence(sentence: str) -> int:
    return len(sentence.split())


def count_vowels_from_sentence(sentence: str) -> int:
    vowels = 0
    vowel_char = "aiueo"
    for word in sentence:
        for string in word:
            if string in vowel_char:
                vowels += 1
    return vowels


print("""
    Program penghitung kata, huruf konsonan, dan huruf vokal
""")

sentence = input("Inputkan kalimat: ")

words = count_words_from_sentence(sentence)
vowels = count_vowels_from_sentence(sentence)
alphabets = count_alphabet_from_sentence(sentence)

print("""
    Jumlah kata: {}
    Jumlah semua huruf: {}
    Jumlah huruf vokal: {}
""".format(words, alphabets, vowels))