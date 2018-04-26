def anagrams(word, words):
    anagram_list = []
    for n in words:
        if sorted(n) == sorted(word):
            anagram_list.append(n)
    return anagram_list