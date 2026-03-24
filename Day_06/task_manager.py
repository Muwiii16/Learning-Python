my_tasks = []
for i in range(3):
    new_item = input("Enter a new task: ")
    my_tasks.append(new_item)

print(f"You have {len(my_tasks)} tasks to do!")
for index, tasks in enumerate(my_tasks, start = 1):
    print(f"{index}. {tasks}")

done_task=int(input("Which task number did you finish?"))
my_tasks.pop(done_task-1)
