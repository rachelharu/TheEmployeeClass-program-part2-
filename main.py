import csv
import sys

FILENAME = "employees.csv"

#read the employees from the file
def read_employees():
  try:
    employees = []
    with open(FILENAME, newline="") as file:
      reader = csv.reader(file)
      for row in reader:
        employees.append(row)
    return employees
  except FileNotFoundError as error:
    print(f"Could not find {FILENAME} file.")
    exit_program()
  except Exception as e:
    print(type(e), e)
    exit_program()
    
#exiting the program
  def exit_program():
    print("Terminating program.")
    sys.exit()
    
#write employees to files
def write_employees(employees):
  try:
    with open(FILENAME, "w", newline="") as file:
      writer = csv.writer(file)
      writer.writerows(employees)
  except Exception as e:
    print(type(e), e)
    exit_program()

#add employee to the list
def add_employee(employees):
  empid = input("Enter the employee ID: ")
  sal = input("enter the salary of the employee: ")
  employee = [empid,sal]
  employees.append(employee)
  write_employees(employees)
  print(f"Employee {empid}: {sal} was added.\n")

#display the list of employees 
def list_employees(employees):
  for i, employee in enumerate(employees, start=1):
    print(f"{i} Employee ID: {employee[0]} (${employee[1]})")
  print()
  
employees = read_employees()
list_employees(employees)

