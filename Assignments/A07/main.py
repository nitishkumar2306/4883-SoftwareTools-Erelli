import PySimpleGUI as sg
import pandas as pd
import get_weather
from calendar import monthrange
from bs4 import BeautifulSoup

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

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def gui():
    # Create a list of months, years, and filter options
    months = list(range(1, 13))
    currentYear = currentDate()
    years = list(range(2000, currentYear[2] + 1))
    filter_options = ['daily', 'weekly', 'monthly']

    # Define the layout of the window
    layout = [
        [
            [sg.Text('Year:')], [sg.Combo(years, key='-YEAR-', size=(30, 1), readonly=True)],
            [sg.Text('Month:')], [sg.Combo(months, key='-MONTH-', size=(30, 1), readonly=True, enable_events=True)],
            [sg.Text('Day:')], [sg.Combo([], key='-DAY-', size=(30, 1), readonly=True)],
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
        elif event == '-MONTH-':
            month = int(values['-MONTH-'])
            year = int(values['-YEAR-'])
            
            if month == 2:
                num_days = 29 if is_leap_year(year) else 28
            else:
                num_days = monthrange(year, month)[1]
            
            window['-DAY-'].update(values=list(range(1, num_days + 1)))
        elif event == 'Submit':
            month = int(values['-MONTH-'])
            day = int(values['-DAY-'])
            year = int(values['-YEAR-'])
            code = values['-CODE-']
            filter = values['-FILTER-']
            selected_date = f'{month}/{day}/{year}'

            # Create a custom result window
            result_layout = [
                [sg.Text(f'You selected\nDate: {selected_date}\nCode: {code}\nFilter: {filter}', justification='center')],
                [sg.Button('OK')]
            ]
            result_window = sg.Window('Details', result_layout, size=(600, 200), element_justification='center')

            base_url = "https://www.wunderground.com/history"
            # Build the URL to scrape weather from
            url = f"{base_url}/{filter}/{code}/date/{year}-{month}-{day}"
            
            while True:
                event, _ = result_window.read()
                
                if event == sg.WINDOW_CLOSED or event == 'OK':
                    break
            
            result_window.close()
            return url
    
    window.close()

def ShowData(history):
     # Extract table headers and rows from the data element
    headers = [header.get_text(strip=True) for header in history.find_all('th')]
    rows = []
    for row in history.find_all('tr'):
        rows.append([data.get_text(strip=True) for data in row.find_all('td')])

    # Create PySimpleGUI layout for the table
    # Create PySimpleGUI layout for the table with adjusted column widths
    layout = [
    [sg.Table(values=rows, headings=headers, justification='left', col_widths=[20, 20])]
]

    # Create PySimpleGUI window and display the table
    window = sg.Window('Observations', layout)
    event, values = window.read()
    window.close()


def flatten_nested_tables(table_element):

    thead=table_element.find('thead')

    if thead is not None:
        headers = [header.get_text(strip=True) for header in thead.find_all('td')]
    else:
        headers = []  # or any default value you want to assign

    tbody=table_element.find('tbody')
    tables=tbody.find_all('table')


    flattened_data = []
    for table in tables:
        rows = table.find_all('tr')
        table_data=[]
        data_row=[]
        for row in rows:
           
            cells = row.find_all('td')
            for cell in cells:
                # data_row.append(cell.text.strip())  
                data_row.append(cell.text.strip() + ' ')
        table_data.append(" ".join (data_row))
            
        flattened_data.append(table_data)
    # print(flattened_data)    

    # Separate the headers and data
    convert_list = []

    # Iterate through each sublist in flattened_data
    for sublist in flattened_data:
        #print(sublist[0][0].split())
        if len(flattened_data[0][0].split()) < len(sublist[0].split()):
            # Split sublist into groups of three items
            items = sublist[0].split() # Exclude the first item (e.g., 'Max', 'Avg', 'Min')
            row = [items[i:i+3] for i in range(0, len(items), 3)]
            print(row)
        else:
            row=sublist[0].split()
        convert_list.append(row)

    # Split sublist into individual items
    # Transpose the convert_list
    print(convert_list)
    convert_list_1 = list(map(list, zip(*convert_list)))

    print( convert_list_1)
    return convert_list_1,headers

def display_table_data( table_data,headersata):

    layout = [
        [sg.Table(values=table_data, headings=headersata,justification='center')],
        [sg.Button('OK')]
    ]

    window = sg.Window('Table Data', layout, finalize=True)
    while True:
        event, _ = window.read()
        if event == sg.WINDOW_CLOSED or event == 'OK':
            break
    window.close()

if __name__ == '__main__':
    url = gui()
    # url = 'https://www.wunderground.com/history/monthly/CYOW/date/2007-7-6'
    print(url[37:41])   
    bs4_data = get_weather.mainfunction(url)

    if(url[37:41] == 'mont' or url[37:41] == 'week'):
        # Extract the table data recursively
        table_data,headers = flatten_nested_tables(bs4_data)

        # Display the table data using PySimpleGUI
        display_table_data( table_data,headers)
    else:
        ShowData(bs4_data)
  

