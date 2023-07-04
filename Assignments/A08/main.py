from fastapi import FastAPI, Query
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import csv


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

    for row in db:
        # print(row)
        if not row[2] in countries:
            countries[row[2]] = 0

    return list(countries.keys())


def getUniqueregions():
    regions = {}

    for row in db:
        if not row[4] in regions:
            regions[row[3]] = 0

    return list(regions.keys())


def getTotalDeaths(country, region, year):
    sumOfDeaths = 0
    if country and region:
        return {"error": "Cannot provide both country and region parameters. Please provide either country or region."}

    if country and year:
        for row in db:
            if row[2] == country and row[0][:4] == str(year):
                sum_of_deaths = sumOfDeaths + int(row[6])
        return {"country_year_deaths": sum_of_deaths}

    if region and year:
        for row in db:
            if row[3] == region and row[0][:4] == str(year):
                sumOfDeaths = sumOfDeaths + int(row[6])
        return {"country_year_deaths": sumOfDeaths}

    if country:
        for row in db:
            if row[2] == country:
                sumOfDeaths = sumOfDeaths + int(row[6])
        return {"total_deaths": sumOfDeaths}

    if region:
        for row in db:
            if row[3] == region:
                sumOfDeaths = sumOfDeaths + int(row[6])
        return {"total_deaths": sumOfDeaths}

    for row in db:
        sumOfDeaths = sumOfDeaths + int(row[6])
    return {"total_deaths": sumOfDeaths}


@app.get("/")
async def doc_redirect():
    """Api's base route that displays the information created above in the ApiInfo section."""
    return RedirectResponse(url="/docs")


@app.get("/countries/")
async def countries():
    return {"countries": getUniqueCountries()}


@app.get("/regions/")
async def regions():
    return {"Regions": getUniqueregions()}

# Route: /deaths
# Retrieves total deaths for all countries or total deaths for a specific country/region in a specific year


@app.get("/deaths")
async def get_deaths(country: str = None, region: str = None, year: int = None):
    return {"Number of deaths": getTotalDeaths(country, region, year)}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.3", port=5000,
                log_level="debug", reload=True)  # host="127.0.0.1"
