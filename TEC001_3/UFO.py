def acronym(phrase):
    words = phrase.split()
    return ''.join(word[0].upper() for word in words)
phrase = input("Enter a phrase: ")
print(acronym(phrase))