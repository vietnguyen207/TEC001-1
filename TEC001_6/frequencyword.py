def frequencyw(text):
    freq = {}
     
    text = text.lower()
    text = text.replace(".", "").replace(",", "").replace("!", "").replace("?", "")
    
    words = text.split()
    
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    return print(freq)
text = input("Enter a piece of text: ")
frequencyw(text)