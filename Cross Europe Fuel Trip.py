# Define a list named chosen_countries with countries selected for the road trip
chosen_countries = ["France", "Germany", "Spain"]

# Define a dictionary named country_fuel_costs with fuel costs for countries (per liter in currency units)
country_fuel_costs = {
    "France": 1.5,
    "Germany": 1.7,
    "Spain": 1.4
}

# Initialize a variable total_fuel_cost to 0
total_fuel_cost = 0

# Use a for loop to add up the fuel cost for each chosen country
for country in chosen_countries:
    total_fuel_cost += country_fuel_costs.get(country, 0)

# Calculate the average fuel cost per country
average_fuel_cost = total_fuel_cost / len(chosen_countries) if chosen_countries else 0

# Print the total fuel cost for the road trip
print("Total fuel cost for the road trip:", total_fuel_cost)

# Print the average fuel cost per country
print("Average fuel cost per country:", average_fuel_cost)
