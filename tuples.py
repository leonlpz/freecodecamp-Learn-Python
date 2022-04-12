coordinates = (4 ,5) #tuples can´t be modified the values
# can´t be changed
print(coordinates[1])
coord_list = [(1, 4), (2, 5), (6, 4)] #I can create a list
# of tuples
coord_list.extend(coordinates)
coord_list.insert(1, "Hello")
print(coord_list)