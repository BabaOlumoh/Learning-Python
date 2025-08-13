
work_hours = [('Abby', 100), ('Billy', 400), ('Cassie', 800)]

def employee_hours_check(work_hours):
    current_max_hours = 0
    employee_name = ''
    for name, hours in work_hours:
        if hours > current_max_hours:
            current_max_hours = hours
            employee_name = name
        else:
            pass
    
    return (current_max_hours, name)

result  = employee_hours_check(work_hours)

print(result)