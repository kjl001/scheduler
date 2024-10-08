import helper

def remove_task():
    scheduled_years = ['2024', '2025', '2026']

    # Read user input for the year
    while True:
        year = input("SELECT YEAR: ").strip().lower()
        if year in scheduled_years:
            break
        print("Inputted YEAR has not been scheduled!")
        
    # Read user input for the month
    while True:
        month = input("SELECT MONTH: ").strip().lower()
        month = helper.convert_month(month) # convert input month to the correct month key
        if month is not None:
            break
        print("Inputted MONTH is not a valid month!")

    while True:
        date = input("SELECT DATE: ").strip().lower()

        # Check if date is a number
        if not date.isnumeric():
            print("Please enter a number.")
            continue

        # Check if date is in range
        date = int(date)
        if month in ['jan', 'mar', 'may', 'jul', 'aug', 'oct', 'dec'] and (date > 31 or date < 1):
            print("Please select a date from 1 to 31.")
            continue
        if month in ['apr', 'jun', 'sept', 'nov'] and (date > 30 or date < 1):
            print("Please select a date from 1 to 30")
            continue
        if month == 'feb' and (date > 29 or date < 1):
            print("Please select a date from 1 to 29")
            continue

        break

    # Make single digit dates into double digits
    if date < 10:
        date = '0' + str(date)
    else:
        date = str(date)

    # Put schedule into a list
    schedule = []
    with open(year + '/' + month + '.txt', 'r') as file:
        schedule = file.readlines()

    # Start finding the date to remove from
    index = 0
    start_index = 0
    found = False
    for line in schedule:
        # Found a date line or end of file
        if line.startswith('#') or index == len(schedule)-1:
            if index == len(schedule)-1:
                index += 1
            # Date has been found
            if found:
                print("\nHere are the tasks at your selected date:")
                for task_num in range(start_index, index):
                    print(schedule[task_num].rstrip('\n'))
                print("")

                # Wait for user input to remove task
                while True:
                    remove = input("Input task number to remove or [0] to exit: ")
                    # Improper number inputted
                    if (not remove.isnumeric()) or  int(remove) >= (index - start_index) or int(remove) < 0:
                        print("Please input a proper task number.")
                        continue
                    # Exit number
                    elif int(remove) == 0:
                        break
                    # Proper number inputted, remove task
                    else:
                        del schedule[start_index + int(remove)]
                        index -= 1
                        
                        # All tasks have been removed
                        if index - start_index <= 1:
                            del schedule[start_index + int(remove)-1]
                            print("All tasks removed!")
                            break

                        # Print updated tasks
                        print("\nTask removed. Here are the updated tasks:")
                        for task_num in range(start_index, index):
                            print(schedule[task_num].rstrip('\n'))
                        print("")

                break

            # Found the correct date
            elif date == line[5:7]:
                found = True
                start_index = index

        index += 1

    # Update file with new tasks
    with open(year + '/' + month + '.txt', 'w') as file:
        file.writelines(schedule)
    
    print("\nReturning to menu...")