--  SQL:
--   - Create tables for Employee, Address, and Department 
--   - Import your CSV data that you created for the Python portion
--   - commands:
--     - The full data for each Employee with their address as a string, department name, and manager name
--     - the 5 highest paid and lowest paid employees
--     - The total salary for each department, the manager's name, sorted by highest total
--     - Each employee that lives in a given state (The state can be hard coded for now)
-- - Bonus:
--   - Attempt as many as you can!
--   - On the job, you will often be asked to learn and implement new technologies 
--   - Look into Python Packages that will allow you to connect to your SQL instance
--   - SQLAlchemy is a good place to start
--   - scripts:
--     - Create a Python Script that will create the tables automatically
--     - Create a Python Script that will read any CSV file and write the data to the database
--     - Create a Python script that can execute each of the required SQL commands
--     - Export the results of the SQL queries to CSV, and YAML
-- data: 
-- - employees:
--   - id
--   - name
--   - age
--   - salary
--   - department id
--   - address id
--   - manager id
-- - address:
--   - id
--   - street
--   - city
--   - state
-- - department:
--   - id
--   - name
--   - manager id
--   - headquarters address id

CREATE DATABASE employee_proj;
GO

CREATE SCHEMA proj; 
GO

USE employee_proj;

CREATE TABLE departments (
	department_id INT IDENTITY(1,1) PRIMARY KEY,
	department_name VARCHAR (30) NOT NULL,
    headquarters_address_id INT
);

CREATE TABLE address(
    address_id INT IDENTITY(1,1) PRIMARY KEY,
	street VARCHAR (40),
	city VARCHAR (30) NOT NULL,
	state VARCHAR (25)
);

CREATE TABLE employees(
    emp_id INT IDENTITY(1,1) PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR (100) NOT NULL,
    age INT,
    salary DECIMAL (6,2),
    department_id INT,
    address_id INT,
    manager_id INT,
	FOREIGN KEY (department_id) REFERENCES departments (department_id),
    FOREIGN KEY (address_id) REFERENCES address (address_id),
    FOREIGN KEY (manager_id) REFERENCES employees (emp_id)
);

-- The full data for each Employee with their address as a string, department name, and manager name (if the employee has a manager_id, then he is a manager)
SELECT 
    CONCAT(first_name, ' ', last_name) AS 'Employee name', 
    CONCAT(street, ',' , city, ',', state) AS 'Employee address',
    department_name,
    manager_id
FROM 
    employees e
FULL OUTER JOIN
    address a
ON
    e.address_id = a.address_id
FULL OUTER JOIN
    departments d
ON
    e.department_id = d.department_id;

--     - the 5 highest paid and lowest paid employees

SELECT TOP 5
    CONCAT(first_name,' ' ,last_name) AS 'Highest paid employees' , salary
FROM 
    employees
ORDER BY 
    salary DESC

SELECT TOP 5
    CONCAT(first_name,' ' ,last_name) AS 'Lowest paid employees' , salary
FROM 
    employees
ORDER BY 
    salary ;

 -- The total salary for each department, the manager's name, sorted by highest total

 SELECT 
    CONCAT(first_name,' ' ,last_name) AS 'Employee name', department_name,
    SUM(salary) 'Total salary per department'
FROM
    employees e
JOIN
    departments d
ON
    e.department_id = d.department_id
WHERE
    manager_id IS NOT NULL
GROUP BY
    department_name
ORDER BY
    'Total salary per department';

-- Each employee that lives in a given state (The state can be hard coded for now)

SELECT
    CONCAT(first_name,' ' ,last_name) AS 'Employee name', state 
FROM
    employees e
LEFT JOIN
    address a
ON
    e.address_id = a.address_id
WHERE 
    state = ;    
