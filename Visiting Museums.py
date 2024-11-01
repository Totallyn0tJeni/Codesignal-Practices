world_museums = {
    "France": ["Louvre Museum", "Orsay Museum"],
    "Italy": ["Uffizi Gallery", "Vatican Museums"],
    "Spain": ["Prado Museum", "Reina Sofia Museum"],
    "Japan": ["Tokyo National Museum", "Kyoto National Museum"]
}

for country, museums in world_museums.items():
    print(f"In {country}, you should visit:")
    for museum in museums:
        print(f"- {museum}")
    print()  # Adds a blank line between countries for better readability
