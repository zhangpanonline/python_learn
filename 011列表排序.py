# sort(key=lambda 形参: (排序规则1， 排序规则2, ...))

my_list = [1, 3, 5, 4, 2, 1]
my_list.sort()
# print(my_list)

list1 = [
    {'name': 'd', 'age': 19},
    {'name': 'b', 'age': 16},
    {'name': 'a', 'age': 16},
    {'name': 'c', 'age': 20}
]
# list1.sort(key=lambda x: x['age'])
# print(list1)
# list1.sort(key=lambda x: x['name'])
# print(list1)

list2 = ['a', 'bc', 'thee', 'def']
list2.sort(key=len)
# print(list2)

list1.sort(key=lambda x: (x['age'], x['name']), reverse=True)
print(list1)

