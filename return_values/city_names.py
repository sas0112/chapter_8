def city_country():
    city_name = input("please wrte down the city name: ").title()
    country = input("please write down the country: ").title()
    city_country_pairs[city_name] = country


city_country_pairs = {}
city_country()
city_country()
print(city_country_pairs)

