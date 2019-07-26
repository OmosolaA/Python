#3.Palindrome
#Write a function that takes in a word and determines if it is a palindrome.
#Palindrome = a word that is spelled the same way forward and backward.
#Example: racecar spelled backwards is racecar
print(" Is your word a palindrome?  ")
print(" You have 10 tries ")
for i in range(10):
    palindrome = input("Enter a word: ")
#hile palindrome != 'STOP':
    palindrome = palindrome.lower()
    reversepal = palindrome[::-1]
    if palindrome == reversepal:
        print(palindrome + " is a palindrome!")
    else:
        print(palindrome + " is not a palindrome!")
    #if palindrome == 'STOP':
      #  break
    
