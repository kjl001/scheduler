import helper

def add_task():
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

    while True:
        task = input("INPUT TASK: ")

        if len(task) <= 0:
            print("Please input a task.")
            continue
        else:
            break

    if date < 10:
        date = '0' + str(date)
    else:
        date = str(date)

    # Open schedule and add task at date for specified year and month
    schedule = []
    with open(year + '/' + month + '.txt', 'r') as file:
        schedule = file.readlines()

    index = 0
    found = False
    for line in schedule:
        if line.startswith('#'):
            if found:
                break

            # Found the correct date
            if date == line[5:7]:
                found = True
            # Passed wanted date
            elif int(date) < int(line[5:7]):
                found = True
                task = "#" + month.upper() + " " + date + " " + year + "\n" + task + "\n"
                break
        index += 1

    # End of file, not found date
    if not found:
        task = "\n#" + month.upper() + " " + date + " " + year + "\n" + task

    schedule.insert(index, task)

    with open(year + '/' + month + '.txt', 'w') as file:
        file.writelines(schedule)

    print("Returning to menu...")