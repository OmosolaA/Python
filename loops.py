#CHAPTER 7
# 1. Print each item in the following list
listOfItems = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]

for items in listOfItems:
    print(items)


# 2. Print all numbers from 25 to 50
i = 0
for i in range(25, 51):
    print(i)
    i += 1


# 3. Print each item in the list from the first challenge and their indexes
j = 0
for items in listOfItems:
    #for j in range(items):
        print(items)

# 4. Write a program with an infinite loop (with the option to type q to quit) and a list
# of numbers. Each time through the loop ask the user to guess a number on the list and tell them
# whether or not they guessed correctly


    

# 5. Mulitply all the numbers in the list [ 8, 19, 148, 4] with all the numbers
# in the list [9, 1, 33, 83] and append each result to a third list
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []
k = 0
l = 0 
for k in list1:
    for l in list2:
        product = k * l
        list3.append(product)

print(list3)

for m in range(len(list1)):
    for n in range(len(list2)):
                   product = list1[m] * list[n]
                   list3.append(product)


print(list3)



