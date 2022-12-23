class Student(object):
    def __init__(self, stu_id, name, age, gender):
        self.stu_id = stu_id
        self.name = name
        self.age = age
        self.gender = gender
        
    def __str__(self):
        return f"{self.stu_id},{self.name},{self.age},{self.gender}"
    
