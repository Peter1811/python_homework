from collections import Counter
import re

def count_words(string):
    words = list(map(lambda x: x.lower(), re.split(',| |\.', string)))
    count = Counter(words)
    return len(count)

print(count_words("Привет, мир! Это пример, пример текстов для теста."))
