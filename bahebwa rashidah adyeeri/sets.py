#store multiple items in asingle variable
#unchangeable but one can remove and add items
setone={"rice","matooke","irish"}
print(setone)

#duplicates in sets
setone={"rice","matoooke","irish","irish"}
print(setone)

#exercise find the length of your set,datatype,acessing items ,adding and removing items from the set
set_length = len(set)
print(set_length)

#acess the datatype
set_type = type(set)
print(set_type)

#accessing its items
for item in set:
    print(item)

    #adding items
    set.add("posho")
    
    #adding multiple items
    set.update("yams", "potatoes", "beans")
    print(set)

    #deleting items from the set
    set.remove("rice")
    #idiscard does not raise an error if the item is not found in the set:
    set.discard("matooke")
    print(set)


    
    