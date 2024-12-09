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
________________________________________________

def isPalindrom(word):
    cleaned = word.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

    def find_palindromes(text):
        words = text.split()
        palindromes = set()

        for word in words:
            word = ''.join(char for char in word if char.isalnum())
             if isPalindromString(word) and word:
                palindromes.add(word.lower())

