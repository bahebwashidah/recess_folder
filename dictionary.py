
#dictionary are ordered
my_dict={
"phone": "iphone",
"iphone_model":"iphone 15",
"year":2023,


}
print(my_dict)
print(len(my_dict))
print(type(my_dict))

#access items
z=my_dict["year"]
print(z)
y=my_dict.get("phone")
print(y)
my_dict = {"key1": 1, "key2": 2, "key3": 3}

# Get the list of values using the values() method
values_list = list(my_dict.values())

# Print the list of values
print(values_list)

my_dict = {"key1": 1, "key2": 2, "key3": 3}

key = "key4"  # Key that doesn't exist in the dictionary

# Check if the key exists in the dictionary
if key in my_dict:
    value = my_dict[key]
    print("Value:", value)
else:
    print("Key does not exist in the dictionary.")


my_dict = {"key1": 1, "key2": 2, "key3": 3}

# Print the dictionary before modifying
print("Before:", my_dict)

key = "key2"  # Key to modify
new_value = 42  # New value for the key

# Change the value of the key in the dictionary
my_dict[key] = new_value

# Print the dictionary after modifying
print("After:", my_dict)

my_dict = {"key1": 1, "key2": 2, "key3": 3}

# Print the dictionary before updating
print("Before:", my_dict)

# Create a dictionary or iterable with the items to update
update_dict = {"key2": 42, "key3": 99, "key4": 100}

# Update the dictionary with the new items
my_dict.update(update_dict)

# Print the dictionary after updating
print("After:", my_dict)

my_dict = {"key1": 1, "key2": 2, "key3": 3}

# Print the dictionary before adding items
print("Before:", my_dict)

# Approach 1: Assign a new key-value pair
new_key = "key4"
new_value = 42
my_dict[new_key] = new_value

# Print the dictionary after adding items using approach 1
print("After Approach 1:", my_dict)

# Approach 2: Use the update() method
new_items = {"key5": 99, "key6": 100}
my_dict.update(new_items)

# Print the dictionary after adding items using approach 2
print("After Approach 2:", my_dict)

my_dict = {"key1": 1, "key2": 2, "key3": 3}

# Print the dictionary before deleting items
print("Before:", my_dict)

# Approach 1: Using the del statement
del my_dict["key2"]

# Print the dictionary after deleting using approach 1
print("After Approach 1:", my_dict)

# Approach 2: Using the pop() method
my_dict.pop("key3")

# Print the dictionary after deleting using approach 2
print("After Approach 2:", my_dict)

my_dict = {"key1": 1, "key2": 2, "key3": 3}

# Loop through the dictionary using the items() method
for key, value in my_dict.items():
    print("Key:", key)
    print("Value:", value)
    print("---")


my_dict = {
    "nested_dict1": {
        "key1": 1,
        "key2": 2
    },
    "nested_dict2": {
        "key3": 3,
        "key4": 4
    }
}

# Loop through the outer dictionary
for outer_key, outer_value in my_dict.items():
    print("Outer Key:", outer_key)
    print("Outer Value:", outer_value)
    print("---")

    # Loop through the inner dictionaries
    for inner_key, inner_value in outer_value.items():
        print("Inner Key:", inner_key)
        print("Inner Value:", inner_value)
        print("-----")


