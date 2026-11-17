
def calculate_bill(monthly_charge, call_charge, data_charge):
    return monthly_charge + call_charge + data_charge


def display_bill(customer_name, total_bill):
    print("Customer:", customer_name)
    print("Total Bill: £", total_bill)


customer_name = "John"
monthly_charge = 30
call_charge = 10
data_charge = 15

# Just added this for eidt commit test
Test = 123
#This comment going to delete it by delete command


total_bill = calculate_bill(monthly_charge, call_charge, data_charge)
display_bill(customer_name, total_bill)

