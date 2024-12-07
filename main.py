def isPalindrom(word):
    cleaned = word.lower().replace(" ", "").replace(",", "")
    return cleaned == cleaned[::-1]
print(isPalindrom("l,evel"))

___________________________________________
def isPalindrom(word):
    cleaned = word.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def isPalindromList(words):
    palindromes = []
    for word in words:
        if isPalindrom(word):
            palindromes.append(word)
    return palindromes
print(isPalindromList(["hello", "list", "level"]))  


