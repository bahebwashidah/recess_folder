names = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Check if the list has at least 2 items
if len(names) >= 2:
    second_item = names[1]
    print("The second item is:", second_item)
else:
    print("The list does not have a second item.")

names = ["Alice", "Bob", "Charlie", "David", "Eve"]
new_value = "Mallory"

if len(names) >= 1:
    names[0] = new_value
    print("The first item has been changed to:", new_value)
else:
    print("The list is empty. Cannot change the value.")
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
new_item = "Frank"

names.append(new_item)
print("The list with the new item:", names)
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
new_item = "Bathel"

if len(names) >= 2:
    names.insert(2, new_item)
    print("The list with the new item:", names)
else:
    print("The list does not have enough items to add at the specified index.")
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

if len(names) >= 4:
    removed_item = names.pop(3)
    print("The item removed from the list:", removed_item)
    print("The updated list:", names)
else:
    print("The list does not have a fourth item to remove.")
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

last_item = names[-1]
print("The last item in the list:", last_item)
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

last_item = names[-1]
print("The last item in the list:", last_item)
items = [1, 2, 3, 4, 5, 6, 7]

# Indexes 2, 3, and 4 correspond to the 3rd, 4th, and 5th items respectively
subset = items[2:5]

print("The 3rd, 4th, and 5th items are:", subset)
countries = ["United States", "Canada", "United Kingdom", "Germany", "France"]

# Make a copy of the countries list using the slice operator
countries_copy = countries[:]

print("Original countries list:", countries)
print("Copied countries list:", countries_copy)
countries = ["United States", "Canada", "United Kingdom", "Germany", "France"]

for country in countries:
    print(country)
animal_names = ["Lion", "Tiger", "Elephant", "Giraffe", "Monkey"]

# Sort the animal names in ascending order
ascending_order = sorted(animal_names)

# Sort the animal names in descending order
descending_order = sorted(animal_names, reverse=True)

print("Animal names in ascending order:", ascending_order)
print("Animal names in descending order:", descending_order)
animal_names = ["Lion", "Tiger", "Elephant", "Giraffe", "Monkey"]

# Filter animal names with the letter 'a'
animals_with_a = [name for name in animal_names if 'a' in name.lower()]

# Output the filtered animal names
print("Animal names with the letter 'a':", animals_with_a)
first_names = ["John", "Alice", "David"]
last_names = ["Smith", "Johnson", "Brown"]

full_names = [first + " " + last for first, last in zip(first_names, last_names)]

print("Full Names:", full_names)
