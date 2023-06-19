import PySimpleGUI as sg
import pandas as pd
import get_weather


# Read the CSV file
df = pd.read_csv('airport-codes.csv')

# Get the values for the dropdowns from the respective columns
codes = df['icao'].tolist()

def currentDate(returnType='tuple'):
    """ Get the current date and return it as a tuple, list, or dictionary.
    Args:
        returnType (str): The type of object to return. Valid values are 'tuple', 'list', or 'dict'.
    """
    from datetime import datetime
    now = datetime.now()
    if returnType == 'tuple':
        return now.month, now.day, now.year
    elif returnType == 'list':
        return [now.month, now.day, now.year]
    elif returnType == 'dict':
        return {'day': now.day, 'month': now.month, 'year': now.year}
    else:
        raise ValueError("Invalid returnType. Valid values are 'tuple', 'list', or 'dict'.")

def gui():
    # Create a list of months, days, and years
    months = list(range(1, 13))
    days = list(range(1, 32))
    currentYear = currentDate()

    years = list(range(2000, currentYear[2] + 1))
    filter_options = ['daily', 'weekly', 'monthly']

    # Define the layout of the window
    layout = [
        [sg.Text('Select a date:')],
        [
            [sg.Text('Month:')], [sg.Combo(months, key='-MONTH-', size=(30, 1), readonly=True)],
            [sg.Text('Day:')], [sg.Combo(days, key='-DAY-', size=(30, 1), readonly=True)],
            [sg.Text('Year:')], [sg.Combo(years, key='-YEAR-', size=(30, 1), readonly=True)],
            [sg.Text('Code:')], [sg.Combo(codes, key='-CODE-', size=(30, 1), readonly=True)],
            [sg.Text('Filter:')], [sg.Combo(filter_options, key='-FILTER-', size=(30, 1), readonly=True)]
        ],
        [sg.Button('Submit'), sg.Button('Cancel')]
    ]

    # Create the window
    window = sg.Window('Date Selection', layout)

    selected_date = None  # Variable to store the selected date

    while True:
        event, values = window.read()

        # Handle events
        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break
        elif event == 'Submit':
            month = values['-MONTH-']
            day = values['-DAY-']
            year = values['-YEAR-']
            code = values['-CODE-']
            filter = values['-FILTER-']
            selected_date = f'{month}/{day}/{year}'

            # Create a custom result window
            result_layout = [
                [sg.Text(f'You selected\nDate:{selected_date}\nCode: {code}\nFilter: {filter}',justification='center')],
                [sg.Button('OK')]
            ]
            result_window = sg.Window('Details', result_layout, size=(600, 200), element_justification='center')

            base_url = "https://www.wunderground.com/history"
            # build the url to scrape weather from
            # url = f"{base_url}/{filter}/{code}/date/{year}-{month}-{day}"
            url = f"{base_url}/{filter}/{code}/date/{year}-{month}-{day}"
            # print(url)
            
                        
            while True:
                event, _ = result_window.read()
                
                if event == sg.WINDOW_CLOSED or event == 'OK':
                    break
            
            result_window.close()
            return url
    
    window.close()


if __name__ == '__main__':
    url = gui()
    print(url)
    print(type(url))
    get_weather.mainfunction(url)
