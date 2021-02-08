my_list = [11,21,31,114,55321,34]

for value in my_list:
    if value > 100:
        print(value)

############

my_list = [11,21,31,114,55321,34]
my_results = []

for value in my_list:
    if value > 100:
        my_results.append(value)
print(my_results)

##############

my_list = [10,10]
index = len(my_list)
if index < 2:
    my_list.append(0)
else:
    my_list.append(my_list[-1] * my_list[-2])
print(my_list)

###############

my_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list = "qwerty9876"
for index in my_indexes:
    print(index, my_list[index])

###############

