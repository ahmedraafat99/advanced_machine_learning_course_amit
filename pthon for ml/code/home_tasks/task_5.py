#counter class from collection automatically counts occurrences of each word
from collections import Counter

def count_words(words):
    return Counter(words)

words = ["Welcome", "Ali", "Hi", "Ali", "No", "Hi", "No", "Ali", "No", "Ali"]
counts = count_words(words)
counts