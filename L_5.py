my_int = int(51008080880880)
my_int = str(my_int)
result = my_int.count('0')
print(result)

###############

my_int = int(2100102000)
my_int = str(my_int)
print(len(my_int) - len(my_int.rstrip('0')))

###############

my_list_1 = [1, 3, 5, 7, 9]
my_list_2 = [2, 4, 6, 8, 10]
my_result = []
for index, symbol in enumerate(my_list_1):
    if index % 2:
        my_result.append(symbol)
for index, symbol in enumerate(my_list_2):
    if not index % 2:
        my_result.append(symbol)
print(my_result)

################

my_list_1 = [1,3,2,4,5]
my_list_2 = [10, 20, 15, 25, 22]
my_result = []
for index, symbol in enumerate(my_list_1):
    if not symbol % 2:
        my_result.append(symbol)
for index, symbol in enumerate(my_list_2):
    if symbol % 2:
        my_result.append(symbol)
print(my_result)

#################

my_list = [1,2,3,4,5,8,9,8,4,4]
new_list = my_list[1:]
new_list.append(my_list[0])
print(new_list)

################

my_list = ['last',1,2,3,4,5,6,8,7,9,8,7,5]
value = my_list.pop(0)
my_list.append(value)
print(my_list)

###############

my_str = "43 больше чем 34 но меньше чем 56"
num = my_str.split()
result = []
for index in num:
    if index.isdigit():
        result.append(int(index))
print(sum(result))

################

my_str = '123456'
if not int(len(my_str)) % 2 == 0:
    my_str = my_str + '_'
else:
    my_str

my_list = [my_str[index:index + 2] for index in range(0, len(my_str), 2)]
print(my_list)

#################

my_str = "My_long str"
l_limit = "o"
r_limit = "t"
sub_str = my_str[my_str.find(l_limit) + 1 : my_str.find(r_limit)]
print(sub_str)

#################

my_str = "My long string"
l_limit = "o"
r_limit = "g"
sub_str = my_str[my_str.find(l_limit) + 1 : my_str.rfind(r_limit)]
print(sub_str)

###############

my_list = [2,4,1,5,3,9,0,7]
result = 0
for i in range(1, len(my_list) - 2):
    if my_list[i] > my_list[i + 1] + my_list[i - 1]:
        result += 1
print(result)