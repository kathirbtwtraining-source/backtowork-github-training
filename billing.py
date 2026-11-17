
def calculate_bill(monthly_charge, call_charges, data_charges):
    return monthly_charge + call_charges + data_charges


def display_bill(customer_name, monthly_charge, call_charges, data_charges):
    total = calculate_bill(monthly_charge, call_charges, data_charges)

    print("Telecom Billing System")
    print("Customer:", customer_name)
    print("Monthly Charge: £", monthly_charge)
    print("Call Charges: £", call_charges)
    print("Data Charges: £", data_charges)
    print("Total Bill: £", total)


display_bill("John", 30, 15, 10)
