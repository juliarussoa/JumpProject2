import mysql.connector
import csv
import yaml

#     - Create a Python Script that will read any CSV file and write the data to the database
def read_csv_and_write_to_database(filename, table_name):
    try: 
        with open(filename, "rt") as csv_file:
            csv_data = csv.reader(csv_file)
            header = next(csv_data)
            header = [h.strip() for h in header]
            header_string = ','.join(header)
            print(header_string)
            for row in csv_data:
                values = []
                for col in row:
                    try:
                        # Integers
                        int(col) # No Error if it is an Integer
                        values.append(col)
                    except ValueError:
                        # Strings
                        if col.strip() == "NULL":
                            values.append(f'{col.strip()}')
                        else:
                            values.append(f'"{col.strip()}"')

                values = ','.join(values)
               
                print(values)
                try:
                    mycursor.execute(f"INSERT INTO {table_name} ({header_string}) VALUES ({values})")
                except Exception as e:
                    print(e)
        mydb.commit()
    except FileNotFoundError: 
        print("File not found")
    print('Done Reading File', filename)

#     - Create a Python Script that will create the tables automatically
def create_tables():
    mycursor.execute("CREATE DATABASE employee_proj")

    mycursor.execute("CREATE TABLE departments (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR (30) NOT NULL, headquarters_address_id INT)")

    mycursor.execute("CREATE TABLE addresses (id INT AUTO_INCREMENT PRIMARY KEY, street VARCHAR (40) NOT NULL, city VARCHAR (30) NOT NULL, state VARCHAR (25) NOT NULL)")

    mycursor.execute("""
    CREATE TABLE employees (
        id INT AUTO_INCREMENT PRIMARY KEY, 
        name VARCHAR (100) NOT NULL,
        age INT,
        salary DECIMAL (8,2),
        department_id INT,
        address_id INT,
        manager_id INT, 
        FOREIGN KEY (department_id) REFERENCES departments (id),
        FOREIGN KEY (address_id) REFERENCES addresses (id),
        FOREIGN KEY (manager_id) REFERENCES employees (id)
    )""")


def export_to_csv(filename, header, results):
    with open(filename, "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for row in results:
            writer.writerow(row)

def export_to_yaml(filename, header, results):
    with open(filename, "wt") as file:
        l = []
        for row in results:
            l.append(dict(zip(header, row)))
        print(l)
        yaml.dump(l, file)

#     - Create a Python Script that will create the tables automatically
#     - Create a Python Script that will read any CSV file and write the data to the database
#     - Create a Python script that can execute each of the required SQL commands
#     - Export the results of the SQL queries to CSV, and YAML

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="employee_proj"
)

mycursor = mydb.cursor()

# Script Command
create_tables()
read_csv_and_write_to_database('addresses1.csv', 'addresses')
read_csv_and_write_to_database('departments1.csv', 'departments')
read_csv_and_write_to_database('employees1.csv', 'employees')


#The full data for each Employee with their address as a string, department name, and manager name 
# (if the employee has a manager_id, then he is a manager)

sql = """ SELECT 
    e.name AS 'Employee name', 
    CONCAT(a.street, ',' , a.city, ',', a.state) AS 'Employee address',
     d.name as 'Department Name',
     e.manager_id
 FROM 
     employees e
JOIN
     addresses a
 ON
     e.address_id = a.id
JOIN
     departments d
ON
    e.department_id = d.id"""

mycursor.execute(sql)
myresult = mycursor.fetchall()
header = [i[0] for i in mycursor.description]

export_to_csv('data1.csv', header, myresult)
export_to_yaml('data1.yml', header, myresult)

#the 5 highest paid and lowest paid employees
sql = """SELECT
    name AS 'Highest paid employees' , salary
FROM 
    employees
ORDER BY 
    salary DESC
LIMIT 5"""

mycursor.execute(sql)
myresult = mycursor.fetchall()
header = [i[0] for i in mycursor.description]

export_to_csv('data2.csv', header, myresult)
export_to_yaml('data2.yml', header, myresult)

sql = """SELECT
    name AS 'Lower paid employees' , salary
FROM 
    employees
ORDER BY 
    salary
LIMIT 5"""
mycursor.execute(sql)
myresult = mycursor.fetchall()
header = [i[0] for i in mycursor.description]

export_to_csv('data3.csv', header, myresult)
export_to_yaml('data3.yml', header, myresult)

#The total salary for each department, the manager's name, sorted by highest total
sql = """ SELECT  
     d.name,
     SUM(salary) 'Total salary per department'
FROM
    employees e
 JOIN
     departments d
ON
    e.department_id = d.id
 WHERE
     e.manager_id IS NOT NULL
 GROUP BY
     d.name
ORDER BY SUM(salary) DESC """
mycursor.execute(sql)
myresult = mycursor.fetchall()
header = [i[0] for i in mycursor.description]

export_to_csv('data4.csv', header, myresult)
export_to_yaml('data4.yml', header, myresult)

# Each employee that lives in a given state (The state can be hard coded for now)

sql = """SELECT
    e.name AS 'Employee name', a.state 
FROM
    employees e
 LEFT JOIN
   addresses a
 ON
    e.address_id = a.id
WHERE 
     a.state = 'MA' """
mycursor.execute(sql)
myresult = mycursor.fetchall()
header = [i[0] for i in mycursor.description]

export_to_csv('data5.csv', header, myresult)
export_to_yaml('data5.yml', header, myresult)
  