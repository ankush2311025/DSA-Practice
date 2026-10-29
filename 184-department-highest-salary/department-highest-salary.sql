# Write your MySQL query statement below
select d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
from employee e 
join department d
on d.id = e.departmentid
where e.salary = (
    select max(e1.salary) 
    from employee e1
    where e1.departmentid = e.departmentid
);
