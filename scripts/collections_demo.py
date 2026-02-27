print("=" * 70)
print("PYTHON COLLECTIONS: LISTS, TUPLES, AND DICTIONARIES")
print("=" * 70)

# 1. WORKING WITH LISTS
print("\n1. LISTS - Ordered and Mutable Collections")
print("-" * 70)

tour_cities = ["Paris", "London", "Tokyo", "New York", "Barcelona"]
print(f"Original list: {tour_cities}")
print(f"First city: {tour_cities[0]}")
print(f"Last city: {tour_cities[-1]}")
print(f"Third city: {tour_cities[2]}")

tour_cities[1] = "Berlin"
print(f"\nAfter changing index 1: {tour_cities}")

tour_cities.append("Sydney")
print(f"After append: {tour_cities}")

tour_cities.insert(2, "Rome")
print(f"After insert at index 2: {tour_cities}")

tour_cities.remove("Tokyo")
print(f"After removing Tokyo: {tour_cities}")

removed_city = tour_cities.pop()
print(f"Popped city: {removed_city}")
print(f"List after pop: {tour_cities}")

print(f"\nList length: {len(tour_cities)}")
print("Iterating through cities:")
for i, city in enumerate(tour_cities):
    print(f"  {i}: {city}")

# 2. WORKING WITH TUPLES
print("\n2. TUPLES - Ordered and Immutable Collections")
print("-" * 70)

concert_date = (2024, 6, 15, "Madison Square Garden", 20000)
print(f"Concert tuple: {concert_date}")
print(f"Year: {concert_date[0]}")
print(f"Month: {concert_date[1]}")
print(f"Day: {concert_date[2]}")
print(f"Venue: {concert_date[3]}")
print(f"Capacity: {concert_date[4]}")

coordinates = (40.7128, -74.0060)
print(f"\nNYC Coordinates: {coordinates}")
print(f"Latitude: {coordinates[0]}")
print(f"Longitude: {coordinates[1]}")

print("\nDemonstrating immutability:")
try:
    concert_date[0] = 2025
except TypeError as e:
    print(f"ERROR: {e}")
    print("Tuples are immutable - cannot be modified after creation!")

rgb_color = (255, 128, 0)
print(f"\nRGB Color tuple: {rgb_color}")
print(f"Tuple length: {len(rgb_color)}")

# 3. WORKING WITH DICTIONARIES
print("\n3. DICTIONARIES - Key-Value Pairs")
print("-" * 70)

concert_info = {
    "artist": "The Celestials",
    "venue": "Madison Square Garden",
    "city": "New York",
    "capacity": 20000,
    "date": "2024-06-15",
    "sold_out": True,
    "genres": ["Rock", "Pop", "Alternative"]
}

print(f"Concert dictionary: {concert_info}")
print(f"\nArtist: {concert_info['artist']}")
print(f"Venue: {concert_info['venue']}")
print(f"Capacity: {concert_info['capacity']}")
print(f"Sold out: {concert_info['sold_out']}")

concert_info["sold_out"] = False
print(f"\nUpdated sold_out: {concert_info['sold_out']}")

concert_info["ticket_price"] = 150
concert_info["doors_open"] = "18:00"
print(f"Added ticket_price: {concert_info['ticket_price']}")
print(f"Added doors_open: {concert_info['doors_open']}")

del concert_info["genres"]
print(f"\nAfter deleting 'genres' key, keys are: {list(concert_info.keys())}")

print(f"\nAll keys: {list(concert_info.keys())}")
print(f"All values: {list(concert_info.values())}")

print("\nIterating through dictionary:")
for key, value in concert_info.items():
    print(f"  {key}: {value}")

ticket_sales = {
    "VIP": 500,
    "General": 15000,
    "Student": 4500
}
print(f"\nTicket sales: {ticket_sales}")
print(f"VIP tickets sold: {ticket_sales['VIP']}")
print(f"Total tickets: {sum(ticket_sales.values())}")

# 4. CHOOSING THE RIGHT DATA STRUCTURE
print("\n4. CHOOSING THE RIGHT DATA STRUCTURE")
print("-" * 70)

shopping_cart = ["Laptop", "Mouse", "Keyboard", "Monitor"]
print(f"\nShopping Cart (LIST): {shopping_cart}")
print("Use LIST: Order matters, items can be added/removed")

event_date = (2024, 12, 25)
print(f"\nEvent Date (TUPLE): {event_date}")
print("Use TUPLE: Fixed data that should never change")

user_profile = {
    "username": "celestial_fan",
    "email": "fan@example.com",
    "age": 25,
    "premium": True
}
print(f"\nUser Profile (DICTIONARY): {user_profile}")
print("Use DICTIONARY: Need to look up values by meaningful keys")

print("\n" + "=" * 70)
print("COMPARISON SUMMARY")
print("=" * 70)
print("""
LIST: [item1, item2, item3]
  - Ordered, indexed by position (0, 1, 2...)
  - Mutable (can add, remove, modify)
  - Use for: dynamic collections, sequences

TUPLE: (item1, item2, item3)
  - Ordered, indexed by position (0, 1, 2...)
  - Immutable (cannot change after creation)
  - Use for: fixed data, coordinates, return multiple values

DICTIONARY: {"key1": value1, "key2": value2}
  - Unordered, accessed by keys
  - Mutable (can add, remove, modify key-value pairs)
  - Use for: structured data, lookups, mappings
""")
print("=" * 70)
