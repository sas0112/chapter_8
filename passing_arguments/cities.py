def describe_city(city_name, country_name="china"):
    print(city_name.title() + " is in " + country_name.title())


describe_city("beijing")
describe_city("new york", "the united states")
describe_city(country_name="japan", city_name="kyoto")
