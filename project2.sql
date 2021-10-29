CREATE DATABASE employee_proj;


CREATE SCHEMA proj; 


USE employee_proj;

CREATE TABLE departments (
	department_id INT AUTO_INCREMENT PRIMARY KEY,
	department_name VARCHAR (30) NOT NULL,
    headquarters_address_id INT
);

CREATE TABLE address(
    address_id INT AUTO_INCREMENT PRIMARY KEY,
	street VARCHAR (40),
	city VARCHAR (30) NOT NULL,
	state VARCHAR (25)
);

CREATE TABLE employees(
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
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
JOIN
    address a
ON
    e.address_id = a.address_id
JOIN
    departments d
ON
    e.department_id = d.department_id;

--     - the 5 highest paid and lowest paid employees

SELECT 
    CONCAT(first_name,' ' ,last_name) AS 'Highest paid employees' , salary
FROM 
    employees
ORDER BY
	salary DESC
LIMIT
	5;


SELECT 
    CONCAT(first_name,' ' ,last_name) AS 'Lowest paid employees' , salary
FROM 
    employees
ORDER BY 
    salary 
LIMIT
	5;

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
    state = MA;    
