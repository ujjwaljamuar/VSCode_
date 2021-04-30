stock_prices=[('APPLE',200),('GOOGLE',400),('MICROSOFT',100)]
for items in stock_prices:
    print(items)
for items,prices in stock_prices:
    print(items,prices)
    print(prices+(0.1*prices))

#2
print('\n2 >\n')
work_hours=[('ujjwal',40),('vishal',0.5),('mishra',1)]
def employee_check(work_hours):
    current_max=0
    employee_of_the_month=''
    for employee,hours in work_hours:
        if hours>current_max:
            current_max=hours
            employee_of_the_month=employee
        else:
            pass
    return employee_of_the_month,current_max
result=employee_check(work_hours)
print(result)
#or
name,hours=employee_check(work_hours)
print(name)
print(hours)