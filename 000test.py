import random

schools = [[], [], []]
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

for teacher in teachers:
    num = random.randint(0, 2)
    schools[num].append(teacher)
    
print(schools)

