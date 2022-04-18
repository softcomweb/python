from model.employee import EmployeeModel
from database import db

employee1 = EmployeeModel(
    "lngalame", "Leadel", "Kolo", "Mr.Kolo", ["Programming", "Basketball"]
)
employee2 = EmployeeModel(
    "nbaby", "Nicole", "Kolo", "Mrs.Kolo", ["Programming", "Basketball"]
)
employee3 = EmployeeModel(
    "jbaby", "Joy", "Kolo", "Mrs.Kolo", ["Programming", "Basketball"]
)
employee4 = EmployeeModel(
    "jkolo", "Jamie", "Kolo", "Mr.Kolo", ["Programming", "Basketball"]
)
employee5 = EmployeeModel(
    "tkolo", "Tanja", "Kolo", "Mrs.Kolo", ["Programming", "Basketball"]
)
employee6 = EmployeeModel(
    "rkolo", "Ralf", "Kolo", "Mr.Kolo", ["Programming", "Basketball"]
)


employees = [employee1, employee2, employee3, employee4, employee5]

for employee in employees:
    print(employee.to_object())
    db.put_single_item(employee.to_object())


item = db.get_single_item("LoginAlias", pk=employee1.pk)
print(item)

#item =db.query_for_item("LoginAlias", )
