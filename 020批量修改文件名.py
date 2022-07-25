import os


def create_files1():
    for i in range(10):
        file_name = 'file/file_' + str(i + 1) + '.txt'
        print(file_name)
        f = open(file_name, 'w')
        f.close()
        

# create_files1()

def create_files2():
    os.chdir('file')
    for i in range(10, 20):
        file_name = 'file_' + str(i + 1) + '.txt'
        print(file_name)
        f = open(file_name, 'w')
        f.close()
    os.chdir('../')
    
    
# create_files2()


def modify_filename():
    buf_list = os.listdir('file')
    print(buf_list)
    for file in buf_list:
        file_name = 'py_' + file
        os.rename('file/' + file, 'file/' + file_name)


# modify_filename()
