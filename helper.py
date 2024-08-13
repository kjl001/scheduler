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
        'sep': ['september', 'sept', 'sep', '09', '9'],
        'oct': ['october', 'oct', '10'],
        'nov': ['november', 'nov', '11'],
        'dec': ['december', 'dec', '12']
    }

    for key in month_map.keys():
        if input_month in month_map[key]:
            return key
        
    return None