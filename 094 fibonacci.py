def fn(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
        
    
if __name__ == '__main__':
    my_gen = fn(10)
    for val in my_gen:
        print(val, end=' ')
        