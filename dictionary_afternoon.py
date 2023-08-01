Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

# Print the value of the shoe size
print("Shoe Size:", Shoes["size"])
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

# Change the value "Nick" to "Adidas"
Shoes["brand"] = "Adidas"

# Print the updated dictionary
print(Shoes)
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

# Add the key/value pair "type": "sneakers" to the dictionary
Shoes["type"] = "sneakers"

# Print the updated dictionary
print(Shoes)
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40,
    "type": "sneakers"
}

# Get a list of all the keys in the dictionary
keys_list = list(Shoes.keys())

# Print the list of keys
print(keys_list)
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40,
    "type": "sneakers"
}

# Get a list of all the values in the dictionary
values_list = list(Shoes.values())

# Print the list of values
print(values_list)
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40,
    "type": "sneakers"
}

# Check if the key "size" exists in the dictionary
if "size" in Shoes:
    print("The key 'size' exists in the dictionary.")
else:
    print("The key 'size' does not exist in the dictionary.")
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40,
    "type": "sneakers"
}

# Loop through the dictionary and print each key-value pair
for key, value in Shoes.items():
    print(key, ":", value)
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40,
    "type": "sneakers"
}

# Remove the key "color" from the dictionary
Shoes.pop("color")

# Print the updated dictionary
print(Shoes)
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40,
    "type": "sneakers"
}

# Empty the dictionary
Shoes.clear()

# Print the empty dictionary
print(Shoes)
# Original dictionary
original_dict = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

# Making a copy of the original dictionary
copy_dict = original_dict.copy()

# Modifying the copy dictionary
copy_dict["age"] = 26

# Printing both dictionaries
print("Original Dictionary:", original_dict)
print("Copied Dictionary:", copy_dict)
# Creating a nested dictionary
student = {
    "name": "John",
    "age": 18,
    "grades": {
        "math": 90,
        "science": 85,
        "english": 95
    },
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "country": "USA"
    }
}

# Accessing values in the nested dictionary
print("Name:", student["name"])
print("Age:", student["age"])
print("Math Grade:", student["grades"]["math"])
print("City:", student["address"]["city"])
