# TODO: Define a list of temperatures
temperatures = [25, 32, 10, 18, 29, 8, 20]

# TODO: Write a loop to go through each temperature in the list
for temp in temperatures:
    # TODO: Add an 'if' statement to check if the temperature is over a really hot threshold
    if temp > 30:
        print(f"{temp}°C is really hot! Stay hydrated.")
        break  # Exit the loop if the temperature is really hot
    
    # TODO: Add an 'elif' condition before the general temperature message to check if it's too cold
    elif temp < 12:
        print(f"{temp}°C is too cold! Stay warm.")
        continue  # Skip to the next temperature
    
    # TODO: Print a message saying the temperature is nice for all other cases
    print(f"{temp}°C is nice. Enjoy your day!")
