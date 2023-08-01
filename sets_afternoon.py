
favorite_beverages = set(['Coffee', 'Mango Juice', 'Green Tea'])

favorite_beverages.add('Iced Tea')
favorite_beverages.add('Lemonade')
mySet = {"oven", "kettle", "microwave", "refrigerator"}

if "microwave" in mySet:
    print("Microwave is present in the set.")
else:
    print("Microwave is not present in the set.")
mySet = {"oven", "kettle", "microwave", "refrigerator"}

mySet.remove("kettle")

print("Updated set:", mySet)
mySet = {"oven", "kettle", "microwave", "refrigerator"}

for item in mySet:
    print(item)
mySet = {"apple", "banana", "orange", "grape"}
myList = ["kiwi", "melon"]

print("Original Set:", mySet)
print("Original List:", myList)

# Add elements from the list to the set
mySet.update(myList)

print("Updated Set:", mySet)
ages = {22}
names = {"bahebwa_rashidah_adyeeri"}

# Join the two sets
joined_set = ages.union(names)

print("Joined Set:", joined_set)
