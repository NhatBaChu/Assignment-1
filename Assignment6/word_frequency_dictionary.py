def word_frequency(text):

    words = text.split()
    freq = {}

    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1

    return freq


sentence = input("Enter text: ")
result = word_frequency(sentence)

print(result)