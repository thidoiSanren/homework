def city_country(city, country, population=''):
    city_name = city
    country_name = country
    population = population
    if population:
        place = str(city_name) + ', ' + str(country_name) + '-population ' + str(population)
    else:
        place = str(city_name) + ', ' + str(country_name)
    return place