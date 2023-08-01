x = ("samsung", "iphone", "tecno", "redmi")
favorite_brand = x[1]

print("My favorite phone brand is:", favorite_brand)
x = ("samsung", "iphone", "tecno", "redmi")
second_last_item = x[-2]

print("The second-to-last item in the tuple:", second_last_item)
x = ("samsung", "iphone", "tecno", "redmi")
second_last_item = x[-2]

print("The second-to-last item in the tuple:", second_last_item)
x = ("samsung", "iphone", "tecno", "redmi")

# Convert the tuple to a list
x_list = list(x)

# Update "iphone" to "itel"
x_list[1] = "itel"

# Convert the list back to a tuple
x_updated = tuple(x_list)

print("Updated tuple:", x_updated)
x = ("samsung", "iphone", "tecno", "redmi")
new_tuple = x + ("Huawei",)

print("Updated tuple:", new_tuple)
x = ("samsung", "iphone", "tecno", "redmi")

# Loop through the tuple
for item in x:
    print(item)
x = ("samsung", "iphone", "tecno", "redmi")

# Convert the tuple to a list
x_list = list(x)

# Remove the first item from the list
del x_list[0]

# Convert the list back to a tuple
x_updated = tuple(x_list)

print("Updated tuple:", x_updated)
cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu"])

print("Cities in Uganda:", cities)
x = ("samsung", "iphone", "tecno", "redmi")

cities = ("Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu")

# Unpack the tuple into separate variables
city1, city2, city3, city4, city5 = cities

# Print the unpacked cities
print("City 1:", city1)
print("City 2:", city2)
print("City 3:", city3)
print("City 4:", city4)
print("City 5:", city5)

cities = ("Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu")

# Print the 2nd, 3rd, and 4th cities using index range
for i in range(1, 4):
    print("City", i + 1, ":", cities[i])
first_names = ("bahebwa", "rashidah")
last_names = ("adyeeri", "tahla")

# Join the two tuples
full_names = first_names + last_names

print("Full Names:", full_names)

colors = ("red", "green", "blue")

# Multiply the tuple by 3
multiplied_colors = colors * 3

print("Multiplied Colors:", multiplied_colors)
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

# Count the number of times 8 appears in the tuple
count_8 = thistuple.count(8)

print("Number of times 8 appears:", count_8)

