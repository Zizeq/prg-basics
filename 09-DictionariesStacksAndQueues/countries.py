countries = [
{"name":"Poland", "population":38000000},
{"name":"USA", "population":336523731},
{"name":"Mexico", "population":75541537},
{"name":"UK", "population":67187536},
{"name":"Brazil", "population":42334009}
]
print("COUNTRY    POPULATION")
for country in countries:
    print(f"{country['name']:<10} {country['population']}")