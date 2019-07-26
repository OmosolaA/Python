#1. Reverse a string using a stack

#word = "Steven"

#word = Stack()
#word.pop()
#print(word)

#2. Use a stack to create a new list with the items in the following list reversed: [1, 2, 3, 4, 5]

numbers = [1, 2, 3, 4, 5]

newList = []
while len(numbers) > 0: 
    item = numbers.pop()
    newList.append(item)

print(newList)
