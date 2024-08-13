################################################
# Create a schedule system
# Have a selector to select to add task or view tasks
# Add multiple tasks to a single day
# Allow viewing how many tasks are there on a month with month view
# Have different date inputs like 8-9-24 or 08-09-2024 or Aug 9, 2024
################################################

import add as a
import view as v

while True:
    option = input("Do you want to [1] ADD a task; [2] VIEW a task; [3] REMOVE a task; [4] EXIT?: ").strip().lower()
    match option:
        case '1' | 'add':
            a.add_task()
        case '2' | 'view':
            v.view_task()
        case '3' | 'remove':
            print("REMOVE")
        case '4' | 'exit':
            print("Exiting...")
            exit()