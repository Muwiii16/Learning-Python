my_tasks = []
is_running = True

while is_running:

    user_choice = input(
        "\nWhat would you like to do? (add/view/exit): ").lower()
    if user_choice == 'add':
        new_item = input("\nPlease enter a new task: ")
        my_tasks.append(new_item)
        print(f"Added: {new_item}")
    elif user_choice == 'view':
        if len(my_tasks) == 0:
            print("Your list is empty! Go take a nap.")
        else:
            print("\n --- To-Do List ---")
            for count, item in enumerate(my_tasks):
                print(f"{count+1}. {item}")
            list_choice = input(
                "\nHave you completed any of these tasks? (yes/no): ").lower()
            if list_choice == 'yes':
                completed_task = int(
                    input("Please enter the number of the completed task: "))
                if 0 < completed_task <= len(my_tasks):
                    removed_task = my_tasks.pop(completed_task - 1)
                    print(
                        f'The task "{removed_task}"" has been removed from your list.')
                else:
                    print("Invalid task number.")
    elif user_choice == 'exit':
        is_running = False
    else:
        print("Invalid choice. Please choose 'add', 'view', or 'exit'.")
