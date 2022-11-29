my_str = 'hello world'
my_dict = {}

for i in my_str:
    if i != ' ':
        my_dict[i] = my_str.count(i)
        

print(my_dict)
