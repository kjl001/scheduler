def convert_month(input_month):
    month_map = {
        'jan': ['january', 'jan', '01', '1'],
        'feb': ['february', 'feb', '02', '2'],
        'mar': ['march', 'mar', '03', '3'],
        'apr': ['april', 'apr', '04', '4'],
        'may': ['may', '05', '5'],
        'jun': ['june', 'jun', '06', '6'],
        'jul': ['july', 'jul', '07', '7'],
        'aug': ['august', 'aug', '08', '8'],
        'sept': ['september', 'sept', '09', '9'],
        'oct': ['october', 'oct', '10'],
        'nov': ['november', 'nov', '11'],
        'dec': ['december', 'dec', '12']
    }

    for key in month_map.keys():
        if input_month in month_map[key]:
            return key
        
    return None

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
    month = convert_month(month) # convert input month to the correct month key
    if month is not None:
        break
    print("Inputted MONTH is not a valid month!")

# Loop through selected schedule
file = open(year + '/' + month + '.txt', 'r')
while True:
    schedule = file.readline().rstrip('\n')
    if not schedule:
        break
    print(schedule)


file.close()