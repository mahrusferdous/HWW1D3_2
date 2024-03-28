our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

both_airline_fly = our_routes.intersection(competitor_routes)
print(both_airline_fly)

difference = our_routes.difference(competitor_routes)
print(difference)

print("Neither airline shares any that isn't displayed in either.")