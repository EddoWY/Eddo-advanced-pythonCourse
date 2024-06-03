def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    return " ".join((words[w] for w in sentence.split()))


print(translate("el gato esta en la casa"))
