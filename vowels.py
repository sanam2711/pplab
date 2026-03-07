def containsvowel(word):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for char in word:
        if char in vowels:
            return True
    return False


userword = input("enter word: ")

if containsvowel(userword):
    print("word has vowels")
else:
    print("word not contains vowels")

