#creating an empty list
my_list = []

#appending my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#inserting a number to my_list
my_list.insert(1, 15)

#adding another list
list = [50, 60, 70]

#extending my_list
my_list.extend(list)

#Removing last element
my_list.pop()

#sorting the list
my_list.sort()

#finding index of 30 and printing final list
index_30 = my_list.index(30)
print("Index of 3o:", index_30)

#print final list
print("Final list:", my_list)