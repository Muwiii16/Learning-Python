my_tasks = []
for i in range(3):
    new_item = input("Enter a new task: ")
    my_tasks.append(new_item)
    
count = 1
for item in my_tasks:
    print(f"{count}. {item}")
    count += 1
