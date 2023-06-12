# Reverse words[https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python]
def reverse_words(text):
    words = text.split()
    temp_reversed_word = []

    # Loop throught list of words
    for word in words:
        temp = ""
        # Loop through each char in reversed word
        for char in reversed(word):
            temp += char
        temp_reversed_word.append(temp)

    # Join temp list into string
    str_result = ' '.join(temp_reversed_word)

    # Add extra spaces where necessary (for edge cases)
    for i in range(len(text)):
        if text[i].isspace() and i+1 < len(text) and text[i+1].isspace():
            str_result = str_result[:i] + " " + str_result[i:]

    return str_result

# People one-liner
def reverse_words2(str):
    # Cara baca: untuk setiap huruf pada string yang dipisahkan, maka dibalik (s[::-1]) lalu semuanya dijoin menjadi string
    return ' '.join(s[::-1] for s in str.split(' '))

