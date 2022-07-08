def fn(*args, **kwargs):
    print("args：", args)
    print("kwargs：", kwargs)
    print("=============================================================================================")
    
    # num = 0
    # for i in args:
    #     num = num + i
    # 
    # for j in kwargs.values():
    #     num = num + j
    # 
    # print(f"求和的结果是：{num}")
    
    
my_list = [1, 2, 3, 4, 5, 6]
my_dict = {'a': 7, 'b': 8, 'c': 9, 'd': 10}

fn(*my_list)  # 列表前加*叫拆包，相当于将列表中每一项数据作为位置参数进行传递
fn(*my_dict)  # 将my_dict 中的key作为位置实参进行传递
fn(**my_dict)  # 将my_dict 中的键值对作为关键字实参进行传递
