def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

    while True:
        date = input('Date: ')
        
        if ',' in date:
            month_day, year = date.split(', ')
            month, day = month_day.split(' ')
            
            try:
                month = str(months.index(month.capitalize()) + 1)
            except ValueError:
                pass
            else:
                day = add_leading_zero(day)
                month = add_leading_zero(month)
                print(f'{year}-{month}-{day}')    
        
        
        if '/' in date:
            month, day, year = date.split('/')
            
            month = add_leading_zero(month)
            day = add_leading_zero(day)
            
            print(f'{year}-{month}-{day}')
    

def add_leading_zero(value: str) -> str:
    """Function that adds leading zero for single digits"""
    return f'0{value}' if (len(value) < 2) else value
    

if __name__ == '__main__':
    main()
