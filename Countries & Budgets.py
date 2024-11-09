def choose_countries(budget, costs):
    total_cost = 0
    chosen_countries = []
    for country, cost in costs.items():
        if total_cost + cost > budget:
            break
        total_cost += cost
        chosen_countries.append(country)
    return chosen_countries

chosen_countries = choose_countries(travel_budget, country_costs)
print(chosen_countries) # Prints ['France', 'Italy', 'Spain', 'Germany']

def calculate_cost(countries, costs):
    total_cost = 0
    for country in countries:
        total_cost += costs[country]
    return total_cost

total_cost = calculate_cost(chosen_countries, country_costs)
print(total_cost) # Prints 4400
