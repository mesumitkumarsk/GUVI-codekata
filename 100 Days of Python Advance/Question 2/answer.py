import json

# Read the JSON string
json_string = input()

# Parse the JSON string into a list of dictionaries
people = json.loads(json_string)

# Filter the list to get names of people aged 30 or above and with nationality "USA"
matching_people = [person["name"] for person in people if person["age"] >= 30 and person["nationality"] == "USA"]

# Print the names separated by a space, or "No matching people found" if no matches
if matching_people:
    print(" ".join(matching_people))
else:
    print("No matching people found")
