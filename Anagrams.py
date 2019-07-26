#4. Anagram
#Write a function that takes in two words and determines if the words are an anagram
#of each other. Anagram = A word created by rearranging the letters of another word.
#Example: iceman and cinema


word1 = input("Enter your first word: ")
first = list(word1)

word2 = input("Enter your second word: ")
second = list(word2)

first.sort()
second.sort()

print(first)
print(second)

def Anagram():
    if first == second:
        print(word1)
        print(" and ")
        print(word2)
        print(" make an anagram!")
    else:
        print(word1)
        print(" and ")
        print(word2)
        print(" do not make an anagram! Please try again")

Anagram()
