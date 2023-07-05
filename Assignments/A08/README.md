
## Project Title : Fast Api with Covid Data

## Name : Nitish Kumar Erelli

## Project Description :

This project is a RESTful API created using FastAPI that provides access to COVID-19 data. The API fetches data from a publicly available data source and exposes endpoints to retrieve various statistics related to COVID-19 cases.

## Table of Contents

- [Endpoints](#endpoints)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Additional Functionalities](#additional-functionalities)
- [Implementation Process](#implementation-process)
- [Challenges Faced](#challenges-faced)

## Endpoints

The API exposes the following endpoints:

 <img src="https://github.com/nitishkumar2306/4883-SoftwareTools-Erelli/blob/main/Assignments/A08/Output/api_home_page.png" height="400" width="1000">

### `/countries/`

- Retrieves a list of unique countries with COVID-19 data.
  
  <img src="https://github.com/nitishkumar2306/4883-SoftwareTools-Erelli/blob/main/Assignments/A08/Output/api_country.png" height="350" width="1000">


### `/regions/`

- Retrieves a list of unique WHO regions with COVID-19 data.

  <img src="https://github.com/nitishkumar2306/4883-SoftwareTools-Erelli/blob/main/Assignments/A08/Output/api_region.png" height="350" width="1000">


### `/deaths`

- Retrieves total deaths for all countries.

  <img src="https://github.com/nitishkumar2306/4883-SoftwareTools-Erelli/blob/main/Assignments/A08/Output/api_deaths_1.png" height="300" width="1000">

  <img src="https://github.com/nitishkumar2306/4883-SoftwareTools-Erelli/blob/main/Assignments/A08/Output/api_deaths_2.png" height="300" width="1000">

### `/deaths?country=Brazil`

- Retrieves the total deaths for the given country.

### `/deaths?region=AFRO`

- Retrieves the total deaths for the given region.

### `/deaths?country=France&year=2020`

- Retrieves the total deaths for the given country in a specified year.

### `/deaths?region=AFRO&year=2020`

- Retrieves the total deaths for the given region in a specified year.


### `/max_deaths?min_date=2021-06-01&max_date=2021-12-31`

- Retrieves the maximum number in given range of dates.

  <img src="https://github.com/nitishkumar2306/4883-SoftwareTools-Erelli/blob/main/Assignments/A08/Output/api_max_deaths.png" height="350" width="1000">

### `/max_deaths`

- Retrieves the country that has maximum number of deaths.

  <img src="https://github.com/nitishkumar2306/4883-SoftwareTools-Erelli/blob/main/Assignments/A08/Output/api_max_deaths.png" height="350" width="1000">

### `/min_deaths?min_date=2021-06-01&max_date=2021-12-31`

- Retrieves the maximum number in given range of dates.

  <img src="https://github.com/nitishkumar2306/4883-SoftwareTools-Erelli/blob/main/Assignments/A08/Output/api_min_deaths.png" height="350" width="1000">

### `/min_deaths`

- Retrieves the country that has maximum number of deaths.

  <img src="https://github.com/nitishkumar2306/4883-SoftwareTools-Erelli/blob/main/Assignments/A08/Output/api_min_deaths.png" height="350" width="1000">

### `/avg_deaths/`

- Retrieves the average number of deaths per country.

  <img src="https://github.com/nitishkumar2306/4883-SoftwareTools-Erelli/blob/main/Assignments/A08/Output/api_avg_deaths.png" height="350" width="1000">

## Installation and Setup

1. Clone this repository to your local machine.

```bash
git clone https://github.com/your-username/A08-FastAPI-COVID-19-Data.git
```

2. Install the required Python packages using pip.

```bash
pip install -r requirements.txt
```

3. Run the FastAPI application.

```bash
uvicorn main:app --reload
```

## Usage

Once the FastAPI application is running, you can access the API at http://localhost:8000.

To retrieve data, make GET requests to the respective endpoints mentioned above using tools like curl, Postman, or your web browser.

Example: Retrieve total deaths for all countries

```
GET http://localhost:8000/deaths
```

Example: Retrieve total deaths for France in the year 2020

```
GET http://localhost:8000/deaths?country=France&year=2020
```

## Additional Functionalities

You can extend the API to include more data points, such as new cases, cumulative cases, or recovery rates. Additionally, you can implement error handling for invalid input and add pagination support for large datasets.

## Implementation Process

The implementation process involved creating a FastAPI application, defining routes, and handling requests to fetch and process COVID-19 data from a publicly available data source. Pandas library was used to read the CSV data and perform data manipulations.

## Challenges Faced

Some of the challenges faced during the implementation included handling date formats, ensuring data consistency, and optimizing data retrieval for faster response times.

