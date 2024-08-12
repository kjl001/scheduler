################################################
# Create a schedule system
# Have a selector to select to add task or view tasks
# Add multiple tasks to a single day
# Allow viewing how many tasks are there on a month with month view
# Have different date inputs like 8-9-24 or 08-09-2024 or Aug 9, 2024
################################################

option = input("Do you want to [1] ADD a task or [2] VIEW a task?: ").strip().lower()
match option:
    case '1' | 'add':
        import add
    case '2' | 'view':
        import view