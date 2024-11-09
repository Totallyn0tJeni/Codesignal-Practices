# TODO: Declare a global list to keep track of visited landmarks
visited_landmarks = []

# TODO: Define a function named log_landmark that takes two parameters: landmark and city
def log_landmark(landmark, city):
    global visited_landmarks  # Use the global list inside the function
    # TODO: Add the landmark and its city to the global list in the format "landmark in city"
    visited_landmarks.append(f"{landmark} in {city}")
    print(f"Logged: {landmark} in {city}")

# TODO: Call the log_landmark function with examples e.g., "Eiffel Tower" and "Paris"
log_landmark("Eiffel Tower", "Paris")
log_landmark("Colosseum", "Rome")
log_landmark("Statue of Liberty", "New York")

# TODO: Print the list of visited landmarks
print("Visited Landmarks:", visited_landmarks)
