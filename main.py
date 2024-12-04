def isPalindrom(word):
    cleaned = word.lower().replace(" ", "")
    cleaned1 = word.lower().replace(".", "")
    return cleaned == cleaned[::-1]
print(isPalindrom("l,evel"))
