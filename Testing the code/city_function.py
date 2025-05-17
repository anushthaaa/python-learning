def get_city(city, country, population = "50000"):
    
    if population:
        details = city  + "," + " " + country + " - " + population
    else:
        details = city + "," + " " + country
    return details.title()