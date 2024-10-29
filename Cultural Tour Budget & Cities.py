# Define the budget for the cultural tour
cultural_tour_budget = 2000

# Define the cost associated with each city visit
city_costs = {
    "Rome": 800,
    "Paris": 700,
    "Berlin": 500,
    "Amsterdam": 400,
}

# Initialize the total amount spent and the list of chosen cities
total_spent = 0
chosen_cities = []

# Use a while loop to selectively add cities to the tour list based on the budget
while total_spent < cultural_tour_budget and city_costs:
    # Retrieve a city and its associated cost
    city, cost = city_costs.popitem()  # This removes cities in the reverse order of insertion
    
    # Check if adding this city would exceed your budget
    if total_spent + cost <= cultural_tour_budget:
        # If not, update the total spent and add the city to your list
        total_spent += cost
        chosen_cities.append(city)

# Print the list of cities chosen for the cultural tour
print("Cities chosen for the cultural tour:", chosen_cities)
print("Total spent:", total_spent)
print("Remaining budget:", cultural_tour_budget - total_spent)
