from app.models import Employee

import string
import random
# exec(open(r'C:\Users\sruja\Desktop\softech.py\Django\csv_project\app\db_shell.py').read())

des = ['software Engineer', 'Senior Software Engineer', 'Linux Administrator', 'Associate', 'CEO', 'Python Devp']

for i in range(20):
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for i in range(10)) 
    
    letters = string.digits
    sal = ''.join(random.choice(letters) for i in range(5)) 
    
    letters = string.ascii_uppercase
    comp = ''.join(random.choice(letters) for i in range(10)) 
    
    design = random.choice(des)
    # print(design)
    emp = Employee(name=name, salary=sal, company=comp, designation=design)
    emp.save()