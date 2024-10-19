# Travel profile has necessary details of the traveller, including insurance now
travel_profile = {
    "passport": True, 
    "visa": {"required": True, "available": False}, 
    "tickets": True,
    "insurance": True,
}

# Check if all required documents for travel are available
if travel_profile['passport'] and travel_profile['tickets'] and travel_profile['insurance']:
    if travel_profile['visa']['required'] and not travel_profile['visa']['available']:
        print("You need to apply for a visa.")
    else:
        print("You are ready to travel.")
else:
    advice = "General travel advice: "
    if not travel_profile['passport']:
        advice += "Make sure you have your passport, "
    if not travel_profile['tickets']:
        advice += "tickets, "
    if not travel_profile['insurance']:
        advice += "and insurance ready for hassle-free travel."
  
