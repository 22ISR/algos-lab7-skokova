def isPalindrom(word):
    cleaned = word.lower()
    return cleaned == cleaned[::-1]
    cleaned1 = cleaned.replace("_", "")
print(isPalindrom("l evel"))
