from fastapi import FastAPI, Query
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import csv
from datetime import datetime



app = FastAPI()

db = []

# Open the CSV file
with open('data.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    i = 0
    # Read each row in the CSV file
    for row in reader:
        if i == 0:
            i += 1
            continue
        db.append(row)


def getUniqueCountries():
    global db
    countries = {}

    try:
        for row in db:
            if not row[2] in countries:
                countries[row[2]] = 0
    except Exception as e:
        print("An error occurred:", str(e))
        return []

    return {"countries": list(countries.keys()), "success": True}



def getUniqueRegions():

    regions = {}

    try:
        for row in db:
            if not row[4] in regions:
                regions[row[3]] = 0
    except Exception as e:
        print("An error occurred:", str(e))
        return []
    return {"regions": list(regions.keys()),"success": True}


def getTotalDeaths(country, region, year):

   sumOfDeaths = 0
   try:
    if country and region:
        return {"error": "Cannot provide both country and region parameters. Please provide either country or region."}
    if country and year:
        for row in db:
            if row[2] == country and row[0][:4] == str(year):
               sumOfDeaths += int(row[6])
        return {"total_deaths":sumOfDeaths,"success": True}
    if region and year:
        for row in db:
            if row[3] == region and row[0][:4] == str(year):
                sumOfDeaths += int(row[6])
        return {"total_deaths":sumOfDeaths,"success": True}

    if country:
        for row in db:
            if row[2] == country:
                sumOfDeaths += int(row[6])
        return {"total_deaths":sumOfDeaths,"success": True}

    if region:
        for row in db:
            if row[3] == region:
                sumOfDeaths += int(row[6])
        return {"total_deaths":sumOfDeaths, "success": True}

    for row in db:
        sumOfDeaths += int(row[6])
    return {"total_deaths":sumOfDeaths,"success": True}
   except Exception as e:
    print("An error occurred:", str(e))
    return {"error": "An error occurred while processing the request.","success": False}


def getMaxDeaths(start_date, end_date):
    
    maxDeaths = 0
    deaths = 0
    maxDeathsCountry = None
    countries = {}
    try:
        for row in db:
            if not row[2] in countries:
                countries[row[2]] = 0


        if start_date and end_date:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")

            for country in countries.keys():
                deaths = 0  # Reset deaths for each country
                for row in db:
                    row_date = datetime.strptime(row[0], "%Y-%m-%d")
                    if start_date <= row_date <= end_date and row[2] == country:
                        deaths += int(row[6])

                if deaths > maxDeaths:
                    maxDeaths = deaths
                    max_deaths_country = country

            return {"country": max_deaths_country, "Death count:":maxDeaths, "success": True}   
        
        for country in countries.keys():
            for row in db:
                if row[2] == country:
                    deaths = deaths + int(row[6])
            if deaths > maxDeaths:
                maxDeaths = deaths
                maxDeathsCountry = country
            deaths = 0
        return {"country": maxDeathsCountry, "Death count:":maxDeaths, "success": True}

    except Exception as e:
        print("An error occurred:", str(e))
        return {"error": "An error occurred while processing the request."}

def getMinDeaths(start_date, end_date):


    minDeaths = float('inf')  # Initialize min_deaths with infinity
    deaths = 0
    min_deaths_country = None
    countries = {}
    try:
        for row in db:
            if not row[2] in countries:
                countries[row[2]] = 0


        if start_date and end_date:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")

            for country in countries.keys():
                deaths = 0  # Reset deaths for each country
                for row in db:
                    row_date = datetime.strptime(row[0], "%Y-%m-%d")
                    if start_date <= row_date <= end_date and row[2] == country:
                        deaths += int(row[6])

                if deaths < minDeaths:
                    minDeaths = deaths
                    min_deaths_country = country

            return {"country": min_deaths_country, "Death count:":minDeaths, "success": True}   
        
        for country in countries.keys():
            deaths = 0  # Reset deaths for each country
            for row in db:
                if row[2] == country:
                    deaths += int(row[6])

            if deaths < minDeaths:
                minDeaths = deaths
                min_deaths_country = country

        return {"country": min_deaths_country, "Death count:":minDeaths, "success": True}
    
    except Exception as e:
        print("An error occurred:", str(e))
        return {"error": "An error occurred while processing the request."}
    
def getAvgDeaths():

    count = 0
    avg_deaths = 0.000
    sumOfDeaths = 0
    countries = {}
    try:
        for row in db:
            sumOfDeaths = sumOfDeaths + int(row[6])
        avg_deaths = float(sumOfDeaths /len(db))
        return{"Average deaths" : avg_deaths, "success": True}
    except Exception as e:
        print("An error occurred:", str(e))
        return {"error": "An error occurred while processing the request."}

@app.get("/", response_class= HTMLResponse)
async def doc_redirect():
    """Api's base route that displays the information created above in the ApiInfo section."""
    try:
        return RedirectResponse(url="/docs")
    except Exception as e:
        print("An error occurred:", str(e))
        return {"error": "An error occurred while processing the request."}


@app.get("/countries")
async def countries():
    """
    Fetches the unique countries from the database.

    - **Returns:**
      - (list) : A list of unique country names.

    #### Example:

    [http://127.0.0.2:8000/docs#/default/countries_countries_get](http://127.0.0.2:8000/docs#/default/countries_countries_get)

    #### Response:

        {
            "countries": ["Afghanistan", "Albania", "Algeria", ...],
            "success": true
        }

    """
    try:
        return getUniqueCountries()
    except Exception as e:
        print("An error occurred:", str(e))
        return {"error": "An error occurred while processing the request.", "success": False}


@app.get("/regions")
async def regions():
    """
    Fetches the unique regions from the database.

    - **Returns:**
      - (list) : A list of unique region names.

    #### Example:

    [http://127.0.0.2:8000/docs#/default/regions_regions_get](http://127.0.0.2:8000/docs#/default/regions_regions_get)

    #### Response:

        {
            "regions": ["AFRO", "AMRO", "EMRO", ...],
            "success": true
        }

    """
    try:
        return getUniqueRegions()
    except Exception as e:
        print("An error occurred:", str(e))
        return {"error": "An error occurred while processing the request.","success": False}


@app.get("/deaths")
async def get_deaths(country: str = None, region: str = None, year: int = None):
    """
    Calculates the total deaths based on the provided filters (country, region, year).

    - **Params:**
      - country (str): A country name.
      - region (str): A region name.
      - year (int): A 4-digit year.

    - **Returns:**
      - (dict): A dictionary containing the total deaths based on the filters.

    #### Example 1:

    [http://127.0.0.2:8000/deaths?country=Brazil](http://127.0.0.2:8000/deaths?country=Brazil)

    #### Response 1:

        {
            "total_deaths": 703399,
            "success": true,
        }

    #### Example 2:

    [http://127.0.0.2:8000/deaths?region=EMRO&year=2023](http://127.0.0.2:8000/deaths?region=EMRO&year=2023)

    #### Response 2:

        {
            "total_deaths": 2246,
            "success": true,
        }

    #### Example 3:

    [http://127.0.0.2:8000/deaths?country=Brazil&year=2022](http://127.0.0.2:8000/deaths?country=Brazil&year=2022)

    #### Response 3:

        {
            "total_deaths": 74917,
            "success": true
        }  

    #### Example 4:

    [http://127.0.0.2:8000/docs#/default/get_deaths_deaths_get](http://127.0.0.2:8000/docs#/default/get_deaths_deaths_get)

    #### Response 4:

        {
            "total_deaths": 6945714,
            "success": true,
        }

    """
    try:
        return getTotalDeaths(country, region, year)
    except Exception as e:
        print("An error occurred:", str(e))
        return {"error": "An error occurred while processing the request.","success": False}
    
    
@app.get("/max_deaths")
async def max_deaths(start_date: str = None, end_date: str = None):
    """
    Calculates the country with the highest number of deaths within the given date range.

    - **Params:**
      - start_date (str): The start date in the format "YYYY-MM-DD".
      - end_date (str): The end date in the format "YYYY-MM-DD".

    - **Returns:**
      - (dict): A dictionary containing the country with the highest deaths and its death count.

    #### Example 1:

    [http://127.0.0.2:8000/max_deaths?start_date=2021-01-31&end_date=2021-03-30](http://127.0.0.2:8000/max_deaths?start_date=2021-01-31&end_date=2021-03-30)

    #### Response 1:

        {
            "country": "United States of America",
            "Death count": 103845,
            "success": true
        }

    #### Example 2:

    [http://127.0.0.2:8000/max_deaths](http://127.0.0.2:8000/max_deaths)

    #### Response 2:

        {
            "country": "United States of America",
            "Death count:": 1127152,
            "success": true
        }

    """
    try:
        return getMaxDeaths(start_date, end_date)
    except Exception as e:
        print("An error occurred:", str(e))
        return {"error": "An error occurred while processing the request."}
    

@app.get("/min_deaths")
async def min_deaths(start_date: str = None, end_date: str = None):

    """
    Calculates the country with the lowest number of deaths within the given date range.

    - **Params:**
      - start_date (str): The start date in the format "YYYY-MM-DD".
      - end_date (str): The end date in the format "YYYY-MM-DD".

    - **Returns:**
      - (dict): A dictionary containing the country with the lowest deaths and its death count.

    #### Example 1:

    [http://127.0.0.2:8000/min_deaths?start_date=2021-01-31&end_date=2021-04-30](http://127.0.0.2:8000/min_deaths?start_date=2021-01-31&end_date=2021-04-30)

    #### Response 1:

        {
            "country": "American Samoa",
            "Death count:": 0,
            "success": true
        }
    
    #### Example 2:

    [http://127.0.0.2:8000/min_deaths](http://127.0.0.2:8000/min_deaths)

    #### Response 2:

    
        {
            "country": "Democratic People's Republic of Korea",
            "Death count:": 0,
            "success": true
        }

    """
    try:
        return getMinDeaths(start_date, end_date)
    except Exception as e:
        print("An error occurred:", str(e))
        return {"error": "An error occurred while processing the request.", "success": False}

@app.get("/avg_deaths")
async def avg_deaths():
    """
    Calculates the average number of deaths across all countries.

    - **Returns:**
      - (dict): A dictionary containing the average number of deaths.

    #### Example:

    [http://127.0.0.2:8000/avg_deaths](http://127.0.0.2:8000/avg_deaths)

    #### Response:

    {
    
        "Average deaths": 23.149139120523127

    }

    """
    try:
        return getAvgDeaths()
    except Exception as e:
        print("An error occurred:", str(e))
        return {"error": "An error occurred while processing the request.", "success": False}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.2", port=8000, log_level="debug", reload=True) 
