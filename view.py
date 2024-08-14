import helper

def view_task():
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

    # Loop through selected schedule
    with open(year + '/' + month + '.txt', 'r') as file:
        print("")
        while True:
            schedule = file.readline().rstrip('\n')
            if not schedule:
                break
            print(schedule)

    print("\nReturning to menu...")