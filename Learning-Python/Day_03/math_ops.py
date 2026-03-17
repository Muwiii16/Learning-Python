user_age = int(input("How old are you?: "))
friends_age = int(input("How old is your friend?: "))

print(user_age > friends_age)
print(user_age == 18)


phrase = "Python is amazing"

print("Python" in phrase)
print("Java" in phrase)
print("z" not in phrase)

list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

print(list_a == list_b)
print(list_a is list_b)
print(list_a is list_c)


x1, y1 = 2, 2
x2, y2 = 6, 10

slope = (y2-y1)/(x2-x1)
print("The slope is: ", slope)


sentence = input("Enter a sentence: ")
letter = input("Enter a letter: ")
print(letter in sentence)
print(len(sentence))
print(len(sentence) % 4 == 0)
