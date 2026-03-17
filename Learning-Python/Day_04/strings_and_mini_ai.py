var = "Hello, I am your AI assistant"

print(var[0:5])
print(var[20:])

raw_input = "  SEARCH for Python Slicing   "

clean_input = (raw_input.strip().lower())
print(clean_input.find("search"))
print(clean_input[11:])

user_name = input("Please enter your name: ")
user_birth_year = (input("Please enter the year you were born: "))
clean_name = user_name.strip()
clean_birth_year = user_birth_year.strip()
age = 2024-int(clean_birth_year)
print(f"Hello {clean_name}, you are {age} years old!")