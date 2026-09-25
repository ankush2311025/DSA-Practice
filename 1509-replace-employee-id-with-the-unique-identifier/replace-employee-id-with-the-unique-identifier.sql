# Write your MySQL query statement below
select e1.name , e2.unique_id
from employees as e1
left join employeeuni as e2
on e1.id = e2.id;