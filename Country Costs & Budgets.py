def choose_countries(budget, cost_threshold, costs):
    total_cost = 0
    chosen_countries = []

    for country, cost in costs.items():
        # Check if the country cost exceeds the cost threshold
        if cost > cost_threshold:
            print(f"Skipping {country}: Cost (${cost}) exceeds the cost threshold (${cost_threshold}).")
            continue
        
        # Check if adding this country would exceed the overall budget
        if total_cost + cost > budget:
            print(f"Skipping {country}: Adding it would exceed the total budget (${budget}).")
            continue
        
        # Add country to chosen list and update total cost
        total_cost += cost
        chosen_countries.append(country)

    return chosen_countries

def calculate_cost(countries, costs):
    return sum(costs[country] for country in countries)

# Sample data for demonstration
travel_budget = 5000
cost_threshold = 1000  # Maximum cost preference for each country
country_costs = {'France': 1200, 'Italy': 1500, 'Spain': 800, 'Germany': 900, 'Greece': 1100}

# Choosing countries based on budget and cost threshold
chosen_countries = choose_countries(travel_budget, cost_threshold, country_costs)
trip_cost = calculate_cost(chosen_countries, country_costs)

print(f"The countries selected within budget and cost preference are: {chosen_countries}")
print(f"The total cost of the trip is: ${trip_cost}")
