from fastapi import FastAPI, Query
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import csv
from datetime import datetime

description = """🚀
## 4883 Software Tools
### Where awesomeness happens
"""


app = FastAPI(
    description=description,
)

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

    return list(countries.keys())



def getUniqueRegions():
    regions = {}

    try:
        for row in db:
            if not row[4] in regions:
                regions[row[3]] = 0
    except Exception as e:
        print("An error occurred:", str(e))
        return []

    return list(regions.keys())


def getTotalDeaths(country, region, year):
   sumOfDeaths = 0
   try:
    if country and region:
        return {"error": "Cannot provide both country and region parameters. Please provide either country or region."}
    if country and year:
        for row in db:
            if row[2] == country and row[0][:4] == str(year):
               sumOfDeaths += int(row[6])
        return {"country_year_deaths":sumOfDeaths}
    if region and year:
        for row in db:
            if row[3] == region and row[0][:4] == str(year):
                sumOfDeaths += int(row[6])
        return {"country_year_deaths":sumOfDeaths}

    if country:
        for row in db:
            if row[2] == country:
                sumOfDeaths += int(row[6])
        return {"total_deaths":sumOfDeaths}

    if region:
        for row in db:
            if row[3] == region:
                sumOfDeaths += int(row[6])
        return {"total_deaths":sumOfDeaths}

    for row in db:
        sumOfDeaths += int(row[6])
    return {"total_deaths":sumOfDeaths}
   except Exception as e:
    print("An error occurred:", str(e))
    return {"error": "An error occurred while processing the request."}


def getMaxDeaths(start_date, end_date):
    ### lets start
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

            return {"country": max_deaths_country, "Death count:":maxDeaths}   
        
        for country in countries.keys():
            for row in db:
                if row[2] == country:
                    deaths = deaths + int(row[6])
            if deaths > maxDeaths:
                maxDeaths = deaths
                maxDeathsCountry = country
            deaths = 0
        return {"country": maxDeathsCountry, "Death count:":maxDeaths}

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

            return {"country": min_deaths_country, "Death count:":minDeaths}   
        
        for country in countries.keys():
            deaths = 0  # Reset deaths for each country
            for row in db:
                if row[2] == country:
                    deaths += int(row[6])

            if deaths < minDeaths:
                minDeaths = deaths
                min_deaths_country = country

        return {"country_with_min_deaths": min_deaths_country, "Death count:":minDeaths}
    
    except Exception as e:
        print("An error occurred:", str(e))
        return {"error": "An error occurred while processing the request."}
    
def getAvgDeaths():
    count = 0
    avg_deaths = 0
    sumOfDeaths = 0
    countries = {}
    try:
        for row in db:
            # print(row)
            if not row[2] in countries:
                countries[row[2]] = 0
                count += 1
        for row in db:
            sumOfDeaths = sumOfDeaths + int(row[6])
        avg_deaths = sumOfDeaths // count
        return{avg_deaths}
    except Exception as e:
        print("An error occurred:", str(e))
        return {"error": "An error occurred while processing the request."}

@app.get("/")
async def doc_redirect():
    """Api's base route that displays the information created above in the ApiInfo section."""
    try:
        return RedirectResponse(url="/docs")
    except Exception as e:
        print("An error occurred:", str(e))
        return {"error": "An error occurred while processing the request."}


@app.get("/countries/")
async def countries():
    try:
        return {"countries": getUniqueCountries()}
    except Exception as e:
        print("An error occurred:", str(e))
        return {"error": "An error occurred while processing the request."}


@app.get("/regions/")
async def regions():
    try:
        return {"Regions": getUniqueRegions()}
    except Exception as e:
        print("An error occurred:", str(e))
        return {"error": "An error occurred while processing the request."}


@app.get("/deaths")
async def get_deaths(country: str = None, region: str = None, year: int = None):
    try:
        return {"Number of deaths": getTotalDeaths(country, region, year)}
    except Exception as e:
        print("An error occurred:", str(e))
        return {"error": "An error occurred while processing the request."}
    
    
@app.get("/max_deaths")
async def max_deaths(start_date: str = None, end_date: str = None):
    try:
        return{"country with maximum deaths":getMaxDeaths(start_date, end_date)}
    except Exception as e:
        print("An error occurred:", str(e))
        return {"error": "An error occurred while processing the request."}
    

@app.get("/min_deaths")
async def min_deaths(start_date: str = None, end_date: str = None):
    try:
        return{"country with min deaths":getMinDeaths(start_date, end_date)}
    except Exception as e:
        print("An error occurred:", str(e))
        return {"error": "An error occurred while processing the request."}

@app.get("/avg_deaths")
async def avg_deaths():
    try:
        return{"Average deaths":getAvgDeaths()}
    except Exception as e:
        print("An error occurred:", str(e))
        return {"error": "An error occurred while processing the request."}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.3", port=5000,
                log_level="debug", reload=True)  # host="127.0.0.1"
