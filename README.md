# Data Engineer Interview

## Problem

A company intends to give its employees a pay increase. They have provided
you with a CSV containing all the employees, salary, and respective
department within the company. 

**DataFrame employees** (./employees.csv)
```
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | str    |
| salary      | int    |
| department  | str    |
+-------------+--------+
```

HR has allocated a budget of $10,000 for this round of raises, and would like to distribute this evenly across the departments. Write a solution to modify the salary column with the new salary adjustments.

Save the results. 

## Pick one of the following, time willing

### Bonus Problem

Write tests for your solution with pytest

### Bonus Problem

Spin up a MinIO Object Storage container with docker and persist the results to the object storage.

### Bonus Problem

Employees have been waiting anxiously for their raise, but HR insists that
we need to give them the following data before they roll out the salary changes:

total_salary_before
total_salary_now
total_salary_added

salaries_sorted

Write a solution to use the data from the previous problem to get the above data for HR.

Save the results.