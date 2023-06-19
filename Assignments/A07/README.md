## Project Title : Web Scraping
## Name : Nitish Kumar Erelli
## Project Description : 
This project is a data retrieval and display application that allows users to fetch weather data from Wunderground based on specified parameters and view it in a tabular format. It utilizes PySimpleGUI for creating the data entry form, Selenium for fetching async data from Wunderground, and BeautifulSoup (BS4) for parsing the retrieved data.

## Requirements

- Python 3.x
- PySimpleGUI
- Selenium
- BeautifulSoup4

## Installation

1. Clone the repository or download the project files.

2. Install the required Python packages:

```shell
pip install PySimpleGUI selenium beautifulsoup4
```

3. Download the appropriate WebDriver for your browser. Selenium requires a WebDriver to interface with the chosen browser. Make sure to place the WebDriver executable in a directory included in your system's PATH variable.

   - For Chrome: [ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)
   - For Firefox: [GeckoDriver - WebDriver for Firefox](https://github.com/mozilla/geckodriver/releases)
   - For Edge: [EdgeDriver - WebDriver for Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

## Usage

1. Open a terminal or command prompt and navigate to the project directory.

2. Run the `main.py` file:

```shell
python3 main.py
```

3. The application will launch, displaying a data entry form with the following fields: day, month, year, airport, and filter (daily, weekly, monthly).

4. Enter the desired values in the form fields.

5. Click the "Submit" button to create the appropriate URL to query Wunderground for the specified weather data.

6. Selenium will automatically open a browser window, navigate to the generated URL, and retrieve the async data from Wunderground.

7. BS4 will parse the retrieved data and extract the requested weather data.

8. Finally, the application will display the received data in a tabular view using PySimpleGUI.

9. Close the application window to exit the program.

## Customization

- You can customize the application by modifying the form layout, adding or removing form fields, or adjusting the data parsing logic to suit your specific needs.

- Additionally, you can enhance the user interface by modifying the PySimpleGUI code for the tabular view to customize the appearance and behavior of the displayed data.
