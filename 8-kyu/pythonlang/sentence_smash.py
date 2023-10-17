def smash(words):
    new_string = ''
    for word in words:
        if new_string == '':
            new_string += word
        else:
            new_string = new_string + ' ' + word
    
    return new_string
    
# One liner
def smash(words):
    return " ".join(words)
