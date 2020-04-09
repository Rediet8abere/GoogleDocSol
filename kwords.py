"""Given a string of text and a number k, find the k words in the given text that
 appears more frequently.Return the words in a new array sorted in decreasing order

input: text(str), k(int)
output: array
one fish two fish red fish blue fish one love true love
3 """



def kwords(text, k):
    freq_words = {}
    text = text.split()
    for i in range(len(text)):
        if text[i] not in freq_words:
            freq_words[text[i]] = 1
        else:
            freq_words[text[i]] += 1
    print("freq_words: ", freq_words)
    words = []
    # freq_words_keys = list(freq_words.keys())
    # freq_words_v = list(freq_words.values())
    freq_words_values =sorted(list(freq_words.values()))
    for i in range(1, k+1):
        for word, freq in freq_words.items():
            if freq == freq_words_values[-i] and word not in words:
                words.append(word)
    print("words: ", words)
    return words


print("frequent words: ", kwords("one fish two fish red fish blue fish one love true love one", 3))
